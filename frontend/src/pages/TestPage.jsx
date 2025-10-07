import React from 'react';
import BackendTest from '../components/BackendTest';

const TestPage = () => {
  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <h1>🧪 Backend API Testing Page</h1>
      <p>This page is for testing your FastAPI backend connection and endpoints.</p>
      
      <BackendTest />
      
      <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#f8f9fa', borderRadius: '8px', border: '1px solid #dee2e6' }}>
        <h3>📝 Testing Notes</h3>
        <ul>
          <li><strong>Backend URL:</strong> http://127.0.0.1:8000</li>
          <li><strong>Frontend URL:</strong> http://localhost:5173 (or 5174)</li>
          <li><strong>Console:</strong> Press F12 to see detailed test results</li>
          <li><strong>Remove:</strong> Delete this page when testing is complete</li>
        </ul>
      </div>
    </div>
  );
};

export default TestPage;