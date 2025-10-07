import { useEffect, useState } from 'react';

// Custom hook for scroll-triggered animations
export const useScrollAnimation = (threshold = 0.1) => {
  const [isVisible, setIsVisible] = useState(false);
  const [elementRef, setElementRef] = useState(null);

  useEffect(() => {
    if (!elementRef) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          // Stop observing after first trigger to prevent memory leaks
          observer.unobserve(elementRef);
        }
      },
      { threshold }
    );

    observer.observe(elementRef);

    return () => {
      observer.disconnect();
    };
  }, [elementRef, threshold]);

  return [setElementRef, isVisible];
};

// Custom hook for typewriter effect
export const useTypewriter = (text, speed = 100, startDelay = 0) => {
  const [displayText, setDisplayText] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    setIsTyping(true);
    setDisplayText('');
    
    let timeout;
    let timer;
    let isCancelled = false;
    
    timeout = setTimeout(() => {
      if (isCancelled) return;
      let index = 0;
      timer = setInterval(() => {
        if (isCancelled) {
          clearInterval(timer);
          return;
        }
        if (index < text.length) {
          setDisplayText(text.slice(0, index + 1));
          index++;
        } else {
          setIsTyping(false);
          clearInterval(timer);
        }
      }, speed);
    }, startDelay);

    return () => {
      isCancelled = true;
      clearTimeout(timeout);
      clearInterval(timer);
    };
  }, [text, speed, startDelay]);

  return { displayText, isTyping };
};

// Custom hook for staggered animations
export const useStaggeredAnimation = (itemCount, delay = 100) => {
  const [visibleItems, setVisibleItems] = useState(new Set());

  const triggerAnimation = () => {
    for (let i = 0; i < itemCount; i++) {
      setTimeout(() => {
        setVisibleItems(prev => new Set([...prev, i]));
      }, i * delay);
    }
  };

  const resetAnimation = () => {
    setVisibleItems(new Set());
  };

  return { visibleItems, triggerAnimation, resetAnimation };
};