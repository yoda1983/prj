'use strict'

let burger = document.getElementById('burger');
burger.addEventListener('click', openNavburger);

function openNavburger(){
    document.querySelector('.header__burger').classList.toggle('active');
    document.querySelector('.header__menu').classList.toggle('flex__menu'); 
    document.querySelector('.container__menu-mobile').classList.toggle('open'); 
    document.getElementById('hidden-menu').toggleAttribute('hidden');
    document.getElementById('content').toggleAttribute('hidden');
    document.getElementById('body').classList.toggle('lock');
    document.getElementById('menu__logo').toggleAttribute('hidden');
    let elem = document.querySelector('#menu__logo-mobile')
        
    if (elem.style.justifyContent == ''|| elem.style.justifyContent =='space-between'){

        elem.style = " justify-content:flex-end;"
    } 
    else if(elem.style.justifyContent = "flex-end"){
        elem.style = "justify-content: space-between;"
    }
    
    console.log(elem.style)
}

let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);
window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
});


const conteinerForButton=document.querySelector(".container__form-window")
    conteinerForButton.style.overflow="scroll"

const okButton=document.querySelector(".form-window__button")
const htmlElem=document.documentElement


okButton===null?htmlElem.style.overflow="scroll":htmlElem.style.overflow="hidden"
