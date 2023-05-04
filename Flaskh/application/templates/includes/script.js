const Toggle = {
    showMenu() {
        document.querySelector('header').classList.toggle('active')
    },

    closeMenu() {
        document.querySelector('header').classList.remove('active')
    }
}