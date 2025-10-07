import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Navigation from './components/navigation/Navigation';
import ScrollToTop from './components/ScrollToTop';
import About from './pages/About';
import Experience from './pages/Experience';
import Projects from './pages/Projects';
import Skills from './pages/Skills';
import Contact from './pages/Contact';
import TestPage from './pages/TestPage';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<About />} />
            <Route path="/experience" element={<Experience />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/skills" element={<Skills />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/test" element={<TestPage />} />
          </Routes>
        </main>
        <ScrollToTop />
      </div>
    </Router>
  );
};

export default App;
