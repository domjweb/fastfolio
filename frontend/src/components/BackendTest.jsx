import React from 'react';

const BackendTest = () => {
  // Test backend connection
  const testBackendConnection = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/', {
        method: 'GET',
      });
      const data = await response.json();
      console.log('✅ Backend connected:', data);
      alert('Backend Connected! Check console for details.');
    } catch (error) {
      console.error('❌ Backend connection failed:', error);
      alert('Backend connection failed! Check console for details.');
    }
  };

  // Test contact form submission
  const testContactSubmission = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: 'React Test User',
          email: 'react@test.com', 
          subject: 'Test from React',
          message: 'This is a test from the React frontend'
        })
      });
      const data = await response.json();
      console.log('✅ Contact submitted:', data);
      alert('Contact form test successful! Check console for details.');
    } catch (error) {
      console.error('❌ Contact submission failed:', error);
      alert('Contact submission failed! Check console for details.');
    }
  };

  // Test all endpoints
  const testAllEndpoints = async () => {
    console.log('🧪 Testing all endpoints...');
    
    const endpoints = [
      { name: 'About', url: 'http://127.0.0.1:8000/about' },
      { name: 'Experiences', url: 'http://127.0.0.1:8000/experiences' },
      { name: 'Projects', url: 'http://127.0.0.1:8000/projects' },
      { name: 'Skills', url: 'http://127.0.0.1:8000/skills' }
    ];

    for (const endpoint of endpoints) {
      try {
        const response = await fetch(endpoint.url);
        const data = await response.json();
        console.log(`✅ ${endpoint.name} endpoint:`, data);
      } catch (error) {
        console.error(`❌ ${endpoint.name} endpoint failed:`, error);
      }
    }
  };

  return (
    <div style={{ padding: '2rem', backgroundColor: '#f0f0f0', margin: '2rem', borderRadius: '8px' }}>
      <h3>🧪 Backend API Testing</h3>
      <p>Use these buttons to test your FastAPI backend connection:</p>
      
      <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', marginTop: '1rem' }}>
        <button 
          onClick={testBackendConnection}
          style={{ padding: '0.5rem 1rem', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
        >
          Test Basic Connection
        </button>
        
        <button 
          onClick={testContactSubmission}
          style={{ padding: '0.5rem 1rem', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
        >
          Test Contact Form
        </button>
        
        <button 
          onClick={testAllEndpoints}
          style={{ padding: '0.5rem 1rem', backgroundColor: '#ffc107', color: 'black', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
        >
          Test All Endpoints
        </button>
      </div>
      
      <div style={{ marginTop: '1rem', padding: '1rem', backgroundColor: '#e9ecef', borderRadius: '4px' }}>
        <strong>Instructions:</strong>
        <ol>
          <li>Make sure your FastAPI server is running on port 8000</li>
          <li>Click the buttons above to test different endpoints</li>
          <li>Open browser console (F12) to see detailed results</li>
          <li>Remove this component when testing is complete</li>
        </ol>
      </div>
    </div>
  );
};

export default BackendTest;