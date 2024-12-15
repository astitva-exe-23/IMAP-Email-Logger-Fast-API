from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

DATABASE_URL = settings.db_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer,primary_key=True,index=True)
    sender = Column(String,index=True)
    subject = Column(String)
    timestamp = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)