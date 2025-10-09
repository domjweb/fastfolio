import os
from dotenv import load_dotenv
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from azure.cosmos import CosmosClient, exceptions
from datetime import datetime

load_dotenv()
# Read CosmosDB connection string from environment
COSMOS_CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
DATABASE_ID = "domjweb"
CONTAINER_ID = "contacts"

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
        container.create_item(body=item)
        return {"status": "success", "message": "Contact submitted."}
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=f"CosmosDB error: {e.message}")
