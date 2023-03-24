const rangeSlider = document.querySelector('.catalog__filters-range-container')
if (rangeSlider) {
    noUiSlider.create(rangeSlider, {
        start: [0, 5000],
        connect: true,
        step: 1,
        range: {
            'min': [0],
            'max': [5000]
        }
    });
    let snapValues = [
        document.querySelector('#id_price__gt'),
        document.querySelector('#id_price__lt')
    ];
    rangeSlider.noUiSlider.on('update', (values, handle) => {
        snapValues[handle].value = values[handle].split('.')[0]
    })
}

function toggleFilters() {
    document.querySelector('.catalog__search-block-filters').classList.toggle('active')
    let filters = document.querySelector('.catalog__filters')
    let cards = document.querySelector('.catalog__cards')
    filters.classList.toggle('active')
    cards.classList.toggle('shifted')
}

