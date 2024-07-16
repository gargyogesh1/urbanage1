// to get current year
// function getYear() {
//     var currentDate = new Date();
//     var currentYear = currentDate.getFullYear();
//     document.querySelector("#displayYear").innerHTML = currentYear;
// }

// getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


    document.querySelector('.close-button').addEventListener('click', function() {

        document.querySelector('.wrapper').style.display = 'none';
        document.querySelector('.close1').style.display = 'none';
        document.querySelector('.close2').style.display = 'none';


    });

    // document.querySelectorAll('.show-pop_up').forEach(function(button) {
    //     button.addEventListener('click', function() {
    //         // document.querySelector('.wrapper').style.display = 'flex';
    //         document.querySelector('.close1').style.display = 'flex';
    //         document.querySelector('.close2').style.display = 'flex';
    //         document.querySelector('.wrapper').style.display = 'flex';

    //     });
    // });

    document.querySelectorAll('.show-pop_up').forEach(function(button) {
        button.addEventListener('click', function() {
            document.querySelector('.close1').style.display = 'flex';
            document.querySelector('.close2').style.display = 'flex';
            document.querySelector('.wrapper').style.display = 'flex';
        });
    });
    
    function showPopup() {
        setInterval(() => {
            document.querySelector('.close1').style.display = 'flex';
            document.querySelector('.close2').style.display = 'flex';
            document.querySelector('.wrapper').style.display = 'flex';
        }, 1000000); // Show popup every 2 seconds (2000 milliseconds)
    }
    
    // Call showPopup function when the page loads
    showPopup();
    
//     let next = document.querySelector('.next');
// let prev = document.querySelector('.prev');

// next.addEventListener('click', nextSlide);
// prev.addEventListener('click', prevSlide);

// // Function to move to the next slide
// function nextSlide() {
//     let items = document.querySelectorAll('.item');
//     document.querySelector('.slide').appendChild(items[0]);
// }

// // Function to move to the previous slide
// function prevSlide() {
//     let items = document.querySelectorAll('.item');
//     document.querySelector('.slide').prepend(items[items.length - 1]);
// }

// setInterval(nextSlide, 5000);
