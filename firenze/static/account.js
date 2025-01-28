
// if (window.innerWidth < 641) {
//   $('.lk-panel__list').slick({
//     infinite: false,
//     freeMode: true,
//     variableWidth: true,
//   });
// }

const logoutBtn = document.querySelector('.logout');

logoutBtn.onclick = async () => {
  const res = await PublicAPI.logout();
  console.log(res);
  if (res.redirect_link) {
    setTimeout(() => {
      window.location.href = res.redirect_link;
    }, 1500);
  }
  if (res.success && !res.redirect_link) {
    showBaseSnackWithText('Вы успешно вышли из аккаунта!')
    setTimeout(() => {
      window.location.href= "/";
    }, 1500);
    return;
  }
  if (!res.success) {
    showBaseSnackWithText(res.message);
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
      // window.location.href = window.location.href;
    } else {
      showBaseSnackWithText(res.message);
    }
  }
}


const lkImgInp = document.querySelector('.lk-panel__img-inp');
const lkImg = document.querySelector('.lk-panel__img');
if (lkImgInp) {
  lkImgInp.addEventListener('change', async (e) => {
    const form = document.querySelector('form.lk-panel__img-wrap');
    const formData = new FormData(form);

    const res = await PublicAPI.uploadPhoto(formData);

    if (res.success) {
      const reader = new FileReader();
      reader.onloadend = function() {
        lkImg.src = reader.result;
      }
  
      reader.readAsDataURL(lkImgInp.files[0]);
    } else {
      if (res.message) {
        showBaseSnackWithText(res.message)
      } else {
        showBaseSnackWithText('Неизвестная ошибка!Попробуйте позже')
      }
    }

  })
  

}