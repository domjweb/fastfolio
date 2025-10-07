import React, { useState, useEffect } from 'react';

const ScrollToTop = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [isLaunching, setIsLaunching] = useState(false);

  // Show rocket when user scrolls down
  useEffect(() => {
    const toggleVisibility = () => {
      if (window.pageYOffset > 300) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', toggleVisibility);
    return () => window.removeEventListener('scroll', toggleVisibility);
  }, []);

  const scrollToTop = () => {
    setIsLaunching(true);
    
    // Smooth scroll to top
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });

    // Reset launch animation after scroll
    setTimeout(() => {
      setIsLaunching(false);
    }, 1000);
  };

  return (
    <div
      className={`scroll-to-top ${isVisible ? 'visible' : ''} ${isLaunching ? 'launching' : ''}`}
      onClick={scrollToTop}
      title="Blast off to top!"
    >
      🚀
    </div>
  );
};

export default ScrollToTop;