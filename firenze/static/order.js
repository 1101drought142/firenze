const orderBtn = document.querySelector('.order__offer');
const orderForm = document.querySelector('form.order');

orderBtn.onclick = async (e) => {
  e.preventDefault();

  if (checkRequiredFields(orderForm)) {
    return;
  }

  const res = await PublicAPI.order(new FormData(orderForm));
  if (res.success) {
    showBaseSnackWithText('Заказу успешно оформлен!')
    if (res.redirect_link) {
      window.location.href= res.redirect_link;
    }
  } else {
    showBaseSnackWithText(res.message);
  }
}