
if (window.innerWidth < 641) {
  $('.lk-panel__list').slick({
    infinite: false,
    freeMode: true,
    variableWidth: true,
  });
}

const logoutBtn = document.querySelector('.logout');

logoutBtn.onclick = async () => {
  const res = await PublicAPI.logout();
  console.log(res);
  if (res.redirect_link) {
    window.location.href = res.redirect_link;
  }
  if (res.success && !res.redirect_link) {
    showBaseSnackWithText('Вы успешно вышли из аккаунта!')
    window.location.href= "/";
    return;
  }
  if (!res.success) {
    showSnack(res.message);
  }
}

const lkSave = document.querySelector('.lk__save');
if (lkSave) {
  lkSave.onclick = async (e) => {
    e.preventDefault();
    const form = lkSave.closest('form.lk-content');
    const formData = new FormData(form);

    const res = await PublicAPI.changeInfo(formData);
    if (res.success) {
      showBaseSnackWithText('Данные успешно изменены');
      window.location.href = window.location.href;
    } else {
      showBaseSnackWithText(res.message);
    }
  }
}