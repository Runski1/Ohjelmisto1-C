'use strict';
const targetElem = document.body;
const container = document.createElement('div');
container.id = 'container'
targetElem.appendChild(container);

const logo = document.createElement('img');

logo.src = '../img/logo.png';
const enterCont = document.createElement('div')
enterCont.id='enterGame'
targetElem.appendChild(enterCont)
const enterGame = document.createElement('button')
enterGame.innerText = 'Enter the game'
enterGame.id = 'enterGameButton';
enterGame.classList.add('button')
setTimeout(() => {
    enterCont.appendChild(enterGame,container.appendChild(logo));
}, 1000);



//**const video_Background = document.createElement('video');
// video_Background.id = 'background-video';
// video_Background.autoplay.
// document.addEventListener("DOMContentLoaded", function () {
//         // Create video element
//         let video = document.createElement("video");
//         video.id = "background-video";
//         video.autoplay = true;
//         video.loop = true;
//         video.muted = true;
//         video.src = "https://assets.codepen.io/6093409/river.mp4";
//         video.type = "video/mp4";
//
//         // Set poster attribute
//         video.poster = "https://assets.codepen.io/6093409/river.jpg";
//
//         // Append video to the body
//         document.body.appendChild(video);
//     });