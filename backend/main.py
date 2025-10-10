
import os
import logging
from dotenv import load_dotenv
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from azure.cosmos import CosmosClient, exceptions
from datetime import datetime

# Import portfolio models and data
from models import (
    Experience, ExperiencesResponse,
    Project, ProjectsResponse, 
    SkillCategory, SkillsResponse,
    AboutInfo, AboutResponse
)
from portfolio_data import portfolio_data


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str



# Setup logging
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Read CosmosDB connection string from environment
COSMOS_CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
DATABASE_ID = "domjweb"
CONTAINER_ID = "contacts"
logging.info(f"Using Cosmos DB connection string: {COSMOS_CONNECTION_STRING[:50]}... (truncated)")
logging.info(f"Database: {DATABASE_ID}, Container: {CONTAINER_ID}")

# Initialize Cosmos client
client = CosmosClient.from_connection_string(COSMOS_CONNECTION_STRING)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

app = FastAPI()



# Allow CORS for local frontend and production (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://localhost:4173",
        "https://domjweb.com",
        "https://www.domjweb.com",
        "https://ashy-sea-0e6938f0f.2.azurestaticapps.net"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Portfolio API is running!", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/contact")
def submit_contact(form: ContactForm):
    try:
        item = {
            "id": str(uuid.uuid4()),
            "name": form.name,
            "email": form.email,
            "message": form.message,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        logging.info(f"Attempting to write item to Cosmos DB: {item}")
        response = container.create_item(body=item)
        logging.info(f"Successfully wrote item to Cosmos DB. Response: {response}")
        return {"status": "success", "message": "Contact submitted."}
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"CosmosDB error: {e.message}")
        raise HTTPException(status_code=500, detail=f"CosmosDB error: {e.message}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


# (Optional) You can add Cosmos DB-based endpoints for listing/updating contacts if needed


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
            "POST /contact": "Submit contact form"
        },
        "documentation": "/docs"
    }



