var wow = new WOW(
    {
        boxClass: 'wow',      // animated element css class (default is wow)
        animateClass: 'animated', // animation css class (default is animated)
        offset: 0,          // distance to the element when triggering the animation (default is 0)
        mobile: true,       // trigger animations on mobile devices (default is true)
        live: true,       // act on asynchronously loaded content (default is true)
        callback: function (box) {
            // the callback is fired every time an animation is started
            // the argument that is passed in is the DOM node being animated
        },
        scrollContainer: null // optional scroll container selector, otherwise use window
    }
);

// $(window).on('load', function () { // makes sure the whole site is loaded 
//     $('#status').fadeOut(); // will first fade out the loading animation 
//     $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
//     $('body').delay(100).css({ 'overflow': 'visible' });
// })
var loader = document.querySelector(".loader");

window.addEventListener("load", vanish);

function vanish() {
    wow.init();
    // loader.fadeOut("slow");
    // preloader.fadeOut("slow");
    // bod.css({'overflow': 'visible'});
    loader.classList.add("disappear");
}
