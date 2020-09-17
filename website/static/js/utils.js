// // change header image after 2 seconds
// var images = ['parallax_04.jpg','intro-bg.jpg','dog.png', 'ipad.png'],
//     index = 0, // starting index
//     maxImages = images.length - 1;
// var timer = setInterval(function() {
//     var currentImage = images[index];
//     index = (index == maxImages) ? 0 : ++index;
//     $('.intro-header').fadeOut(500, function() {
//         $('.intro-header').attr("style", 'background-image:url(/static/img/'+currentImage);
//         $('.intro-header').fadeIn(500);
//     });
//  }, 5000);
//

$(document).ready(function () {
    $(".manipfil").click(function () {
        $(".ftotal").toggleClass("fechado");
    });
});

$('.form_datetime').datetimepicker({
    language:  'pt-BR',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 1,
    forceParse: 0,
    showMeridian: 1
});

$('.form_date').datetimepicker({
    language:  'pt-BR',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0
});

$(function() {
  $("#locations").autocomplete({
    source: "/api/get_locations/",
    minLength: 2,
  });
});

/* swiper start */
var swiper = new Swiper('.swiper-container', {
    pagination: '.swiper-pagination',
    paginationClickable: true,
    autoplay: 10000,
    loop: true,

});