document.addEventListener('DOMContentLoaded', () => {
    // Auto-generate the current date and time
    const fechaInput = document.getElementById('fecha');
    const horaInput = document.getElementById('hora');
    const now = new Date();
    fechaInput.value = now.toLocaleDateString('es-ES');
    horaInput.value = now.toLocaleTimeString('es-ES');

    // Simulate fetching product name based on product number
    const numeroProductoInput = document.getElementById('numero_producto');
    const nombreProductoInput = document.getElementById('nombre_producto');

    numeroProductoInput.addEventListener('blur', () => {
        const numeroProducto = numeroProductoInput.value.trim();

        // Simulate fetching product name from a database or an API
        if (numeroProducto) {
            // Replace this with actual fetching logic
            const productoNombres = {
                '001': 'Producto A',
                '002': 'Producto B',
                '003': 'Producto C'
            };
            nombreProductoInput.value = productoNombres[numeroProducto] || 'Producto desconocido';
        } else {
            nombreProductoInput.value = '';
        }
    });
});
