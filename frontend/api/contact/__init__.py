import azure.functions as func
import json
import logging
from models import ContactRequest

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
            
            # In production, you would:
            # 1. Send email notification
            # 2. Store in database
            # 3. Send confirmation email to user
            
            # For now, just log the contact request
            logging.info(f"Contact form submission: {contact_request.dict()}")
            
            # Simulate processing
            response_data = {
                "message": "Thank you for your message! I'll get back to you soon.",
                "contact_id": f"contact_{contact_request.name.lower().replace(' ', '_')}_123",
                "status": "received"
            }
            
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