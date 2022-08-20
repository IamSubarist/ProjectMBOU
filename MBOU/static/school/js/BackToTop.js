window.onscroll = function backToTopBtn() {
    var backToTop = document.querySelector('.backToTop');
    if(window.pageYOffset > 400){
        backToTop.classList.add('backToTop_active');
    } else {
        backToTop.classList.remove('backToTop_active');
    }
}

const scrollBtn = document.querySelector('.backToTop')

scrollBtn.onclick = () => {
    window.scrollTo(0, 0);
}