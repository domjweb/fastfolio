import React, { useState } from 'react';
import { portfolioAPI } from '../api';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    

    try {
      // Use the API utility to send contact form
      await portfolioAPI.sendContact(formData);
      setSubmitStatus('success');
      setFormData({ name: '', email: '', subject: '', message: '' });
    } catch (error) {
      setSubmitStatus('error');
    }
    
    setIsSubmitting(false);
  };

  return (
    <div className="contact-page">
      <div className="page-header">
        <h1>Let's Connect</h1>
        <p>I'm always interested in new opportunities and collaborations</p>
      </div>
      
      <div className="contact-content">
        <div className="contact-info">
          <h3>Get In Touch</h3>
          <p>
            Whether you have a project in mind, want to discuss opportunities, 
            or just want to say hello, I'd love to hear from you!
          </p>
          
          <div className="contact-methods">
            <div className="contact-item">
              <span className="icon">📧</span>
              <div>
                <h4>Email</h4>
                <a href="mailto:dominique@domjweb.com">dwebb@domjweb.com</a>
              </div>
            </div>
            
            <div className="contact-item">
              <span className="icon">💼</span>
              <div>
                <h4>LinkedIn</h4>
                <a href="https://linkedin.com/in/dominique-webb" target="_blank" rel="noopener noreferrer">
                  linkedin.com/in/domjweb
                </a>
              </div>
            </div>
            
            <div className="contact-item">
              <span className="icon">💻</span>
              <div>
                <h4>GitHub</h4>
                <a href="https://github.com/domjwebb" target="_blank" rel="noopener noreferrer">
                  github.com/domjweb
                </a>
              </div>
            </div>
            
            <div className="contact-item">
              <span className="icon">🌐</span>
              <div>
                <h4>Links</h4>
                <a href="https://linktr.ee/domjweb" target="_blank" rel="noopener noreferrer">
                  linktr.ee/domjweb
                </a>
              </div>
            </div>
          </div>
        </div>
        
        <div className="contact-form-container">
          <h3>Send Me a Message</h3>
          
          {submitStatus && (
            <div className={`status-message ${submitStatus}`}>
              {submitStatus === 'success' && '✅ Message sent successfully!'}
              {submitStatus === 'error' && '❌ Failed to send message. Please try again.'}
              {submitStatus === 'demo' && '🔄 Demo mode: Message logged to console'}
            </div>
          )}
          
          <form onSubmit={handleSubmit} className="contact-form">
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                required
                placeholder="Your full name"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                required
                placeholder="your.email@example.com"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="subject">Subject</label>
              <input
                type="text"
                id="subject"
                name="subject"
                value={formData.subject}
                onChange={handleInputChange}
                required
                placeholder="What's this about?"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea
                id="message"
                name="message"
                value={formData.message}
                onChange={handleInputChange}
                required
                rows="5"
                placeholder="Tell me more about your project or inquiry..."
              ></textarea>
            </div>
            
            <button 
              type="submit" 
              className="btn btn-primary"
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Sending...' : 'Send Message'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Contact;