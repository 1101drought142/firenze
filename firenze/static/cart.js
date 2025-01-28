const removeBtns = document.querySelectorAll('.cart-item__remove');
removeBtns.forEach(btn => {
  btn.onclick = async (e) => {
    e.preventDefault();
    const item = btn.closest('.cart-item');
    const id = item.getAttribute('variant-id');

    const res = await PublicAPI.removeFromCart(id);
    document.querySelector('form.cart').innerHTML = res;
    // if (res.success) {
    //   showBaseSnackWithText('Товару успешно удалён!');
    //   item.remove();
    // } else if (!res.success) {
    //   showBaseSnackWithText(res.message);
    // } else {
    //   showBaseSnackWithText('Непредвиденная ошибка!');
    // }
  }
})


window.addEventListener('click', async (e) => {
  if (e.target.closest('.dropdown-list__item')) {
    const cart = e.target.closest('.cart');
    // const product = e.target.closest('.cart-item');
    const item = e.target.closest('.dropdown-list__item');
    const variantId = item.getAttribute('data-val');
    const productId = item.closest('.cart-item').getAttribute('product-id');

    const res = await PublicAPI.changeCartProductParam(productId, variantId);
    // console.log(res);

    cart.innerHTML = res;
    // console.log(product);
    // cart.replaceChildren(product, res);
  }
})