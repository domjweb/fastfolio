import React, { useEffect, useRef } from 'react';
import { useTypewriter } from '../hooks/animations';
import profileImage from '../assets/profile.jpg';

const About = () => {
  const { displayText } = useTypewriter("Hello, I'm Dominique", 150, 500);

  return (
    <div className="about-page">
      <div className="hero-section">
        <div className="hero-content">
          <h1 className="typewriter">{displayText}<span className="cursor">|</span></h1>
          <h2 className="fade-in-up">Full Stack Developer & Problem Solver</h2>
          <p className="intro-text fade-in-up delay-1">
            Passionate about creating innovative solutions and building 
            meaningful digital experiences. Welcome to my portfolio!
          </p>
        </div>
        <div className="hero-image">
          <img 
            src={profileImage} 
            alt="Dominique Webb - Profile Photo" 
            className="profile-photo"
          />
        </div>
      </div>
      
      <div className="about-content">
        <section className="overview">
          <h3>About Me</h3>
          <p>
            I’m a full-stack software engineer passionate about creating solutions that simplify 
            complex problems and make a real impact. I work seamlessly across multiple tech stacks 
            to design scalable, intuitive, and AI-driven applications. What drives me is turning technical 
            challenges into smooth, user-focused experiences!
          </p>
        </section>
        
        <section className="highlights">
          <h3>Key Highlights</h3>
          <div className="highlight-grid">
            <div className="highlight-card">
              <h4>🚀 Experience</h4>
              <p>Turning ideas into impactful products — each line of code shaped by curiosity and craft.</p>
            </div>
            <div className="highlight-card">
              <h4>💡 Projects</h4>
              <p>From concept to launch, I build projects that blend creativity, scalability, and purpose.</p>
            </div>
            <div className="highlight-card">
              <h4>🛠️ Technologies</h4>
              <p>A tech chameleon — fluent across stacks, always exploring new tools that push innovation forward.</p>
            </div>
            <div className="highlight-card">
              <h4>🎯 Focus</h4>
              <p>Clean code, seamless design, and experiences that make technology feel effortless.</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default About;