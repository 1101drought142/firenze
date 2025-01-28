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
// Date inputs

(function() {
  if (!document.querySelector('.dateInput')) return;

  const phoneInputs = document.querySelectorAll('.dateInput input');

  phoneInputs.forEach(inp => {
    const wrap = inp.closest('.dateInput');

    IMask(
      inp,
      {
        mask: Date,
        min: new Date(1920, 0, 1),
        max: new Date(2025, 0, 1),
        lazy: false
      }
    )

    inp.addEventListener('blur', () => {
      if (inp.value[inp.value.length - 1] == '_') {
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

  window.addEventListener('click', (e) => {
    let dropdown;
    let header;
    let headerContent;
    let inp;
    if (e.target.closest('.dropdown')) {
      dropdown = e.target.closest('.dropdown');
      header = dropdown.querySelector('.dropdown__header');
      headerContent = header.querySelector('span');
      inp = dropdown.querySelector('.dropdown__header-inp');
    } else { return }
    
    if (e.target.closest('.dropdown__header')) {
      const wasActive = dropdown.classList.contains('active');
      document.querySelectorAll('.dropdown').forEach(dr => dr.classList.remove('active'))
      if (wasActive) {
        dropdown.classList.remove('active');
        return;
      };
      dropdown.classList.add('active');
    }

    if (e.target.closest('.dropdown-list__item')) {
      const item = e.target.closest('.dropdown-list__item');
      
      headerContent.innerHTML = item.innerHTML;
      inp.value = item.getAttribute('data-val');
      header.setAttribute('data-val', item.getAttribute('data-val'));
    
    
      // close
      dropdown.classList.remove('active');

    }

  })

  const dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(dropdown => {
    const header = dropdown.querySelector('.dropdown__header')
    const headerContent = header.querySelector('span');
    const inp = dropdown.querySelector('.dropdown__header-inp');

    const items = dropdown.querySelectorAll('.dropdown-list__item');

    header.addEventListener('click', () => {
    })

    items.forEach(item => {
      item.addEventListener('click', () => {
      })
    })

  })

})();