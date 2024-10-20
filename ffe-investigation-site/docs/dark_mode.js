document.addEventListener('DOMContentLoaded', function() {
    // Force the dark mode by setting the color scheme to 'slate'
    document.documentElement.setAttribute('data-md-color-scheme', 'slate');
    localStorage.setItem('data-md-color-scheme', 'slate'); // Persist dark mode across sessions
});