import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import './App.css';
import Navigation from './components/navigation/Navigation';
import ScrollToTop from './components/ScrollToTop';
import ErrorBoundary from './components/ErrorBoundary';
import About from './pages/About';
import Experience from './pages/Experience';
import Projects from './pages/Projects';
import Skills from './pages/Skills';
import Contact from './pages/Contact';
import TestPage from './pages/TestPage';

// Component to handle route changes and scroll
const RouteHandler = ({ children }) => {
  const location = useLocation();
  
  useEffect(() => {
    // Log route changes for debugging
    console.log('Route changed to:', location.pathname);
    
    // Scroll to top on route change
    window.scrollTo(0, 0);
  }, [location.pathname]);
  
  return children;
};

const App = () => {
  return (
    <ErrorBoundary>
      <Router>
        <RouteHandler>
          <div className="App">
            <Navigation />
            <main className="main-content">
              <ErrorBoundary>
                <Routes>
                  <Route path="/" element={<About />} />
                  <Route path="/experience" element={<Experience />} />
                  <Route path="/projects" element={<Projects />} />
                  <Route path="/skills" element={<Skills />} />
                  <Route path="/contact" element={<Contact />} />
                  <Route path="/test" element={<TestPage />} />
                  {/* Catch-all route for better SPA behavior */}
                  <Route path="*" element={<Navigate to="/" replace />} />
                </Routes>
              </ErrorBoundary>
            </main>
            <ScrollToTop />
          </div>
        </RouteHandler>
      </Router>
    </ErrorBoundary>
  );
};

export default App;
