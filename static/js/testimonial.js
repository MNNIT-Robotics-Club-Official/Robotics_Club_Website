
$(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:2,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        itemsMobile:[650,1],
        pagination:true,
        navigation:false,
        mouseDrag : false,
        slideSpeed:1000,
        autoPlay:8000
    });
});