"use strict";
//!! объект первого слайдера
let slider_big = {
    0: "../static/img/slider_2.jpg",
    1: "../static/img/slider_9.jpg",
    2: "../static/img/slider_4.jpg",
    3: "../static/img/slider_7.jpg",
    4: "../static/img/slider_6.jpg",
    5: "../static/img/slider_8.jpg",
    length: 6,
    number: 1,
    chek_blocks: document.getElementsByClassName("about-itec__online-tour-circle"),
    //!! функция парамерта ссылки
    begin() {
        let a = null;
        if (this.number == 0) {
            a = this.number;
            return this[a];
        } else if (this.number < 0) {
            this.number = this.number + this.length;
            a = this.number;
            return this[a];
        } else if (this.number == this.length) {
            this.number = this.number - this.length;
            a = this.number;
            return this[a];
        } else {
            a = this.number;
            return this[a];
        }
    },
};
//!! события на полоски
for (let value of slider_big.chek_blocks) {
    document.getElementById(value.id).addEventListener("click", {
        handleEvent: chekFunk,
        obj: slider_big,
        conteiner: document.querySelector(".about-itec__online-tour"),
    });
}

//!! функция на полоски
function chekFunk(event) {
    let obj = this.obj;
    let i = 0;
    let target = event.target;
    let conteiner = this.conteiner;
    for (let value of obj.chek_blocks) {
        if (value == target) {
            break;
        } else {
            i++;
        }
    }
    obj.number = i;
    for (let value of obj.chek_blocks) {
        if (value == target) {
            document.getElementById(value.id).style.background = "#ffffff";
        } else {
            document.getElementById(value.id).style.background = "none";
        }
    }
    let img = `url(${obj[i]})`;
    conteiner.style.background = img;
}


//!! события на стрелки
document.querySelector(".online-tour__arrow-wrapper-right").addEventListener("click", {
    handleEvent:()=> sliderGo("right",slider_big,document.querySelector("#slider-block")),
});
document.querySelector(".online-tour__arrow-wrapper-left").addEventListener("click", {
    handleEvent:()=> sliderGo("left",slider_big,document.querySelector("#slider-block")),
});

//!! универсальная функция на слайдер с полосками
function sliderGo(fn = this.fn, object = this.obj, containerSlide = this.conteiner) {
    let obj = object;
    let container = containerSlide;
    if (fn == "left") {
        obj.number--;
        let img = `url(${obj.begin()})`;
        container.style.background = img;
    } else {
        obj.number++;
        let img = `url(${obj.begin()})`;
        container.style.background = img;
    }

    if (obj.chek_blocks != undefined) {
        let i = 0;
        for (let value of obj.chek_blocks) {
            if (i == obj.number) {
                document.getElementById(value.id).style.background = "#ffffff";
                i++;
            } else {
                document.getElementById(value.id).style.background = "none";
                i++;
            }
        }
    }
}

sliderGo("left", slider_big, document.querySelector("#slider-block"))
