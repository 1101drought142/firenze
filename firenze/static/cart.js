const removeBtns = document.querySelectorAll('.cart-item__remove');
removeBtns.forEach(btn => {
  btn.onclick = async (e) => {
    e.preventDefault();
    const item = btn.closest('.cart-item');
    const id = item.getAttribute('variant-id');

    const res = await PublicAPI.removeFromCart(id);
    if (res.success) {
      showBaseSnackWithText('Товару успешно удалён!');
      item.remove();
    } else if (!res.success) {
      showBaseSnackWithText(res.message);
    } else {
      showBaseSnackWithText('Непредвиденная ошибка!');
    }
  }
})