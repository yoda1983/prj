'use strict'

let elements = document.querySelectorAll('.about__form-button')

for (let i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', modelWindow);
}

//функция возвращает имя курса в блоке
function NameCurse(element) {
  const eventBlock = element
  const BlockColiction = eventBlock.parentNode.parentNode.children
  let NameCurse = null
  for (const blockColictionElement of BlockColiction) {
    if (blockColictionElement.className == "about__title") {
      NameCurse = blockColictionElement.innerHTML.trim()
    }
  }
  if (element.className == "english__button") {
    NameCurse = document.querySelector(".english__title").innerHTML.trim()
  }
  return NameCurse
}

//писал костыли на костыли
function modelWindow(event) {
  let NameCurs = NameCurse(event.target)
  //вставляем имя курса в всплывающий блок
  let FormNameCourse = document.querySelector('.form-application__name-course')
  let BlockedDiv = document.querySelector('.choice__courses')
  FormNameCourse.innerHTML = NameCurs
  BlockedDiv.value = NameCurs
  //получаем форму всплывающего блока для назначения параметра 'name'
  let form = document.querySelector(".form-application__form-wrapper").parentElement
  form.name = NameCurs
  document.documentElement.style.overflow="hidden"
  document.querySelector('.container__form-application').style.display = 'block';
  document.querySelector('.container__form-application').style.overflow='scroll';
}

document.querySelector('.english__button').addEventListener('click', modelWindow)

function fn(e) {
  if (e.target.id == 'form_app') {
    console.log('delete')
    document.documentElement.style.overflow="auto"
    document.querySelector('.container__form-application').style.overflow='hidden';
    form_app.style.display = 'none';
  }
}

let form_app = document.getElementById('form_app');
form_app.addEventListener('click', fn)


let crossElem = document.querySelector('.form-application__cross')

crossElem.addEventListener('click',function cross(){
  document.documentElement.style.overflow="scroll"
  form_app.style.display = 'none';
})