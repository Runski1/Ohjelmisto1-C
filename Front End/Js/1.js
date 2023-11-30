'use strict';

function startScreen() {
    const targetElem = document.body;

    // Create container for the start screen
    const container = document.createElement('div');
    container.id = 'container';
    targetElem.appendChild(container);

    // Create and add the logo
    const logo = document.createElement('img');
    logo.src = '../img/logo.png';
    logo.id = 'logo';
    container.appendChild(logo);

    // Create container for the "Enter the game" button
    const enterCont = document.createElement('div');
    enterCont.id = 'enterGame';
    targetElem.appendChild(enterCont);

    // Create and add the "Enter the game" button
    const enterGame = document.createElement('button');
    enterGame.innerText = 'Enter the game';
    enterGame.id = 'enterGameButton';
    enterGame.classList.add('button');
    enterCont.appendChild(enterGame);

    // Add the 'show' class with a transition when the DOM is loaded
    document.addEventListener("DOMContentLoaded", function () {
        let enterGameButton = document.getElementById("enterGameButton");

        // Triggering the reflow/repaint before adding the 'show' class
        enterGameButton.offsetHeight;

        // Add a class to the button to trigger the transition
        enterGameButton.classList.add("show");
    });
}


function selectGame() {
    // Function to transition to the new game screen

    setTimeout(() => {
        document.body.innerHTML = ''; // Clear the body content
        const targetElem = document.body;

        // Create and add the "New game" button
        const newGame = document.createElement('button');
        newGame.innerText = 'New game';
        newGame.classList.add('button');
        newGame.style.width = '40rem';
        newGame.style.height = '6rem';
        newGame.style.fontSize = '2rem';
        targetElem.appendChild(newGame);
        // Add the 'show' class with a transition
        setTimeout(() => {
            newGame.classList.add('show');
        }, 0); // Use 0 for the next available frame
    }, 600);
}


// Call the startScreen function to initialize the start screen
startScreen();

document.getElementById("enterGameButton").addEventListener("click", selectGame);

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
