let navBtn = document.getElementById('boton-nav')
let aside = document.getElementById('aside')
let navUl = document.getElementById('nav-ul')
let closeNav = document.getElementById('close-nav')

navBtn.addEventListener('click', () => {
    navBtn.style.display = 'none'
    closeNav.style.display = 'block'
    aside.style.width = '200px'
    navUl.style.display = 'flex'
    navUl.style.flexDirection = 'column'
    navUl.style.fontSize = '12px'
})

closeNav.addEventListener('click', () => {
    navBtn.style.display = 'block'
    closeNav.style.display = 'none'
    aside.style.width = '40px'
    navUl.style.display = 'none'
    navUl.style.flexDirection = 'column'
    navUl.style.fontSize = '12px'
})