document.addEventListener('DOMContentLoaded', function() {
    document.documentElement.setAttribute('data-md-color-scheme', 'slate');  // Force dark mode
    localStorage.setItem('data-md-color-scheme', 'slate');  // Persist dark mode across sessions
});