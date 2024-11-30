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

body.addEventListener('click', async (e) => {
  const productWrap = document.querySelector('.pproduct')
  if (e.target.closest('.pproduct-block-items__label')) {
    const label = e.target.closest('.pproduct-block-items__label');

    if (label.classList.contains('disabled')) return;

    const productId = +productWrap.getAttribute('data-product-id');
    const variantId = +label.getAttribute('data-variant');

    const res = await PublicAPI.changeProductParams(productId, variantId);
    productWrap.innerHTML = res;

  }
})