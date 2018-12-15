$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.carousel').carousel();

    $('.carousel.carousel-slider').carousel({
        fullWidth: true
    });
    $('select').formSelect();
    $('.datepicker').datepicker({
        selectMonths: true, // Creates a dropdown to control month
        format: 'dd-mm-yyyy'    
    });
});
