import azure.functions as func
import json
import logging
from portfolio_data import about_info

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('About endpoint processed a request.')
    
    try:
        return func.HttpResponse(
            json.dumps(about_info.dict()),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "*"
            }
        )
    except Exception as e:
        logging.error(f"Error in about endpoint: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            headers={"Content-Type": "application/json"}
        )