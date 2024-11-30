const signUpBtn = document.querySelector('.auth__signup');

if (signUpBtn) {
  signUpBtn.onclick = async (e) => {
    e.preventDefault();
    const signUpForm = document.querySelector('.signUpForm');
    const hasUnfilled = checkRequiredFields(signUpForm);
    if (hasUnfilled) {
      return;
    }
    
    // validation
    const passInp = signUpForm.querySelector('input[name="password"]');
    const passConfirmInp = signUpForm.querySelector('input[name="passwordConfirm"]');
    if (passInp.value !== passConfirmInp.value) {
      showBaseSnackWithText('Ошибка! Пароли не совпадают!');
      return;
    }
  
  
    const formData = new FormData(signUpForm);
    const res = await PublicAPI.signUp(formData);
    if (res.redirect_link) {
      showBaseSnackWithText('Успешно! Вы зарегистрировались!');
      window.location.href = redirect_link;
    }
  }
}

const authBtn = document.querySelector('.auth__login');

if (authBtn) {
  authBtn.onclick = async (e) => {
    console.log('123');
    e.preventDefault();
    const loginForm = document.querySelector('.loginForm');
    let hasUnfilled = false;
    if (document.querySelector('.loginForm .tab-content.active input').value.length < 6) { hasUnfilled = true};
    if (document.querySelector('.passwordInput input').value.length < 3) { hasUnfilled = true };
    if (hasUnfilled) {
      console.log(hasUnfilled)
      showBaseSnackWithText('Ошибка! Заполните все поля!')
      return;
    }
    
    const formData = new FormData(loginForm);
    const res = await PublicAPI.signUp(formData);
    if (res.success) {
      showBaseSnackWithText('Успешно! Вы авторизовались');
    }
    if (res.redirect_link) {
      window.location.href = redirect_link;
    }
    if (!res.success) {
      showSnack(res.message)
    }
  }
}