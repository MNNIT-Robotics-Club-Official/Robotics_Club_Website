
$(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:2,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        itemsMobile:[650,1],
        pagination:true,
        mouseDrag :false,
        navigation:false,
        slideSpeed:1000,
        autoPlay:8000
    });

    $("#sponsor-slider").owlCarousel({
        items: 4,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        itemsMobile:[650,1],
        pagination:true,
        mouseDrag :false,
        navigation:false,
        slideSpeed:1000,
        autoPlay:8000
    });

    $("#home-testimonial-slider").owlCarousel({
        items:2,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,1],
        itemsMobile:[650,1],
        pagination:true,
        mouseDrag :false,
        nav:true,
        navigation:true,
        navigationText: [
                "<i class='icon-arrow-left icon-white'><</i>",
                "<i class='icon-arrow-right icon-white'>></i>"
              ],
        navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
        slideSpeed:1000,
        autoPlay:8000
    });
});