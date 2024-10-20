document.addEventListener('DOMContentLoaded', function() {
    document.documentElement.setAttribute('data-md-color-scheme', 'slate');  // Force dark mode
    localStorage.setItem('data-md-color-scheme', 'slate');  // Persist dark mode across sessions
});

// Google Analytics
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-FF4SS4SRX9');

// Clarity
(function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "olrkim6xfb");