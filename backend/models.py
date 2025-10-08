# Portfolio Data Models
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Experience Models
class Experience(BaseModel):
    id: int
    title: str
    company: str
    period: str
    description: str
    technologies: List[str]
    achievements: List[str]

class ExperiencesResponse(BaseModel):
    experiences: List[Experience]

# Project Models
class Project(BaseModel):
    id: int
    title: str
    description: str
    technologies: List[str]
    features: List[str]
    github: str
    demo: str
    image: str

class ProjectsResponse(BaseModel):
    projects: List[Project]

# Skills Models
class Skill(BaseModel):
    name: str
    level: int
    years: int

class SkillCategory(BaseModel):
    category: str
    skills: List[Skill]

class SkillsResponse(BaseModel):
    skill_categories: List[SkillCategory]

# About Models
class AboutInfo(BaseModel):
    name: str
    title: str
    description: str
    email: str
    linkedin: str
    github: str
    phone: Optional[str] = None
    location: Optional[str] = None

class AboutResponse(BaseModel):
    about: AboutInfo