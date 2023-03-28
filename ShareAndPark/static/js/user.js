
// Показать/скрыть пароль
function togglePassword() {
    const element = event.target
    const input = element
        .closest('.modal__input-container')
        .querySelector('.modal__input')
    if (input.type === 'password') {
        input.type = 'text'
    } else {
        input.type = 'password'
    }
    element.classList.toggle('showed')
    element.classList.toggle('hidden')
}
