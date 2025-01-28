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
    if (res.success) {
      showBaseSnackWithText('Успешно! Вы зарегистрировались!');
      if (res.redirect_link) {
        window.location.href = res.redirect_link;
      } else {
        setTimeout(() => {
          window.location.href = '/account/';
        }, 1500);
      }
    } else {
      showBaseSnackWithText('Ошибка! Попробуйте позже');
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
    const res = await PublicAPI.login(formData);
    if (res.success) {
      showBaseSnackWithText('Успешно! Вы авторизовались');
    }
    if (res.redirect_link) {
      window.location.href = res.redirect_link;
    }
    if (!res.success) {
      showBaseSnackWithText(res.message)
    }
  }
}

const forgotBtn = document.querySelector('.auth__forgotRequest');

if (forgotBtn) {
  forgotBtn.onclick = async (e) => {
    e.preventDefault();
    const forgotForm = document.querySelector('.forgotForm');
    let hasUnfilled = checkRequiredFields(forgotForm);
    if (hasUnfilled) {
      showBaseSnackWithText('Ошибка! Заполните все поля!')
      return;
    }

    if (document.querySelector('.input__field').value.length < 3) {
      showBaseSnackWithText('Ошибка!Заполните корректно почту')
      return;
    }
    if (document.querySelector('.input.error')) {
      showBaseSnackWithText('Ошибка!Заполните корректно почту')
      return;
    }

    const formData = new FormData(forgotForm);
    const res = await PublicAPI.forgotPass(formData);
    if (res.success) {
      showBaseSnackWithText('Отправили письмо! Не забудьте проверить папку "Спам" ');

      document.querySelector('.auth-choice__title').innerHTML = `На вашу почту направлено письмо с инструкцией по восстановлению пароля от аккаунта, следуйте шагам в инструкции. <br><br>Если письмо не приходит, проверьте папку “Спам”`
      document.querySelector('.forgot__goAuth').classList.add('active');
      forgotBtn.classList.remove('active');
    }
    if (res.redirect_link) {
      window.location.href = res.redirect_link;
      return;
    }
    if (!res.success) {
      showBaseSnackWithText(res.message)
    }
    
  }
}