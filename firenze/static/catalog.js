(function() {
  if (document.querySelector('.slideInput')) {
    const slideInputs = document.querySelectorAll('.slideInput');

    slideInputs.forEach(slideInput => {
      const wrapper = slideInput.closest('.slideInput-wrapper');
      const minInput = wrapper.querySelector('.min');
      const maxInput = wrapper.querySelector('.max');


      const minValue = +minInput.getAttribute('data-min-value')
      const maxValue = +maxInput.getAttribute('data-max-value')
      // init slider
      noUiSlider.create(slideInput, {
        start: [minValue, maxValue],
        connect: true,
        range: {
            'min': minValue,
            'max': maxValue
        },
        step: maxValue / 100
      });
      

      // Update slider on input changes
      minInput.addEventListener('change', (e) => {
        slideInput.noUiSlider.set([e.target.value, null]);
      })
      maxInput.addEventListener('change', (e) => {
        slideInput.noUiSlider.set([null, e.target.value]);
      })

      // update inputs on slider change

      slideInput.noUiSlider.on('update', (values, handle) => {
        const value = values[handle];

        // === 0 more obviously
        if (handle === 0) {
          minInput.value = Math.round(value);
        } else {
          maxInput.value = Math.round(value);
        }
      });

    })

  }
})();


const filterBtnAccept = document.querySelector('.filter-btns__accept');
const filterSortBtnAccept = document.querySelector('#sortAccept');
const catalog = document.querySelector('.catalog');
const formParams = document.querySelector('.filter-params');
const formSort = document.querySelector('.filter-sort');
filterBtnAccept.onclick = async (e) => {
  e.preventDefault();
  const formData = new FormData(formParams);
  const sortData = new FormData(formSort);
  const page = catalog.getAttribute('current-page');
  formData.append('page', 1);

  for (let pair of sortData.entries()) {
    formData.append(pair[0], pair[1]);
  }

  const res = await PublicAPI.filter(formData);
  catalog.innerHTML = res;
}
filterSortBtnAccept.onclick = async (e) => {
  e.preventDefault();
  const formData = new FormData(formParams);
  const sortData = new FormData(formSort);
  const page = catalog.getAttribute('current-page');
  formData.append('page', 1);

  for (let pair of sortData.entries()) {
    formData.append(pair[0], pair[1]);
  }

  const res = await PublicAPI.filter(formData);
  catalog.innerHTML = res;
}

window.addEventListener('click', async (e) => {
  if (e.target.closest('.pagination__item') || e.target.closest('.pagination__btn')) {
    const item = e.target.closest('.pagination__item') || e.target.closest('.pagination__btn');

    const page = item.getAttribute('data-page');
    const formData = new FormData(formParams);
    formData.append('page', page);
    const sortData = new FormData(formSort);

    for (let pair of sortData.entries()) {
      formData.append(pair[0], pair[1]);
    }

    const res = await PublicAPI.filter(formData);
    catalog.innerHTML = res;
  }
  
})