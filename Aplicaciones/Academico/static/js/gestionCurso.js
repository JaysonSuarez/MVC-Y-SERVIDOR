 /*Creamos una funcion que mediante el evento click en el boton eliminar, muestre en pantalla un mensaje
 donde se pregunte si esta seguro de eliminar el curso, esto con el fin de evitar accidentes*/
(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el curso?');
            if(!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();

