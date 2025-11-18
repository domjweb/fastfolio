import React from 'react';

const Projects = () => {
  const resolveImage = (img) => {
    if (!img) return null;
    // if absolute URL or protocol-relative, return as-is
    if (/^(https?:)?\/\//.test(img)) return img;
    // if already starts with slash, assume public path
    if (img.startsWith('/')) return img;
    // convert ./image.png -> /image.png (public)
    if (img.startsWith('./')) return img.replace(/^\.\//, '/');
    // otherwise prefix with /
    return `/${img}`;
  };
  const projects = [
    {
      id: 1,
      title: "Trauma Revenue Insights Mini-Registry",
      description: "Full-stack healthcare analytics platform combining clinical trauma registry data with revenue cycle management. Built with NQS-inspired dashboards featuring Performance Improvement metrics, Revenue Analysis, and Data Quality tracking. Identifies $5M+ in annual lost charges through intelligent flagging and prioritization of high-value opportunities for Trauma Program Managers and RCM teams.",
      technologies: ["Django", "React", "TypeScript", "Azure Container Apps", "Terraform", "Docker", "GitHub Actions", "REST API", "Vite"],
      features: [
        "Four-tab analytics dashboard: Overview, Performance Improvement, Revenue Analysis, and Data Quality",
        "Automated revenue capture rate calculation identifying cases with >$10k uncaptured charges",
        "Real-time complication risk analysis based on ISS severity and resource utilization patterns",
        "CI/CD pipeline with GitHub Actions deploying containerized microservices to Azure",
        "Business logic layer calculating expected charges, data completeness scores, and quality flags",
        "Responsive UI with interactive visualizations, severity distributions, and timeline charts"
      ],
      github: "https://github.com/domjweb/TraumaReg",
      demo: "https://traumareg-frontend.greenground-19fbcf12.eastus.azurecontainerapps.io",
      image: "/traumaRegBanner.png",
      tagline: "Proactive analytics for trauma programs—find lost revenue before it's too late!"

    },
    {
      id: 2,
      title: "Healthcare Claims Processing System",
      description: "Enterprise-grade healthcare claims validation and processing system built with FastAPI and React. Processes EDI 837 (837I Institutional and 837P Professional) claim files, validates against HIPAA standards, performs automated adjudication, and generates 835 remittance advice. Deployed on Azure Container Apps with PostgreSQL database, featuring real-time claim tracking and status management.",
      technologies: ["Python", "FastAPI", "React", "PostgreSQL", "Docker", "Azure Container Apps", "Terraform", "SQLAlchemy", "Alembic", "X12 EDI"],
      features: [
        "HIPAA-compliant EDI 837 file parsing (Institutional & Professional)",
        "Automated claim validation and adjudication engine",
        "835 remittance advice generation",
        "Real-time claim status tracking and management",
        "RESTful API with auto-generated OpenAPI documentation",
        "Containerized microservices architecture",
        "Infrastructure as Code with Terraform",
        "PostgreSQL database with migrations"
      ],
      github: "https://github.com/domjweb/FastVal",
      demo: "https://fastval-dev-frontend.ambitiousdune-c30d7366.eastus2.azurecontainerapps.io",
      image: "/fastvalBanner.png",
      tagline: "Streamlining Healthcare Claims Processing with Modern Cloud Architecture"
    },
    {
      id: 3,
      title: "Interactive Story Generator",
      description: "Story Generator is a web app that lets users instantly create and explore interactive, AI-generated adventure stories based on their chosen themes.",
      technologies: ["JavaScript", "Python", "React", "Node.js", "FastAPI", "Cosmos DB", "SWA", "Azure Managed Functions"],
      features: [
        "Interactive, AI-generated adventure stories based on user-chosen themes",
        "Asynchronous story generation with real-time job status updates",
        "Persistent story and job storage using Azure Cosmos DB",
        "Seamless frontend/backend integration with live polling and instant feedback",
        "User-friendly interface for entering themes and exploring stories",
        "Dynamic story navigation with branching choices and multiple endings",
        "Custom favicon and branding support",
        "Scalable, serverless deployment using Azure Static Web Apps and Azure Functions",
        "Secure, anonymous user sessions for story creation and exploration",
        "Responsive design for desktop and mobile devices"
      ],
      github: "https://github.com/domjweb/FastAdventure",
      demo: "https://kind-desert-0cf58b00f.1.azurestaticapps.net/",
      image: "/isgBanner.png",
      tagline: "Create, explore, and share AI-powered adventures with a single click!"
    },
    {
      id: 4,
      title: "Task Management App",
      description: "a collaborative request and workflow management app built with React, FastAPI, Temporal, and PostgreSQL. It enables teams to efficiently submit, track, and resolve requests with real-time collaboration, assignment, team management, and progress analytics.",
      technologies: ["React", "FastAPI", "Cosmos DB", "PostgreSQL", "Temporal"],
      features: [
        "Request submission and tracking",
        "Real-time collaboration on requests",
        "Request assignment to team members",
        "Team management and user roles",
        "Status updates and workflow automation",
        "Progress analytics and reporting",
        "Audit trail of request events",
        "Integration with Temporal for workflow orchestration",
        "Modern UI built with React",
        "Backend API with FastAPI",
        "Persistent data storage with PostgreSQL"
      ],
      github: "https://github.com/domjweb/FastOrchestration",
      demo: "https://happy-smoke-0e8381a0f.1.azurestaticapps.net/",
      image: "./Fastorcbanner.png",
    }
  ];

  return (
    <div className="projects-page">
      <div className="page-header">
        <h1>Featured Projects</h1>
        <p>A showcase of my recent work and technical capabilities</p>
      </div>
      
      <div className="projects-grid">
        {projects.map((project) => (
          <div key={project.id} className="project-card">
            <div className="project-image">
              <div className="image-placeholder">
                {project.image ? (
                  <img
                    src={resolveImage(project.image)}
                    alt={project.title}
                    className="project-image-img"
                  />
                ) : (
                  <>🖼️ No image</>
                )}
              </div>
            </div>
            
            <div className="project-content">
              <h3>{project.title}</h3>
              {project.tagline && (
                <div className="project-tagline">
                  {project.tagline}
                </div>
              )}
              <p className="project-description">{project.description}</p>
              
              <div className="project-tech">
                <h4>Technologies:</h4>
                <div className="tech-tags">
                  {project.technologies.map((tech, idx) => (
                    <span key={idx} className="tech-tag">{tech}</span>
                  ))}
                </div>
              </div>
              
              <div className="project-features">
                <h4>Key Features:</h4>
                <ul>
                  {project.features.map((feature, idx) => (
                    <li key={idx}>{feature}</li>
                  ))}
                </ul>
              </div>
              
              <div className="project-links">
                <a href={project.github} target="_blank" rel="noopener noreferrer" className="btn btn-secondary">
                  📁 View Code
                </a>
                <a href={project.demo} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
                  🚀 Live Demo
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Projects;