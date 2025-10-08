from models import AboutInfo, Experience, Project, SkillCategory, Skill

# Sample about information
about_info = AboutInfo(
    name="Dominic Webb",
    title="Full-Stack Developer & Cloud Solutions Architect",
    summary="Passionate developer with expertise in modern web technologies and cloud platforms. Experienced in building scalable applications using React, Python, and Azure services. Always eager to learn new technologies and solve complex problems.",
    location="United Kingdom",
    email="dominic@domjweb.com",
    linkedin="https://linkedin.com/in/domjweb",
    github="https://github.com/domjweb"
)

# Sample professional experiences
experiences = [
    Experience(
        title="Senior Full-Stack Developer",
        company="Tech Solutions Ltd",
        location="London, UK",
        start_date="2022-01",
        end_date=None,
        description=[
            "Led development of microservices architecture using FastAPI and Azure Functions",
            "Built responsive React applications with modern hooks and state management",
            "Implemented CI/CD pipelines using GitHub Actions and Azure DevOps",
            "Mentored junior developers and conducted code reviews",
            "Reduced deployment time by 60% through automation and containerization"
        ],
        technologies=["React", "Python", "FastAPI", "Azure", "Docker", "PostgreSQL"]
    ),
    Experience(
        title="Cloud Developer",
        company="Digital Innovations Inc",
        location="Manchester, UK", 
        start_date="2020-06",
        end_date="2021-12",
        description=[
            "Developed serverless applications using Azure Functions and Cosmos DB",
            "Created REST APIs with comprehensive documentation using OpenAPI",
            "Implemented authentication and authorization using Azure AD",
            "Optimized application performance resulting in 40% faster load times",
            "Collaborated with cross-functional teams using Agile methodologies"
        ],
        technologies=["Python", "Azure Functions", "Cosmos DB", "React", "TypeScript"]
    ),
    Experience(
        title="Junior Web Developer",
        company="Creative Web Studio",
        location="Birmingham, UK",
        start_date="2019-03",
        end_date="2020-05", 
        description=[
            "Built custom WordPress themes and plugins for client websites",
            "Developed interactive frontend components using vanilla JavaScript",
            "Collaborated with designers to implement pixel-perfect UIs",
            "Maintained and updated existing web applications",
            "Provided technical support and training to clients"
        ],
        technologies=["JavaScript", "PHP", "WordPress", "HTML5", "CSS3", "MySQL"]
    )
]

# Sample projects
projects = [
    Project(
        name="Portfolio Website",
        description="Modern portfolio website built with React and Azure Static Web Apps, featuring serverless API backend and custom domain integration.",
        technologies=["React", "Azure Static Web Apps", "Azure Functions", "Python", "Vite"],
        github_url="https://github.com/domjweb/fastfolio",
        live_url="https://domjweb.com",
        image_url="/images/portfolio-project.jpg"
    ),
    Project(
        name="Task Management API",
        description="RESTful API for task management with user authentication, real-time updates, and comprehensive test coverage.",
        technologies=["FastAPI", "PostgreSQL", "Redis", "Docker", "Pytest"],
        github_url="https://github.com/domjweb/task-api",
        live_url=None,
        image_url="/images/task-api-project.jpg"
    ),
    Project(
        name="E-commerce Dashboard",
        description="Analytics dashboard for e-commerce platforms with real-time sales tracking, inventory management, and customer insights.",
        technologies=["React", "TypeScript", "Chart.js", "Node.js", "MongoDB"],
        github_url="https://github.com/domjweb/ecommerce-dashboard",
        live_url="https://dashboard-demo.domjweb.com",
        image_url="/images/dashboard-project.jpg"
    )
]

# Sample skill categories
skill_categories = [
    SkillCategory(
        category="Frontend Development",
        skills=[
            Skill(name="React", proficiency=5),
            Skill(name="TypeScript", proficiency=4),
            Skill(name="JavaScript", proficiency=5),
            Skill(name="HTML5", proficiency=5),
            Skill(name="CSS3", proficiency=4),
            Skill(name="Vite", proficiency=4),
            Skill(name="Tailwind CSS", proficiency=3)
        ]
    ),
    SkillCategory(
        category="Backend Development", 
        skills=[
            Skill(name="Python", proficiency=5),
            Skill(name="FastAPI", proficiency=5),
            Skill(name="Node.js", proficiency=3),
            Skill(name="REST APIs", proficiency=5),
            Skill(name="GraphQL", proficiency=3),
            Skill(name="WebSocket", proficiency=3)
        ]
    ),
    SkillCategory(
        category="Cloud & DevOps",
        skills=[
            Skill(name="Azure", proficiency=4),
            Skill(name="Azure Functions", proficiency=4),
            Skill(name="Azure Static Web Apps", proficiency=4),
            Skill(name="Docker", proficiency=3),
            Skill(name="GitHub Actions", proficiency=4),
            Skill(name="Azure DevOps", proficiency=3)
        ]
    ),
    SkillCategory(
        category="Databases",
        skills=[
            Skill(name="PostgreSQL", proficiency=4),
            Skill(name="Azure SQL Database", proficiency=3),
            Skill(name="Cosmos DB", proficiency=3),
            Skill(name="Redis", proficiency=3),
            Skill(name="MongoDB", proficiency=2)
        ]
    ),
    SkillCategory(
        category="Tools & Others",
        skills=[
            Skill(name="Git", proficiency=5),
            Skill(name="VS Code", proficiency=5),
            Skill(name="Postman", proficiency=4),
            Skill(name="Pytest", proficiency=4),
            Skill(name="Jest", proficiency=3),
            Skill(name="Linux", proficiency=3)
        ]
    )
]