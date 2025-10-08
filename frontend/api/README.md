# Portfolio API - Azure Static Web Apps Managed Functions

This directory contains Azure Functions that power the backend API for the portfolio website.

## API Endpoints

### GET /api/about
Returns personal information and summary.

**Response:**
```json
{
  "name": "Dominic Webb",
  "title": "Full-Stack Developer & Cloud Solutions Architect",
  "summary": "...",
  "location": "United Kingdom",
  "email": "dominic@domjweb.com",
  "linkedin": "https://linkedin.com/in/domjweb",
  "github": "https://github.com/domjweb"
}
```

### GET /api/experiences
Returns professional experience data.

**Response:**
```json
{
  "experiences": [
    {
      "title": "Senior Full-Stack Developer",
      "company": "Tech Solutions Ltd",
      "location": "London, UK",
      "start_date": "2022-01",
      "end_date": null,
      "description": ["..."],
      "technologies": ["React", "Python", "FastAPI", "Azure", "Docker", "PostgreSQL"]
    }
  ]
}
```

### GET /api/projects
Returns portfolio projects.

**Response:**
```json
{
  "projects": [
    {
      "name": "Portfolio Website",
      "description": "...",
      "technologies": ["React", "Azure Static Web Apps", "Azure Functions", "Python", "Vite"],
      "github_url": "https://github.com/domjweb/fastfolio",
      "live_url": "https://domjweb.com",
      "image_url": "/images/portfolio-project.jpg"
    }
  ]
}
```

### GET /api/skills
Returns technical skills organized by category.

**Response:**
```json
{
  "skills": [
    {
      "category": "Frontend Development",
      "skills": [
        {"name": "React", "proficiency": 5},
        {"name": "TypeScript", "proficiency": 4}
      ]
    }
  ]
}
```

### GET /api/contact
Returns contact form configuration.

**Response:**
```json
{
  "email": "dominic@domjweb.com",
  "linkedin": "https://linkedin.com/in/domjweb",
  "github": "https://github.com/domjweb",
  "form_fields": [
    {"name": "name", "type": "text", "required": true},
    {"name": "email", "type": "email", "required": true},
    {"name": "subject", "type": "text", "required": true},
    {"name": "message", "type": "textarea", "required": true}
  ]
}
```

### POST /api/contact
Submits a contact form message.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Inquiry about services",
  "message": "Hello, I'm interested in your services..."
}
```

**Response:**
```json
{
  "message": "Thank you for your message! I'll get back to you soon.",
  "contact_id": "contact_john_doe_123",
  "status": "received"
}
```

## Local Development

For local development with Azure Functions Core Tools:

```bash
# Install Azure Functions Core Tools
npm install -g azure-functions-core-tools@4 --unsafe-perm true

# Navigate to the API directory
cd api

# Install Python dependencies
pip install -r requirements.txt

# Start the local functions runtime
func start
```

The API will be available at `http://localhost:7071/api/`

## Deployment

This API is automatically deployed when the repository is pushed to GitHub, thanks to Azure Static Web Apps GitHub integration. The functions will be available at:

- Production: `https://domjweb.com/api/`
- Staging: `https://[generated-url].2.azurestaticapps.net/api/`

## File Structure

```
api/
├── about/
│   ├── __init__.py       # About endpoint function
│   └── function.json     # Function binding configuration
├── contact/
│   ├── __init__.py       # Contact endpoint function
│   └── function.json     # Function binding configuration
├── experiences/
│   ├── __init__.py       # Experiences endpoint function
│   └── function.json     # Function binding configuration
├── projects/
│   ├── __init__.py       # Projects endpoint function
│   └── function.json     # Function binding configuration
├── skills/
│   ├── __init__.py       # Skills endpoint function
│   └── function.json     # Function binding configuration
├── host.json             # Azure Functions host configuration
├── models.py             # Pydantic data models
├── portfolio_data.py     # Sample portfolio data
└── requirements.txt      # Python dependencies
```

## Configuration

### CORS
CORS is configured to allow all origins for development. In production, consider restricting to your domain:

```json
{
  "cors": {
    "allowedOrigins": ["https://domjweb.com"],
    "allowedMethods": ["GET", "POST", "OPTIONS"],
    "allowedHeaders": ["Content-Type", "Authorization"]
  }
}
```

### Function Authorization
All functions are currently set to `authLevel: "anonymous"` for easy access. Consider implementing authentication for sensitive operations.

## Data Models

The API uses Pydantic for data validation and serialization. All models are defined in `models.py` and sample data is in `portfolio_data.py`.

## Error Handling

All endpoints include comprehensive error handling with appropriate HTTP status codes and JSON error responses.