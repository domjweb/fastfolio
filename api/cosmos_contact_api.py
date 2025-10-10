import os
import logging
from dotenv import load_dotenv
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from azure.cosmos import CosmosClient, exceptions
from datetime import datetime

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

# Allow CORS for local frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

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
