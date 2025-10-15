import React from 'react';

const Projects = () => {
  // This will eventually come from your backend
  const projects = [
    {
      id: 1,
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
      id: 2,
      title: "Task Management App",
      description: "A collaborative task management application with real-time updates and team collaboration features.",
      technologies: ["React", "FastAPI", "PostgreSQL", "WebSocket"],
      features: [
        "Real-time collaboration",
        "Task assignment & tracking",
        "Team management",
        "Progress analytics",
        "File attachments"
      ],
      github: "https://github.com/yourusername/project2",
      demo: "https://your-demo-link2.com",
      image: "project2.png"
    }
    // Add your actual projects here
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
                {project.id === 1 ? (
                  <img
                    src={project.image}
                    alt={project.title}
                    style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain', borderRadius: '8px' }}
                  />
                ) : (
                  <>🖼️ {project.image}</>
                )}
              </div>
            </div>
            
            <div className="project-content">
              <h3>{project.title}</h3>
              {project.tagline && (
                <div style={{
                  fontSize: '1.1rem',
                  color: '#2563eb',
                  fontWeight: 600,
                  margin: '0.5rem 0 1rem 0',
                  letterSpacing: '0.5px',
                  fontFamily: 'inherit',
                }}>
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