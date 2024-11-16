(function() {
  const tabBtns = document.querySelectorAll('.tabs__item');

  tabBtns.forEach(btn => {
    // Имя группы контента и кнопок
    const baseName = btn.getAttribute('data-tab-base');
    // Имя конкретной кнопки для связи с контентом
    const tabValue = btn.getAttribute('data-tab-val');

    const allGroupContent = document.querySelectorAll(`.tab-content[data-tab-base="${baseName}"]`)
    const allGroupBtns = document.querySelectorAll(`.tabs__item[data-tab-base="${baseName}"]`)
    btn.onclick = () => {
      // Убираем активность со всех кнопок группы
      allGroupBtns.forEach(groupBtn => groupBtn.classList.remove('active'));
      // Обработка случая с кнопкой, включающей все табы сразу
      if (btn.classList.contains('tabs__item--all')) {
        allGroupContent.forEach(content => content.classList.add('active'));
        btn.classList.add('active');
        return;
      }


      // Убираем активность со всего контента
      allGroupContent.forEach(content => content.classList.remove('active'));
      // Ставим активность на контент, соответствующий value кнопки
      const targetContent = document.querySelector(`.tab-content[data-tab-val="${tabValue}"][data-tab-base="${baseName}"]`);
      targetContent.classList.add('active');
      // Ставим активность на кнопку
      btn.classList.add('active');
    }


  })


})();