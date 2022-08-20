window.onscroll = function header__scrollBtn() {
    var header__scroll = document.querySelector('.header__scroll');
    if(window.pageYOffset > 330){
        header__scroll.classList.add('header__scroll_active');
    } else {
        header__scroll.classList.remove('header__scroll_active');
    }
}