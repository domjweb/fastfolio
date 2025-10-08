import azure.functions as func
import json
import logging
from portfolio_data import experiences

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Experiences endpoint processed a request.')
    
    try:
        # Convert Pydantic models to dicts for JSON serialization
        experiences_data = [exp.dict() for exp in experiences]
        
        return func.HttpResponse(
            json.dumps({"experiences": experiences_data}),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "*"
            }
        )
    except Exception as e:
        logging.error(f"Error in experiences endpoint: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            headers={"Content-Type": "application/json"}
        )