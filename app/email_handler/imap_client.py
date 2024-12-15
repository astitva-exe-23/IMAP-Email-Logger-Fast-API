import imaplib
import email
from email.header import decode_header
from app.config import settings


class EmailClient:
    def __init__(self):
        self.host = settings.email_host
        self.port = settings.email_port
        self.user = settings.email_user
        self.password = settings.email_password
        self.connection = None

    
    def connect(self):
        try:
            self.connection = imaplib.IMAP4_SSL(self.host,self.port)
            self.connection.login(self.user,self.password)
        except Exception as e:
            raise Exception(f"Failed to Connect to Email Server:{e}")
        
    
    def fetch_unread_emails(self):
        self.connection.select("inbox")
        status,messages = self.connection.search(None,"UNSEEN")
        email_ids = messages[0].split()
        emails=[]

        for email_id in email_ids:
            _,msg_data = self.connection.fetch(email_id,"(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part,tuple):
                    msg = email.message_from_bytes(response_part[1])
                    sender = decode_header(msg["From"])[0][0]
                    subject = decode_header(msg["Subject"])[0][0]
                    timestamp = msg["Date"]
                    emails.append({"Sender":sender,"subject":subject,"timestamp":timestamp})
        
        return emails
    
    def mark_as_read(self,email_id):
        self.connection.store(email_id,'+FLAGS','\\Seen')

    def disconnect(self):
        if self.connection:
            self.connection.logout()


