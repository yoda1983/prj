"use strict"

let offline = document.querySelector(".offline");
let online = document.querySelector(".online");
let videocourse = document.querySelector(".videocourse");

online.addEventListener('click', openOnlinetext);
offline.addEventListener('click', openOfflinetext);
videocourse.addEventListener('click', openVideocoursetext);

function openOnlinetext (){
    online.classList.add('red_format');
    offline.classList.remove('red_format');
    videocourse.classList.remove('red_format');
    document.querySelector(".format__online").style.display = 'flex';
    document.querySelector(".format__offline").style.display = 'none';
    document.querySelector(".format__videocourse").style.display = 'none';
}

function openOfflinetext (){
    offline.classList.add('red_format');
    online.classList.remove('red_format');
    videocourse.classList.remove('red_format');
    document.querySelector(".format__offline").style.display = 'flex';
    document.querySelector(".format__online").style.display ='none';
    document.querySelector(".format__videocourse").style.display = 'none';
}

function openVideocoursetext (){
    videocourse.classList.add('red_format');
    online.classList.remove('red_format');
    offline.classList.remove('red_format');
    document.querySelector(".format__videocourse").style.display = 'flex';
    document.querySelector(".format__offline").style.display = 'none';
    document.querySelector(".format__online").style.display ='none';
    
}