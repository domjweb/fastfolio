import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
import os
from database import db

# Import portfolio models and data
from models import (
    Experience, ExperiencesResponse,
    Project, ProjectsResponse, 
    SkillCategory, SkillsResponse,
    AboutInfo, AboutResponse
)
from portfolio_data import portfolio_data

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
    "https://domjweb.com",  # Production domain
    "https://www.domjweb.com",  # Production domain with www
    "https://ashy-sea-0e6938f0f.2.azurestaticapps.net"  # Current Azure Static Web App URL
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

# Portfolio Endpoints
@app.get("/about", response_model=AboutResponse)
async def get_about():
    """Get personal/about information"""
    return AboutResponse(about=portfolio_data["about"])

@app.get("/experiences", response_model=ExperiencesResponse)
async def get_experiences():
    """Get professional experience data"""
    return ExperiencesResponse(experiences=portfolio_data["experiences"])

@app.get("/projects", response_model=ProjectsResponse) 
async def get_projects():
    """Get portfolio projects data"""
    return ProjectsResponse(projects=portfolio_data["projects"])

@app.get("/skills", response_model=SkillsResponse)
async def get_skills():
    """Get technical skills data"""
    return SkillsResponse(skill_categories=portfolio_data["skills"])

# Health and info endpoints
@app.get("/api/info")
async def api_info():
    """Get API information and available endpoints"""
    return {
        "name": "FastFolio Portfolio API",
        "version": "1.0.0",
        "description": "Backend API for Dominique Webb's portfolio website",
        "endpoints": {
            "GET /": "API status",
            "GET /health": "Health check", 
            "GET /about": "Personal information",
            "GET /experiences": "Professional experience",
            "GET /projects": "Portfolio projects",
            "GET /skills": "Technical skills",
            "POST /contact": "Submit contact form",
            "GET /contacts": "Get all contacts (admin)",
            "PATCH /contacts/{id}/status": "Update contact status (admin)"
        },
        "documentation": "/docs"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

