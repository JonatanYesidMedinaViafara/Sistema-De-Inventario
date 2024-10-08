document.addEventListener('DOMContentLoaded', function() {
    // Código JavaScript a ejecutar cuando el DOM esté completamente cargado

    // Por ejemplo, podrías agregar algún evento click a un elemento de la página
    const linkInicio = document.querySelector('#link-inicio');
    linkInicio.addEventListener('click', function(event) {
        // Evitar el comportamiento predeterminado del enlace
        event.preventDefault();
        
        // Redirigir al usuario a la página de inicio
        window.location.href = '/';
    });
});
