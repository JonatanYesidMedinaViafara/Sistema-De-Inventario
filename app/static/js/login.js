document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username === '' || password === '') {
            // Si alguno de los campos está vacío, muestra un mensaje emergente de error
            Swal.fire({
                icon: 'error',
                title: '¡Error!',
                text: 'Por favor, completa todos los campos.',
                confirmButtonText: 'Entendido'
            });
        } else {
            // Si los campos están completos, envía el formulario normalmente
            form.submit();
        }
    });
});
