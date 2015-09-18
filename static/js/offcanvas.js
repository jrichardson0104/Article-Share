$(document).ready(function () {
  $('[data-toggle="offcanvas"]').click(function () {
    $('.row-offcanvas').toggleClass('active')
  });
});

$(document).ready(function () {
  $('.list-group-item').hover(function () {
    $(this).toggleClass('active')
  });
  // $('.list-group-item').mouseleave(function () {
  //   $(this).removeClass('active')
  // });

});

