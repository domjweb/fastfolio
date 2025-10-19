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