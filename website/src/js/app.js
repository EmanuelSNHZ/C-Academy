document.addEventListener( 'DOMContentLoaded', function() {

    eventListeners();
} );

function eventListeners() {
    const mobileMenu = document.querySelector( '.mobile-menu' );

    mobileMenu.addEventListener( 'click', navegacionMobile );
};

function navegacionMobile() {
    // console.log('Prueba navegacion mobile');
    const navegacion = document.querySelector('.navegacion');
    navegacion.classList.toggle('menu-activo')
};