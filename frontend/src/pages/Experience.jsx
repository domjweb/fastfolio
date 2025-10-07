import React from 'react';

const Experience = () => {
  // This will eventually come from your backend
  const experiences = [
    {
      id: 1,
      title: "Senior Software Engineer",
      company: "Tech Company Inc.",
      period: "2023 - Present",
      description: "Led development of scalable web applications using React, Node.js, and cloud technologies.",
      technologies: ["React", "Node.js", "AWS", "PostgreSQL"],
      achievements: [
        "Increased application performance by 40%",
        "Led team of 4 developers",
        "Implemented CI/CD pipelines"
      ]
    },
    {
      id: 2,
      title: "Full Stack Developer",
      company: "Startup Solutions",
      period: "2021 - 2023", 
      description: "Built end-to-end web applications and APIs for various client projects.",
      technologies: ["Python", "FastAPI", "React", "MongoDB"],
      achievements: [
        "Delivered 15+ client projects",
        "Reduced deployment time by 60%",
        "Mentored junior developers"
      ]
    }
    // Add your actual experiences here
  ];

  return (
    <div className="experience-page">
      <div className="page-header">
        <h1>Professional Experience</h1>
        <p>My journey in software development and key accomplishments</p>
      </div>
      
      <div className="timeline">
        {experiences.map((exp, index) => (
          <div key={exp.id} className="experience-card">
            <div className="timeline-marker"></div>
            <div className="experience-content">
              <div className="experience-header">
                <h3>{exp.title}</h3>
                <div className="company-info">
                  <span className="company">{exp.company}</span>
                  <span className="period">{exp.period}</span>
                </div>
              </div>
              
              <p className="description">{exp.description}</p>
              
              <div className="technologies">
                <h4>Technologies Used:</h4>
                <div className="tech-tags">
                  {exp.technologies.map((tech, idx) => (
                    <span key={idx} className="tech-tag">{tech}</span>
                  ))}
                </div>
              </div>
              
              <div className="achievements">
                <h4>Key Achievements:</h4>
                <ul>
                  {exp.achievements.map((achievement, idx) => (
                    <li key={idx}>{achievement}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Experience;