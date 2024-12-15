import asyncio
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import selectinload,Session
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.email_handler.imap_client import EmailClient
from app.email_handler.database import SessionLocal, Email
import time
from sqlalchemy.exc import OperationalError

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/fetch-emails")
async def fetch_emails(db: Session = Depends(get_db)):
    client = EmailClient()
    try:
        client.connect()
        
        emails = client.fetch_unread_emails()
        
        records_to_insert = []
        for email_data in emails:
            try:
                records_to_insert.append({
            "sender": email_data.get("Sender"),
            "subject": email_data.get("subject"),
            "timestamp": email_data.get("timestamp")
             })
            except Exception as e:
                print(f"Failed to process email data: {e}")
        
        if records_to_insert:
            # Perform bulk insert
             db.execute(insert(Email),records_to_insert)
             db.commit()
             print(f"Successfully inserted {len(records_to_insert)} emails.")
        else:
            print("No new emails found.")
        
        client.disconnect()
        return {"message": "Emails fetched and stored successfully.", "count": len(emails)}
    except OperationalError as e:
        print(f"Database operation failed: {str(e)}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Unexpected error during email fetch/store operation: {e}")
        return {"error": str(e)}

@router.get("/start-periodic-scan")
async def start_periodic_scan(db: Session = Depends(get_db)):
    async def periodic_scan():
        while True:
            try:
                await fetch_emails(db)
                print("Periodic email scan completed successfully.")
                await asyncio.sleep(30)  # Scan every 5 minutes
            except Exception as e:
                print(f"Error during periodic scan: {e}")
                await asyncio.sleep(60)  # Wait for 60 seconds before retrying

    # Start the background task
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(periodic_scan())
    
    return {"message": "Started periodic email scanning in the background."}
