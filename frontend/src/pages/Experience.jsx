import React from 'react';

const Experience = () => {
  // This will eventually come from your backend
  const experiences = [
    {
      id: 1,
      title: "Full Stack Developer",
      company: "Tegria",
      period: "August 2023 - Present",
      description: "Engineered web applications and patient portal solutions for Tegria’s healthcare clients, including hospitals and medical institutions leveraging Meditech and Epic systems. Delivered end-to-end development for client-facing portals, provider dashboards, and secure API integrations that enhanced patient access and hospital interoperability.",
      technologies: ["C#", "ASP.NET", ".NET", "Classic ASP", "JavaScript", "TypeScript", "React", "SQL Server", "Azure", "Meditech", "Epic", "REST APIs", "CI/CD"],
      achievements: [
        "Developed custom patient portals and web applications enabling patients to securely access records, appointments, and billing information",
        "Integrated hospital systems with Meditech and Epic APIs to synchronize patient data, scheduling, and registration workflows",
        "Built and maintained backend services supporting multi-hospital deployments with high uptime and compliance requirements",
        "Partnered directly with healthcare IT teams to design scalable, compliant solutions that met HIPAA and interoperability standards",
        "Advocated for user-friendly design choices based on client and patient feedback, improving adoption rates across multiple hospital systems"
      ]
    },
    {
      id: 2,
      title: "Full Stack Developer",
      company: "CVS",
      period: "Feb 2023 - Aug 2023", 
      description: "Developed enterprise-grade solutions that enhanced pharmacy operations, patient access, and internal workflow automation for retail and clinical systems.",
      technologies: ["Java", "Spring", "C#", "ASP.NET", ".NET", "Python", "JavaScript", "TypeScript", "Node.js", "Express", "Azure", "SQL Server", "REST APIs", "Proprietary Systems"],
      achievements: [
        "Implemented backend integrations that reduced manual data processing time by 25%",
        "Built workflow automation scripts improving efficiency in pharmacy and clinical support applications",
        "Contributed to the stability of production environments through active debugging, monitoring, and documentation"
      ]
    },
    {
      id: 3,
      title: "Fullstack Developer",
      company: "Kelly Connect",
      period: "Oct 2021 - Feb 2023",
      description: "Developed custom full-stack web applications for KellyConnect’s third-party enterprise clients, delivering scalable recruiting, workforce, and analytics platforms tailored to client needs. Partnered directly with stakeholders to translate business requirements into robust, production-ready solutions used by thousands of employees and applicants.",
      technologies: ["JavaScript", "TypeScript", "React", "Node.js", "Express", "Java", "Spring", "C#", "ASP.NET", ".NET", "PostgreSQL", "AWS", "Lambda", "S3", "API Integrations"],
      achievements: [
        "Built responsive, client-facing web applications that streamlined applicant tracking and onboarding processes",
        "Developed backend services and REST APIs to handle authentication, data management, and performance reporting",
        "Collaborated with cross-functional client teams to design user interfaces and deliver custom workflows for large-scale deployments",
        "Optimized application performance and scalability to support high-volume concurrent users across multiple client environments",
        "Delivered multiple end-to-end solutions on time and within scope, improving client satisfaction and operational efficiency"
      ]
    },
    {
      id: 4,
      title: "Junior Developer",
      company: "Apple",
      period: "Jan 2021 - Oct 2021",
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