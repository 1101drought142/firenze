var thumbsSwiper = new Swiper(".pproduct-slider-sub", {
  spaceBetween: 10,
  freeMode: true,
  watchSlidesProgress: true,
  slidesPerView: 'auto',
});

var mainSwiper = new Swiper(".pproduct-slider-main", {
  spaceBetween: 10,
  thumbs: {
    swiper: thumbsSwiper,
  },
});