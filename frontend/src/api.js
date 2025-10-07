// Portfolio API configuration
const API_BASE_URL = 'http://localhost:8000';

// API endpoints for portfolio data
export const portfolioAPI = {
  // Get all experiences
  getExperiences: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/experiences`);
      if (!response.ok) throw new Error('Failed to fetch experiences');
      return await response.json();
    } catch (error) {
      console.error('Error fetching experiences:', error);
      throw error;
    }
  },

  // Get all projects
  getProjects: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/projects`);
      if (!response.ok) throw new Error('Failed to fetch projects');
      return await response.json();
    } catch (error) {
      console.error('Error fetching projects:', error);
      throw error;
    }
  },

  // Get all skills
  getSkills: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/skills`);
      if (!response.ok) throw new Error('Failed to fetch skills');
      return await response.json();
    } catch (error) {
      console.error('Error fetching skills:', error);
      throw error;
    }
  },

  // Send contact form
  sendContact: async (formData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/contact`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
      if (!response.ok) throw new Error('Failed to send message');
      return await response.json();
    } catch (error) {
      console.error('Error sending contact form:', error);
      throw error;
    }
  },

  // Get about/personal info
  getAboutInfo: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/about`);
      if (!response.ok) throw new Error('Failed to fetch about info');
      return await response.json();
    } catch (error) {
      console.error('Error fetching about info:', error);
      throw error;
    }
  }
};

// Default export for backward compatibility
export default {
  get: (url) => fetch(`${API_BASE_URL}${url}`).then(res => {
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    return res.json().then(data => ({ data }));
  }),
  post: (url, data) => fetch(`${API_BASE_URL}${url}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then(res => {
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    return res.json().then(data => ({ data }));
  })
};