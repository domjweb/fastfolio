import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navigation = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'About', icon: '👋' },
    { path: '/experience', label: 'Experience', icon: '💼' },
    { path: '/projects', label: 'Projects', icon: '🚀' },
    { path: '/skills', label: 'Skills', icon: '🛠️' },
    { path: '/contact', label: 'Contact', icon: '📬' }
  ];

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  return (
    <nav className="navigation">
      <div className="nav-container">
        <div className="nav-brand">
          <Link to="/" className="brand-link">
            <span className="brand-icon">🏠</span>
            <span className="brand-text">Home</span>
          </Link>
        </div>

        {/* Desktop Navigation */}
        <ul className="nav-menu desktop-menu">
          {navItems.map((item) => (
            <li key={item.path} className="nav-item">
              <Link
                to={item.path}
                className={`nav-link ${location.pathname === item.path ? 'active' : ''}`}
              >
                <span className="nav-icon">{item.icon}</span>
                <span className="nav-text">{item.label}</span>
              </Link>
            </li>
          ))}
        </ul>

        {/* Mobile Menu Toggle */}
        <button 
          className="mobile-menu-toggle"
          onClick={toggleMenu}
          aria-label="Toggle mobile menu"
        >
          <span className="hamburger-line"></span>
          <span className="hamburger-line"></span>
          <span className="hamburger-line"></span>
        </button>

        {/* Mobile Navigation */}
        <div className={`mobile-menu ${isMenuOpen ? 'open' : ''}`}>
          <ul className="mobile-nav-list">
            {navItems.map((item) => (
              <li key={item.path} className="mobile-nav-item">
                <Link
                  to={item.path}
                  className={`mobile-nav-link ${location.pathname === item.path ? 'active' : ''}`}
                  onClick={closeMenu}
                >
                  <span className="nav-icon">{item.icon}</span>
                  <span className="nav-text">{item.label}</span>
                </Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Mobile Menu Overlay */}
        {isMenuOpen && (
          <div className="mobile-menu-overlay" onClick={closeMenu}></div>
        )}
      </div>
    </nav>
  );
};

export default Navigation;