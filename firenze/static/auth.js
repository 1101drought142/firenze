const signUpBtn = document.querySelector('.auth__signup');

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
  if (passInp.value !== passConfirmInp) {
    showBaseSnackWithText('Ошибка! Пароли не совпадают!');
    return;
  }


  const formData = new FormData(signUpForm);
  const res = await PublicAPI.signUp(formData);
  console.log(res);

}