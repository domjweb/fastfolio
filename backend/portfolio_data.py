# Portfolio Data Storage - In-memory for now, will migrate to database later
from models import Experience, Project, SkillCategory, Skill, AboutInfo

# Sample portfolio data - replace with your actual information
portfolio_data = {
    "about": AboutInfo(
        name="Dominique Webb",
        title="Full Stack Developer & Problem Solver", 
        description="Passionate about creating innovative solutions and building meaningful digital experiences. I work seamlessly across multiple tech stacks to design scalable, intuitive, and AI-driven applications.",
        email="dominique@domjweb.com",
        linkedin="https://linkedin.com/in/dominiquewebb",
        github="https://github.com/domjweb",
        phone="+1 (555) 123-4567",
        location="Atlanta, GA"
    ),
    
    "experiences": [
        Experience(
            id=1,
            title="Senior Full Stack Developer",
            company="Tech Innovators Inc",
            period="2023 - Present",
            description="Leading development of scalable web applications using React, FastAPI, and Azure cloud technologies. Focus on creating efficient, user-centric solutions.",
            technologies=["React", "FastAPI", "Python", "Azure", "PostgreSQL", "Docker"],
            achievements=[
                "Increased application performance by 45% through optimization",
                "Led cross-functional team of 5 developers",
                "Implemented CI/CD pipelines reducing deployment time by 70%",
                "Architected microservices handling 100K+ daily users"
            ]
        ),
        Experience(
            id=2,
            title="Full Stack Developer",
            company="Digital Solutions Co",
            period="2021 - 2023",
            description="Built end-to-end web applications and APIs for various client projects using modern tech stacks. Focused on delivering high-quality, scalable solutions.",
            technologies=["React", "Node.js", "Express", "MongoDB", "AWS"],
            achievements=[
                "Delivered 20+ client projects on time and under budget",
                "Reduced client onboarding time by 60% through automation",
                "Mentored 3 junior developers",
                "Implemented responsive design increasing mobile engagement by 35%"
            ]
        ),
        Experience(
            id=3,
            title="Frontend Developer",
            company="Creative Web Agency",
            period="2020 - 2021",
            description="Specialized in creating engaging user interfaces and interactive web experiences. Collaborated closely with design teams to bring creative visions to life.",
            technologies=["JavaScript", "React", "HTML5", "CSS3", "SASS"],
            achievements=[
                "Converted 15+ Figma designs to pixel-perfect web interfaces",
                "Improved website loading speeds by 50% through optimization",
                "Established component library used across 10+ projects",
                "Achieved 98% cross-browser compatibility"
            ]
        )
    ],
    
    "projects": [
        Project(
            id=1,
            title="FastFolio - Portfolio Platform",
            description="A modern, responsive portfolio website built with React and FastAPI, featuring dynamic animations, Azure deployment, and Temporal workflow orchestration.",
            technologies=["React", "FastAPI", "Azure Static Web Apps", "Azure Functions", "Temporal", "PostgreSQL"],
            features=[
                "Responsive design with custom animations",
                "Azure cloud deployment with CI/CD",
                "Temporal workflow orchestration",
                "Contact form with database storage",
                "Real-time portfolio updates"
            ],
            github="https://github.com/domjweb/fastfolio",
            demo="https://domjweb.com",
            image="fastfolio-preview.png"
        ),
        Project(
            id=2,
            title="E-Commerce Platform",
            description="Full-stack e-commerce solution with user authentication, payment processing, inventory management, and comprehensive admin dashboard.",
            technologies=["React", "Node.js", "Express", "MongoDB", "Stripe", "JWT"],
            features=[
                "User authentication & authorization",
                "Product catalog with search/filtering",
                "Shopping cart & secure checkout",
                "Payment processing with Stripe",
                "Admin dashboard with analytics",
                "Order tracking and management"
            ],
            github="https://github.com/domjweb/ecommerce-platform",
            demo="https://demo-ecommerce.domjweb.com",
            image="ecommerce-preview.png"
        ),
        Project(
            id=3,
            title="Task Management System", 
            description="Collaborative task management application with real-time updates, team collaboration, file attachments, and progress analytics.",
            technologies=["React", "FastAPI", "WebSockets", "PostgreSQL", "Redis"],
            features=[
                "Real-time collaboration with WebSockets",
                "Task assignment and progress tracking",
                "Team management and permissions",
                "File attachments and comments",
                "Analytics dashboard with insights",
                "Mobile-responsive interface"
            ],
            github="https://github.com/domjweb/task-manager",
            demo="https://tasks.domjweb.com",
            image="taskmanager-preview.png"
        )
    ],
    
    "skills": [
        SkillCategory(
            category="Frontend Development",
            skills=[
                Skill(name="React", level=95, years=4),
                Skill(name="JavaScript/TypeScript", level=90, years=5),
                Skill(name="HTML5/CSS3", level=95, years=6),
                Skill(name="Vue.js", level=75, years=2),
                Skill(name="Next.js", level=80, years=2),
                Skill(name="Tailwind CSS", level=85, years=3)
            ]
        ),
        SkillCategory(
            category="Backend Development",
            skills=[
                Skill(name="Python", level=90, years=4),
                Skill(name="FastAPI", level=90, years=3),
                Skill(name="Node.js", level=85, years=3),
                Skill(name="Express.js", level=80, years=3),
                Skill(name="RESTful APIs", level=95, years=4),
                Skill(name="GraphQL", level=70, years=1)
            ]
        ),
        SkillCategory(
            category="Database & Cloud",
            skills=[
                Skill(name="PostgreSQL", level=85, years=3),
                Skill(name="MongoDB", level=80, years=3),
                Skill(name="Azure", level=85, years=2),
                Skill(name="AWS", level=75, years=2),
                Skill(name="Docker", level=80, years=2),
                Skill(name="Redis", level=70, years=1)
            ]
        ),
        SkillCategory(
            category="Tools & Workflow",
            skills=[
                Skill(name="Git/GitHub", level=95, years=5),
                Skill(name="CI/CD", level=85, years=3),
                Skill(name="Testing (Jest, Pytest)", level=80, years=3),
                Skill(name="Agile/Scrum", level=90, years=4),
                Skill(name="VS Code", level=98, years=5),
                Skill(name="Figma", level=75, years=2)
            ]
        )
    ]
}