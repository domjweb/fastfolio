import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
import os
from database import db

class ContactRequest(BaseModel):
    name: str
    email: str
    company: Optional[str] = None  # Optional field
    subject: str
    message: str
    phone: Optional[str] = None  # Optional field

class ContactResponse(BaseModel):
    id: str
    name: str
    email: str
    company: Optional[str] = None
    subject: str
    message: str
    phone: Optional[str] = None
    created_at: str
    status: str = "new"  # new, read, responded

class ContactsResponse(BaseModel):
    contacts: List[ContactResponse]


app = FastAPI()


origins = [
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:5173",  # Alternative localhost
    "http://localhost:3000",  # Create React App (if used)
    "http://localhost:4173",  # Vite preview
    "https://your-portfolio-domain.com"  # Production domain (update when deployed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

memory_db = {"contacts": []}

@app.get("/")
def home():
    return {"message": "Portfolio API is running!", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/contact", response_model=ContactResponse)
async def submit_contact(contact: ContactRequest):
    """Submit a new contact form from recruiters/visitors"""
    contact_id = str(uuid.uuid4())
    contact_data = {
        "id": contact_id,
        "name": contact.name,
        "email": contact.email,
        "company": contact.company,
        "subject": contact.subject,
        "message": contact.message,
        "phone": contact.phone,
        "created_at": datetime.now().isoformat(),
        "status": "new"
    }
    
    try:
        if db.is_connected():
            await db.create_contact(contact_data)
        else:
            # Fallback to memory storage
            memory_db["contacts"].append(contact_data)
        
        return ContactResponse(**contact_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save contact: {str(e)}")

@app.get("/contacts", response_model=ContactsResponse)
async def get_contacts():
    """Get all contacts - for admin use"""
    try:
        if db.is_connected():
            contacts = await db.get_all_contacts()
        else:
            contacts = memory_db["contacts"]
        
        return ContactsResponse(contacts=contacts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve contacts: {str(e)}")

@app.patch("/contacts/{contact_id}/status")
async def update_contact_status(contact_id: str, status: str):
    """Update contact status - for admin use"""
    try:
        if db.is_connected():
            await db.update_contact_status(contact_id, status)
        else:
            # Fallback to memory storage
            for contact in memory_db["contacts"]:
                if contact["id"] == contact_id:
                    contact["status"] = status
                    return {"message": "Status updated successfully"}
            raise HTTPException(status_code=404, detail="Contact not found")
        
        return {"message": "Status updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update contact: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

