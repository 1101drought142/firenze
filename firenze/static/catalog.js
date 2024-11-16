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