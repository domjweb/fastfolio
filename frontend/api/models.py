from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class ContactResponse(BaseModel):
    message: str
    contact_id: str
    status: str

class Experience(BaseModel):
    title: str
    company: str
    location: str
    start_date: str
    end_date: Optional[str] = None
    description: List[str]
    technologies: List[str]

class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None

class Skill(BaseModel):
    name: str
    proficiency: int  # 1-5 scale

class SkillCategory(BaseModel):
    category: str
    skills: List[Skill]

class AboutInfo(BaseModel):
    name: str
    title: str
    summary: str
    location: str
    email: str
    linkedin: Optional[str] = None
    github: Optional[str] = None