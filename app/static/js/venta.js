document.addEventListener('DOMContentLoaded', function() {
    // Generar automáticamente nombre de empleado, fecha y hora
    var nombreEmpleadoInput = document.getElementById('nombre_empleado');
    var fechaInput = document.getElementById('fecha');
    var horaInput = document.getElementById('hora');

    // Puedes implementar la lógica para obtener el nombre del empleado, fecha y hora actual aquí
    
    // Simplemente como ejemplo, vamos a establecer valores estáticos
    nombreEmpleadoInput.value = "Nombre del Empleado";
    fechaInput.value = obtenerFechaActual();
    horaInput.value = obtenerHoraActual();
});

function obtenerFechaActual() {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    return yyyy + '-' + mm + '-' + dd;
}

function obtenerHoraActual() {
    var now = new Date();
    var hh = String(now.getHours()).padStart(2, '0');
    var mm = String(now.getMinutes()).padStart(2, '0');
    return hh + ':' + mm;
}
