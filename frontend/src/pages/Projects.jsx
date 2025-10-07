import React from 'react';

const Projects = () => {
  // This will eventually come from your backend
  const projects = [
    {
      id: 1,
      title: "E-Commerce Platform",
      description: "A full-stack e-commerce solution with user authentication, payment processing, and admin dashboard.",
      technologies: ["React", "Node.js", "Express", "MongoDB", "Stripe"],
      features: [
        "User authentication & authorization",
        "Product catalog management",
        "Shopping cart & checkout",
        "Payment processing",
        "Order tracking"
      ],
      github: "https://github.com/yourusername/project1",
      demo: "https://your-demo-link.com",
      image: "project1.png"
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
                🖼️ {project.image}
              </div>
            </div>
            
            <div className="project-content">
              <h3>{project.title}</h3>
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