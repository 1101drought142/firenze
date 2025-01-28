// utils
const showSnack = (classname) => {
  const snack = document.querySelector(`.${classname}`);

  document.querySelectorAll('.snack').forEach(sn => sn.classList.remove('active'));
  snack.classList.add('active')
  setTimeout(() => {
    snack.classList.remove('active')
  }, 4500);
}

const showBaseSnackWithText = (text) => {
  document.querySelectorAll('.snack').forEach(sn => sn.classList.remove('active'));
  const snack = document.querySelector('.base-snack');
  const snackTextField = snack.querySelector('.base-snack-content');
  snackTextField.textContent = text;
  snack.classList.add('active');
  setTimeout(() => {
    snack.classList.remove('active')
  }, 4500);
  
}

const checkRequiredFields = (form) => {
  const requiredFields = form.querySelectorAll('input.required');
  let hasError = false;
  requiredFields.forEach(field => {
    if (field.value.length < 3) {
      console.log('wait');
      if (!field.closest('.tab-content:not(.active)')) {
        console.log('suc', field.closest('.tab-content:not(.active)'));
        hasError = true;
      }
    }
  })

  if (hasError) {
    showBaseSnackWithText('Ошибка! Заполните все обязательные поля');
    return true;
  } 
  return false;

}

const debounce = (callback, wait) => {
  let timeoutId = null;
  return (...args) => {
    window.clearTimeout(timeoutId);
    timeoutId = window.setTimeout(() => {
      callback(...args);
    }, wait);
  };
}


//  /utils


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

// search
const searchBtns = document.querySelectorAll('.open-search');
const searchMenu = document.querySelector('.search-menu');
searchBtns.forEach(btn => {
  btn.onclick = () => {
    searchMenu.classList.add('active');
  }
})
const searchMenuClose = document.querySelector('.search-menu__close');
searchMenuClose.onclick = () => {
  searchMenu.classList.remove('active');
}
// /search


// favorites
body.addEventListener('click', async (e) => {
  if (e.target.closest('.fav-btn')) {
    const fav = e.target.closest('.fav-btn');
    
    e.preventDefault();
    // promise callback
    const itemId = fav.getAttribute('item-id');
    const csrf = document.querySelector("#csrf input").value;

    try {
      if (fav.classList.contains('active')) {
        const res = await PublicAPI.deleteFromFavorites(itemId);
        if (res.success) {
          showSnack('fav-removed');
          fav.classList.remove('active');
  
          if (e.target.closest('.lk-favs')) {
            e.target.closest('.product').remove();
          }
  
        } else {
          showSnack('error-snack');
        }
      } else {
        const res = await PublicAPI.addToFavorites(itemId, csrf);
        if (res.success) {
          showSnack('fav-snack');
          fav.classList.add('active');
        } else {
          showSnack('error-snack');
        }
      }
    } catch (e) {
      console.log(e, ' error')
      showSnack('error-snack');
    }

  }
})



// Add product

body.addEventListener('click', async (e) => {
  if (e.target.closest('.add-cart')) {
    const btn = e.target.closest('.add-cart');
    console.log( e.target)
    e.preventDefault();
    e.stopPropagation();
    // let productId;
    // if (btn.closest('.product')) {
      
    //   productId = btn.closest('.product').getAttribute('variant-id');
    // } else {
    //   btn.getAttribute('variant-id');
    // }
    productId = btn.dataset.variant;
    const res = await PublicAPI.addToCart(productId);
    console.log(res.success);
    if (res.success) {
      showSnack('add-success');
    } else {
      showBaseSnackWithText(res.message);
    }
  }
})

//  Add product end


// search

const searchHandler = debounce(async (event) => {
  const string = event.target.value;
  if (string.length > 2) {
    const wrapper = document.querySelector('.search-results .search-items');
    const notFound = document.querySelector('.search-not-found');
  
    const res = await PublicAPI.search(string);
    if (res) {
      notFound.classList.remove('active');
      wrapper.innerHTML = res;
    }
    if (res.trim() == '') {
      notFound.classList.add('active');
    }
  }

}, 250)

const searchField = document.querySelector('.search-top__input');

searchField.addEventListener('input', searchHandler);


// search end


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// sale modal

const saleModal = document.querySelector('.sale-modal');
setTimeout(() => {
  if (getCookie("saleModalShown")) return;
  saleModal.classList.add('active');
  changeModalBgState('enable');

  document.cookie = "saleModalShown=true; path=/; max-age=1209600";
}, 5 * 1000);