'use strict';
const targetElem = document.body;
const container = document.createElement('div');
container.id = 'container'
//add containerin
targetElem.appendChild(container);
const logo = document.createElement('img');
logo.src = '../img/logo.png';
//Add LOST TESTAMENT
container.appendChild(logo)
const enterCont = document.createElement('div')
enterCont.id='enterGame'
//add enter game buttons container
targetElem.appendChild(enterCont)
const enterGame = document.createElement('button')
enterGame.innerText = 'Enter the game'
enterGame.id = 'enterGameButton';
enterGame.classList.add('button')
//adds enter game  button
enterCont.appendChild(enterGame,)


document.addEventListener("DOMContentLoaded", function () {
    let enterGameButton = document.getElementById("enterGameButton");

    // Triggering the reflow/repaint before adding the 'show' class
    enterGameButton.offsetHeight;

    // Add a class to the button to trigger the transition
    enterGameButton.classList.add("show");
});

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
