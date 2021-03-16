// $('#recipeCarousel').carousel({
//     interval: 5000
// })

// $('.carousel .carousel-item').each(function () {
//     var minPerSlide = 4;
//     var next = $(this).next();
//     if (!next.length) {
//         next = $(this).siblings(':first');
//     }
//     next.children(':first-child').clone().appendTo($(this));

//     for (var i = 0; i < minPerSlide; i++) {
//         next = next.next();
//         if (!next.length) {
//             next = $(this).siblings(':first');
//         }

//         next.children(':first-child').clone().appendTo($(this));
//     }
// });
$("#sponserpage-slider").owlCarousel({
    items:4,
    itemsDesktop:[1000,4],
    itemsDesktopSmall:[979,3],
    itemsTablet:[768,2],
    itemsMobile:[650,1],
    pagination:true,
    mouseDrag :false,
    nav:false,
    slideSpeed:1000,
    autoPlay:false
});