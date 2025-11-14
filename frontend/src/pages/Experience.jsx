import React from 'react';

const Experience = () => {
  // This will eventually come from your backend
  const experiences = [
    {
      id: 1,
      title: "Full Stack Developer",
      company: "Tegria",
      period: "Aug 2023 - Present",
      description: "Engineer healthcare data solutions and analytics platforms for hospital clients leveraging Meditech and Epic systems. Integrate third-party patient portals solutions, provider dashboards, clinical reporting tools, and API integrations that transform raw healthcare data into actionable insights for care teams and executives.",
      technologies: ["C#", "ASP.NET", ".NET", "Classic ASP", "JavaScript", "TypeScript", "React", "SQL Server", "Azure", "Meditech", "Epic", "REST APIs", "CI/CD"],
      achievements: [
        "Developed provider dashboards and analytics tools that visualize patient outcomes, quality metrics, and operational performance across multi-hospital deployments",
        "Built data integration pipelines connecting Meditech and Epic systems, enabling real-time reporting and clinical decision support for care coordination teams",
        "Engineered patient portal solutions with secure record access, appointment scheduling, and outcome tracking—improving patient engagement and satisfaction scores",
        "Designed RESTful APIs that aggregate clinical data from disparate hospital systems, powering executive dashboards and registry reporting tools",
        "Partnered with healthcare IT teams to deliver HIPAA-compliant solutions that meet interoperability standards while providing actionable intelligence for quality improvement initiatives"
      ]
    },
    {
      id: 2,
      title: "Full Stack Developer",
      company: "CVS",
      period: "Oct 2021 - Aug 2023", 
      description: "Developed healthcare data solutions and analytics platforms that transformed pharmacy operations, clinical workflows, and patient care delivery through automated insights and visual reporting.",
      technologies: ["Java", "Spring", "C#", "ASP.NET", ".NET", "Python", "JavaScript", "TypeScript", "Node.js", "Express", "Azure", "SQL Server", "REST APIs", "Proprietary Systems"],
      achievements: [
        "Built data integration pipelines that aggregated pharmacy metrics, enabling real-time performance dashboards for operational decision-making",
        "Developed automated reporting tools that reduced manual data analysis time by 25%, providing actionable insights for clinical and retail teams",
        "Designed RESTful APIs serving healthcare data to internal dashboards, supporting executive visibility into patient access and pharmacy operations",
        "Contributed to production system stability through proactive monitoring, creating alerting mechanisms that improved incident response times"
      ]
    },
    {
      id: 3,
      title: "Junior Developer",
      company: "Apple",
      period: "Sep 2020 - Oct 2021",
      description: "Worked on Apple's proprietary applications Core and Gather, building new features for the Gather macOS knowledge base app used by customer service teams.",
      technologies: ["Swift", "Objective-C", "Xcode",],
      achievements: [
        "Enhanced application performance and responsiveness, improving internal support workflows",
        "Collaborated cross-functionally with designers and QA to refine user experience",
        "Maintained high code quality standards through peer reviews and documentation"
      ]
    },
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