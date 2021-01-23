// Used bootstrap v4.5,jquery v3.5.1, owl carousel v2, font awesome v4.7.0

$('.testi.owl-carousel').owlCarousel({
    items: 2,
    margin: 10,
    lazyLoad: true,
    dots: true,
    autoPlay: true,
    autoPlayTimeout: 3000,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 2,
        },
        1000: {
            items: 2,
        }
    }
});