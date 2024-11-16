// Phone inputs

(function() {
  if (!document.querySelector('.phoneInput')) return;

  const phoneInputs = document.querySelectorAll('.phoneInput input');

  phoneInputs.forEach(inp => {
    const wrap = inp.closest('.phoneInput');

    IMask(
      inp,
      {
        mask: '+{7 (000) 000 00-00'
      }
    )

    inp.addEventListener('blur', () => {
      if (inp.value.length < 18 && (!inp.getAttribute('required') && inp.value.length > 0)) {
        wrap.classList.add('error');
      }
    })
    inp.addEventListener('focus', () => {
      wrap.classList.remove('error');
    })
  });

})();

(function() {
  if (!document.querySelector('.mailInput')) return;

  const mailInput = document.querySelectorAll('.mailInput input');
  const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  mailInput.forEach(inp => {
    const wrap = inp.closest('.mailInput');

    inp.addEventListener('blur', () => {
      if (!re.test(inp.value)) {
        wrap.classList.add('error');
      }
    });
    inp.addEventListener('focus', () => {
      wrap.classList.remove('error');
    })

  })
})();


// dropdowns

(function() {

  const dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(dropdown => {
    const header = dropdown.querySelector('.dropdown__header')
    const headerContent = header.querySelector('span');
    const inp = dropdown.querySelector('.dropdown__header-inp');

    const items = dropdown.querySelectorAll('.dropdown-list__item');

    header.addEventListener('click', () => {
      const wasActive = dropdown.classList.contains('active');
      dropdowns.forEach(dr => dr.classList.remove('active'))
      if (wasActive) {
        dropdown.classList.remove('active');
        return;
      };
      dropdown.classList.add('active');
    })

    items.forEach(item => {
      item.addEventListener('click', () => {
        headerContent.innerHTML = item.innerHTML;
        inp.value = item.getAttribute('data-val');
        header.setAttribute('data-val', item.getAttribute('data-val'));


        // close
        dropdown.classList.remove('active');
      })
    })

  })

})();