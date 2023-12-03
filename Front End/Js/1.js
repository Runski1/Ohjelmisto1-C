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
    logo.classList.add('cyanGlow')
    container.appendChild(logo);

    // Create container for the "Enter the game" button
    const startButtonCont = document.createElement('div');
    startButtonCont.id = 'startButtonCont';
    targetElem.appendChild(startButtonCont);

    // Create and add the "Enter the game" button
    const enterGame = document.createElement('button');
    enterGame.innerText = 'Start The Game';
    enterGame.id = 'enterGameButton';
    enterGame.classList.add('hide');

    startButtonCont.appendChild(enterGame);

    // Add the 'show' class with a transition when the DOM is loaded
    document.addEventListener("DOMContentLoaded", function () {


        // Triggering the reflow/repaint before adding the 'show' class
        enterGameButton.offsetHeight;

        // Add a class to the button to trigger the transition
        enterGameButton.classList.add("magentaGlow");
        enterGameButton.classList.add("show");
    });
}


function selectGame() {
    setTimeout(() => {
        const targetElem = document.getElementById('startButtonCont');
        targetElem.innerHTML = '';
        // Create and add the "New game" Form
        const newGameForm = document.createElement('form');
        targetElem.appendChild(newGameForm);

        // Create input field
        const inputNewGame = document.createElement('input');
        inputNewGame.setAttribute('type', 'text');
        inputNewGame.setAttribute('id', 'gameName');
        inputNewGame.setAttribute('name', 'gameName');
        inputNewGame.classList.add('form');
        inputNewGame.classList.add('hide')
        inputNewGame.placeholder = 'Enter New/Saved Game Name';

        // Add input to form
        newGameForm.appendChild(inputNewGame);

        // Create submit button
        const inputButton = document.createElement("button");
        inputButton.setAttribute('type', 'submit');
        targetElem.appendChild(inputButton);
        inputButton.classList.add('hide');
        inputButton.id = 'selectGame'
        inputButton.style.width = '2rem';
        inputButton.innerText = '>';
        // Add the 'show' class with a transition
        setTimeout(() => {
            inputButton.classList.add('magentaGlow');
            inputNewGame.classList.add('magentaGlow');
            inputButton.classList.add('show');
            inputNewGame.classList.add('show');

            // Now that the button is created, add the event listener
            /********MAIN GAME WILL START*********/
            document.getElementById('selectGame').addEventListener('click', addPlayers);
        }, 0); // Use 0 for the next available frame
    }, 600);
}

async function addPlayers() {
    const gameName = document.getElementById('gameName');
    const gameNameRequest =gameName.value;
    try{
        const gameNameResponse = await fetch(`https://127.0.0.1:3000/game_files/savedgames/${gameNameRequest}`);


    }    setTimeout(() => {
        const targetElem = document.getElementById('startButtonCont');
        targetElem.innerHTML = '';

    }, 600);
}

function mainGame() {
    setTimeout(() => {

        const targetELem = document.getElementById('startButtonCont');
        targetELem.classList.add('mainGameContainer');
        // Clear the body content
        targetELem.innerHTML = '';

        // Set the body height to 100%
        document.body.style.height = '100%';
        targetELem.style.width = '50rem';
        targetELem.style.height = '37.5rem';
        targetELem.style.border = '1px solid #19caca';

        setTimeout(() => {
            targetELem.classList.add('lightblueGlow')
            targetELem.classList.add("show");
        }, 600);

    }, 600);

}

/*********************** PROGRAM STARTS FROM HERE**********************/
startScreen();

document.getElementById("enterGameButton").addEventListener('click', selectGame);


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
