# FastFolio - Full Stack Portfolio

A modern, responsive portfolio website built with React and FastAPI, featuring dynamic animations and a clean design.

## 🚀 Live Demo
- **Frontend**: [Coming Soon - Azure App Service]
- **Backend API**: [Coming Soon - Azure App Service]

## 🏗️ Architecture

### Frontend (React + Vite)
- **Framework**: React 19.1.1 with Vite 7.1.7
- **Routing**: React Router DOM
- **Styling**: Custom CSS with animations and glassmorphism effects
- **Features**: 
  - Typewriter animations
  - Scroll-triggered animations
  - Responsive design
  - Scroll-to-top rocket 🚀
  - Dynamic gradient backgrounds

### Backend (FastAPI)
- **Framework**: FastAPI with uvicorn
- **Database**: PostgreSQL (Azure Database)
- **Features**:
  - CORS middleware
  - Pydantic models
  - RESTful API endpoints
  - Contact form handling

## 📂 Project Structure
```
fastfolio/
├── frontend/              # React application
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom hooks
│   │   └── assets/        # Images and static files
│   └── public/           # Public assets
├── backend/              # FastAPI application
│   ├── main.py          # FastAPI app and routes
│   ├── database.py      # Database configuration
│   └── requirements.txt # Python dependencies
└── .github/workflows/   # CI/CD pipelines
```

## 🛠️ Local Development

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🚀 Deployment

This project uses GitHub Actions for CI/CD deployment to Azure:
- **Frontend**: Azure App Service (Static Web App)
- **Backend**: Azure App Service (Python)
- **Database**: Azure Database for PostgreSQL

## 🎨 Features

- **Professional Design**: Clean, modern interface with subtle animations
- **Responsive Layout**: Mobile-first design that works on all devices
- **Performance Optimized**: Fast loading with efficient animations
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Accessibility**: Screen reader friendly with proper ARIA labels

## 🔧 Tech Stack

**Frontend:**
- React 19.1.1
- Vite 7.1.7
- React Router DOM 7.9.3
- Custom CSS with animations

**Backend:**
- FastAPI
- uvicorn
- Pydantic
- PostgreSQL

**Deployment:**
- Azure App Service
- GitHub Actions
- Azure Database for PostgreSQL

## 📧 Contact

**Dominique Webb** - Full Stack Developer
- Portfolio: domjweb.com
- Email:  dominiqueweb@domjweb.com
- LinkedIn: linkedin.com/domjweb
- GitHub: github.com/domjweb

---

