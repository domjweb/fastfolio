
import azure.functions as func
import json
import logging
import sys
import os
import uuid
from datetime import datetime
from models import ContactRequest
from azure.cosmos import CosmosClient, exceptions

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Contact endpoint processed a request.')
    
    # Handle OPTIONS requests for CORS preflight
    if req.method == "OPTIONS":
        return func.HttpResponse(
            "",
            status_code=200,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            }
        )
    
    if req.method == "GET":
        # Return contact information or form schema
        contact_info = {
            "email": "dominic@domjweb.com",
            "linkedin": "https://linkedin.com/in/domjweb",
            "github": "https://github.com/domjweb",
            "form_fields": [
                {"name": "name", "type": "text", "required": True},
                {"name": "email", "type": "email", "required": True},
                {"name": "subject", "type": "text", "required": True},
                {"name": "message", "type": "textarea", "required": True}
            ]
        }
        
        return func.HttpResponse(
            json.dumps(contact_info),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        )
    
    elif req.method == "POST":
        try:
            # Parse and validate request body
            req_body = req.get_json()
            if not req_body:
                return func.HttpResponse(
                    json.dumps({"error": "Request body is required"}),
                    status_code=400,
                    headers={
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    }
                )
            
            # Validate using Pydantic model
            contact_request = ContactRequest(**req_body)
            
            # Try to save to database
            try:
                # Prepare contact data
                contact_data = {
                    "id": str(uuid.uuid4()),
                    "name": contact_request.name,
                    "email": contact_request.email,
                    "subject": contact_request.subject,
                    "message": contact_request.message,
                    "company": req_body.get("company"),  # Optional field
                    "phone": req_body.get("phone"),       # Optional field
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                }

                # Cosmos DB connection
                COSMOS_CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
                DATABASE_ID = "domjweb"
                CONTAINER_ID = "contacts"
                if not COSMOS_CONNECTION_STRING:
                    raise Exception("COSMOS_CONNECTION_STRING environment variable not set.")
                client = CosmosClient.from_connection_string(COSMOS_CONNECTION_STRING)
                database = client.get_database_client(DATABASE_ID)
                container = database.get_container_client(CONTAINER_ID)

                # Write to Cosmos DB
                logging.info(f"Attempting to write item to Cosmos DB: {contact_data}")
                response = container.create_item(body=contact_data)
                logging.info(f"Successfully wrote item to Cosmos DB. Response: {response}")

                # Generate response
                response_data = {
                    "message": "Thank you for your message! I'll get back to you soon.",
                    "contact_id": contact_data["id"],
                    "status": "received"
                }

            except Exception as db_error:
                logging.error(f"Cosmos DB error: {str(db_error)}")
                # Fallback response if database fails
                response_data = {
                    "message": "Thank you for your message! I'll get back to you soon.",
                    "contact_id": f"fallback_{contact_request.name.lower().replace(' ', '_')}",
                    "status": "received"
                }
                # Still log the contact for manual processing
                logging.info(f"Contact form submission (no DB): {contact_request.dict()}")
            
            return func.HttpResponse(
                json.dumps(response_data),
                status_code=200,
                headers={
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            )
            
        except ValueError as e:
            logging.error(f"Validation error in contact endpoint: {str(e)}")
            return func.HttpResponse(
                json.dumps({"error": "Invalid request data", "details": str(e)}),
                status_code=400,
                headers={
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            )
        except Exception as e:
            logging.error(f"Error in contact endpoint: {str(e)}")
            return func.HttpResponse(
                json.dumps({"error": "Internal server error"}),
                status_code=500,
                headers={
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            )
    
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed"}),
            status_code=405,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        )