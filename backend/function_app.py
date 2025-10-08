import azure.functions as func
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your existing FastAPI app
from main import app

# Create Azure Functions app
app_func = func.FunctionApp()

# Configure CORS for production
origins = [
    "https://domjweb.com",
    "https://www.domjweb.com", 
    "https://ashy-sea-0e6938f0f.2.azurestaticapps.net",
    "http://localhost:5173",  # For local development
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app_func.route(route="api/{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function HTTP trigger that forwards requests to FastAPI"""
    
    logging.info(f'HTTP trigger function processed a request: {req.method} {req.url}')
    
    # Import ASGI handler
    from azure.functions import AsgiMiddleware
    
    return await AsgiMiddleware(app).handle_async(req)