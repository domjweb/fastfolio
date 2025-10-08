import azure.functions as func
import json
import logging
from portfolio_data import skill_categories

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Skills endpoint processed a request.')
    
    try:
        # Convert Pydantic models to dicts for JSON serialization
        skills_data = [category.dict() for category in skill_categories]
        
        return func.HttpResponse(
            json.dumps({"skills": skills_data}),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS", 
                "Access-Control-Allow-Headers": "*"
            }
        )
    except Exception as e:
        logging.error(f"Error in skills endpoint: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            headers={"Content-Type": "application/json"}
        )