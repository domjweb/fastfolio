# All code removed: file deleted for PostgreSQL cleanup
import os
import logging
from sqlalchemy import create_engine, Column, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from typing import List, Dict, Any, Optional
import uuid

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    company = Column(String, nullable=True)
    subject = Column(String, nullable=False)
    message = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(String, nullable=False)
    status = Column(String, default="new")

class PostgreSQLDatabase:
    def __init__(self):
        # Azure Functions environment variables
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            logging.warning("DATABASE_URL not found. Database operations will be logged only.")
            self.engine = None
            self.SessionLocal = None
        else:
            try:
                self.engine = create_engine(self.database_url, pool_pre_ping=True)
                self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
                # Create tables
                Base.metadata.create_all(bind=self.engine)
                logging.info("✅ Connected to PostgreSQL database")
            except Exception as e:
                logging.error(f"❌ Failed to connect to PostgreSQL: {e}")
                self.engine = None
                self.SessionLocal = None

    def is_connected(self) -> bool:
        if not self.engine:
            return False
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except Exception:
            return False

    def get_db(self) -> Session:
        if not self.SessionLocal:
            raise Exception("Database not connected")
        db = self.SessionLocal()
        try:
            return db
        except Exception:
            db.close()
            raise

    def create_contact(self, contact_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new contact (synchronous for Azure Functions)"""
        if not self.is_connected():
            logging.warning("Database not connected, contact will be logged only")
            # Generate a fake ID for consistent response
            contact_id = str(uuid.uuid4())
            logging.info(f"Contact submission (no DB): {contact_data}")
            return {
                "id": contact_id,
                "status": "logged",
                **contact_data
            }
        
        try:
            db = self.get_db()
            # Add ID and timestamp if not present
            if 'id' not in contact_data:
                contact_data['id'] = str(uuid.uuid4())
            if 'created_at' not in contact_data:
                contact_data['created_at'] = datetime.now().isoformat()
            if 'status' not in contact_data:
                contact_data['status'] = 'new'
                
            contact = Contact(**contact_data)
            db.add(contact)
            db.commit()
            db.refresh(contact)
            
            result = {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "company": contact.company,
                "subject": contact.subject,
                "message": contact.message,
                "phone": contact.phone,
                "created_at": contact.created_at,
                "status": contact.status
            }
            db.close()
            return result
        except SQLAlchemyError as e:
            if 'db' in locals():
                db.rollback()
                db.close()
            raise Exception(f"Failed to create contact: {str(e)}")

    async def get_all_contacts(self) -> List[Dict[str, Any]]:
        if not self.is_connected():
            raise Exception("Database not connected")
        
        try:
            db = self.get_db()
            contacts = db.query(Contact).all()
            result = []
            for contact in contacts:
                result.append({
                    "id": contact.id,
                    "name": contact.name,
                    "email": contact.email,
                    "company": contact.company,
                    "subject": contact.subject,
                    "message": contact.message,
                    "phone": contact.phone,
                    "created_at": contact.created_at,
                    "status": contact.status
                })
            db.close()
            return result
        except SQLAlchemyError as e:
            if 'db' in locals():
                db.close()
            raise Exception(f"Failed to retrieve contacts: {str(e)}")

    async def update_contact_status(self, contact_id: str, status: str) -> Dict[str, Any]:
        if not self.is_connected():
            raise Exception("Database not connected")
        
        try:
            db = self.get_db()
            contact = db.query(Contact).filter(Contact.id == contact_id).first()
            if not contact:
                db.close()
                raise Exception("Contact not found")
            
            contact.status = status
            db.commit()
            
            result = {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "company": contact.company,
                "subject": contact.subject,
                "message": contact.message,
                "phone": contact.phone,
                "created_at": contact.created_at,
                "status": contact.status
            }
            db.close()
            return result
        except SQLAlchemyError as e:
            if 'db' in locals():
                db.rollback()
                db.close()
            raise Exception(f"Failed to update contact: {str(e)}")

    async def get_contact_by_id(self, contact_id: str) -> Dict[str, Any]:
        if not self.is_connected():
            raise Exception("Database not connected")
        
        try:
            db = self.get_db()
            contact = db.query(Contact).filter(Contact.id == contact_id).first()
            if not contact:
                db.close()
                raise Exception("Contact not found")
            
            result = {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "company": contact.company,
                "subject": contact.subject,
                "message": contact.message,
                "phone": contact.phone,
                "created_at": contact.created_at,
                "status": contact.status
            }
            db.close()
            return result
        except SQLAlchemyError as e:
            if 'db' in locals():
                db.close()
            raise Exception(f"Failed to retrieve contact: {str(e)}")

# Global database instance
db = PostgreSQLDatabase()