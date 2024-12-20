const modalBg = document.querySelector('.modal-bg');
const body = document.querySelector('body');
function changeModalBgState(state = 'toggle') {
  if (state = 'toggle') {
    modalBg.classList.toggle('active');
    body.classList.toggle('disabled');
    return;
  } 
  if (state = 'enable') {
    modalBg.classList.add('active');
    body.classList.add('disabled');
    return;
  }
  if (state = 'disable') {
    modalBg.classList.remove('active');
    body.classList.remove('disabled');
    return;
  }
};
const closeOverlays = document.querySelectorAll('.close-overlays');
closeOverlays.forEach(close => {
  close.addEventListener('click', () => {
    body.classList.remove('disabled');
    modalBg.classList.remove('active');
    document.querySelectorAll('.overlayContent').forEach(ov => ov.classList.remove('active'))
  }
)});

const burgerBtn = document.querySelector('.burger-btn');
const burgerMenu = document.querySelector('.burger-menu');
burgerBtn.onclick = () => {
  burgerBtn.classList.toggle('opened');
  burgerMenu.classList.toggle('active');
  body.classList.toggle('disabled');
}


const modalBtns = document.querySelectorAll('.open-modal');

modalBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const modalClass = btn.getAttribute('data-modal');
    const modal = document.querySelector(`.${modalClass}`);

    modal.classList.add('active');
    changeModalBgState('enable');
  })
})


const favBtns = document.querySelectorAll('.fav-btn');

favBtns.forEach(fav => {

  fav.onclick = (e) => {
    e.preventDefault();
    // promise callback
    const snack = document.querySelector('.fav-snack');

    snack.classList.add('active')
    setTimeout(() => {
      snack.classList.remove('active')
    }, 4500);
  }

})