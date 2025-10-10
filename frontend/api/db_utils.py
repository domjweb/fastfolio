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
    # File intentionally left blank: PostgreSQL logic fully removed for Cosmos DB-only deployment
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