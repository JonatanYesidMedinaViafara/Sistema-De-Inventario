// JavaScript para el HTML de bienvenida (opcional)
// Puedes añadir interactividad o efectos si lo deseas
// Por ejemplo, un efecto de desplazamiento suave a las secciones al hacer clic en los enlaces del menú

document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('a[href^="#"]');
  
    for (const link of links) {
        link.addEventListener('click', scrollToSection);
    }
});

function scrollToSection(e) {
    e.preventDefault();

    const targetId = this.getAttribute('href').substring(1);
    const targetSection = document.getElementById(targetId);
  
    if (targetSection) {
        const topOffset = targetSection.offsetTop;
        window.scrollTo({
            top: topOffset,
            behavior: 'smooth'
        });
    }
}
