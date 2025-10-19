import React from 'react';

const Skills = () => {
  const skillCategories = [
    {
      category: "Frontend Development",
      skills: [
        { name: "React", level: 90, years: 4 },
        { name: "JavaScript/TypeScript", level: 90, years: 4 },
        { name: "HTML/CSS", level: 95, years: 5 },
        { name: "Vite", level: 90, years: 4 },
        { name: "Tailwind CSS", level: 80, years: 3 }
      ]
    },
    {
      category: "Backend Development", 
      skills: [
        { name: "Python", level: 95, years: 4 },
        { name: "FastAPI", level: 90, years: 3 },
        { name: "Node.js", level: 85, years: 3 },
        { name: "Express.js", level: 80, years: 3 },
        { name: "RESTful APIs", level: 85, years: 4 }
      ]
    },
    {
      category: "Database & Cloud",
      skills: [
        { name: "PostgreSQL", level: 80, years: 3 },
        { name: "Azure Cosmos", level: 90, years: 3 },
        { name: "Azure", level: 85, years: 3 },
        { name: "Docker", level: 80, years: 3 },
        { name: "Git/GitHub", level: 90, years: 4 }
      ]
    },
    {
      category: "Tools & Methods",
      skills: [
        { name: "Agile/Scrum", level: 80, years: 3 },
        { name: "CI/CD", level: 85, years: 3 },
        { name: "Testing (Jest, Pytest)", level: 80, years: 2 },
        { name: "VS Code", level: 95, years: 4 },
        { name: "Temporal", level: 80, years: 2 }
      ]
    }
  ];

  const getSkillColor = (level) => {
    if (level >= 85) return "#22c55e"; // Green
    if (level >= 70) return "#3b82f6"; // Blue  
    if (level >= 50) return "#f59e0b"; // Orange
    return "#ef4444"; // Red
  };

  return (
    <div className="skills-page">
      <div className="page-header">
        <h1>Skills & Technologies</h1>
        <p>My technical expertise and proficiency levels</p>
      </div>
      
      <div className="skills-grid">
        {skillCategories.map((category, categoryIdx) => (
          <div key={categoryIdx} className="skill-category">
            <h3 className="category-title">{category.category}</h3>
            <div className="skills-list">
              {category.skills.map((skill, skillIdx) => (
                <div key={skillIdx} className="skill-item">
                  <div className="skill-header">
                    <span className="skill-name">{skill.name}</span>
                    <span className="skill-experience">{skill.years} years</span>
                  </div>
                  <div className="skill-bar-container">
                    <div 
                      className="skill-bar"
                      style={{ 
                        width: `${skill.level}%`,
                        backgroundColor: getSkillColor(skill.level)
                      }}
                    ></div>
                    <span className="skill-percentage">{skill.level}%</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      
      <div className="certifications-section">
        <h3>Certifications & Learning</h3>
        <div className="certifications-grid">
          <div className="cert-card">
            <h4>🎓 AWS Certified Developer</h4>
            <p>Amazon Web Services</p>
            <span className="cert-date">2023</span>
          </div>
          <div className="cert-card">
            <h4>📜 React Professional</h4>
            <p>Meta/Facebook</p>
            <span className="cert-date">2022</span>
          </div>
          <div className="cert-card">
            <h4>🏆 Python Advanced</h4>
            <p>Python Institute</p>
            <span className="cert-date">2022</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Skills;