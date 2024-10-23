document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe[data-src]');
    iframes.forEach(iframe => {
        const src = iframe.getAttribute('data-src');
        iframe.src = src.replace('{base_url}', window.location.pathname.replace(/\/[^/]*$/, ''));
    });
});