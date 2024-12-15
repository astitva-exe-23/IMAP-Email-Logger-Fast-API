from fastapi import FastAPI
from app.email_handler.database import init_db
from app.routes.email_routes import router as email_router


app = FastAPI()
app.include_router(email_router)


async def startup():
    init_db()

app.add_event_handler("startup",startup)

@app.get("/")
async def root():
    return{
        "message":"Welcome to email proccessing project for nexagen"
    }