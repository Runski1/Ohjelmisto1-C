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
  logo.classList.add('cyanGlow');
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
  document.addEventListener('DOMContentLoaded', function() {

    // Triggering the reflow/repaint before adding the 'show' class
    enterGame.offsetHeight;

    // Add a class to the button to trigger the transition
    enterGame.classList.add('magentaGlow');
    enterGame.classList.add('show');
  });
}

function selectGame() {
setTimeout(() => {
    const targetElem = document.getElementById('startButtonCont');
    targetElem.innerHTML = '';

    // Create and add the "New game" Form
    const newGameForm = document.createElement('form');
    newGameForm.id = 'newGameForm';
    newGameForm.classList.add('hide')
    targetElem.appendChild(newGameForm);

    // Create input field for game name
    const inputNewGame = document.createElement('input');
    inputNewGame.setAttribute('type', 'text');
    inputNewGame.setAttribute('id', 'gameName');
    inputNewGame.setAttribute('name', 'gameName');
    inputNewGame.setAttribute('action', '');
    inputNewGame.classList.add('form');
    inputNewGame.placeholder = 'Enter New/Saved Game Name';

    // Add input to form
    newGameForm.appendChild(inputNewGame);

    // Create submit button
    const inputButton = document.createElement('button');
    inputButton.setAttribute('type', 'submit');
    targetElem.appendChild(inputButton);
inputButton.classList.add('hide');
    inputButton.id = 'selectGame';
    inputButton.style.width = '2rem';
    inputButton.innerText = '>';

    // Add the 'show' class with a transition
    setTimeout(() => {
        newGameForm.classList.add('magentaGlow', 'show')
        inputButton.classList.add('show');


      // Add event listener for "Enter" key press on the input field
      inputNewGame.addEventListener('keypress',  function (event) {
        // If the user presses the "Enter" key on the keyboard
        if (event.key === 'Enter') {
          // Cancel the default action, if needed
          event.preventDefault();
          // Trigger the button element with a click
          inputButton.click();

        }
      });

      // Add event listener for button click
      inputButton.addEventListener('click', function (event) {
        event.preventDefault();
        addPlayers();
      });
    }, 0);
}, 300);
}

async function addPlayers() {

  // gets value of entered game name
  const gameName = document.getElementById('gameName');
  const gameNameRequest = gameName.value;
  // makes json request from Flask-server

  const gameNameResponse = await fetch(
      `http://127.0.0.1:3000/get_saveGame/${gameNameRequest}`);
  const jsonData = await gameNameResponse.json();
  console.log(jsonData);
  // if saved game not found makes new game and updates startButtonCont

  if (jsonData.gameName == 'not found') {

    //add new player form for information max player (ammount:4)!!!!
    //if you want to add more players max player limit needed from server
    //for (jsonData.playerLimit.value);

    const playerList = [];

    //add player name input form
    for (let i = 0; i < 3; i++) {
      const targetElem = document.getElementById('newGameForm');
      // Create input field
      const inputNewPlayer = document.createElement('input');
      inputNewPlayer.setAttribute('type', 'text');
      inputNewPlayer.setAttribute('id', `player${i + 1}`);
      inputNewPlayer.classList.add('form');
      //inputNewPlayer.classList.add('hide');
      inputNewPlayer.placeholder = `Player ${i + 1}`;
      targetElem.appendChild(inputNewPlayer);
      playerList.push(inputNewPlayer);

    }
    // adds submit button to player name form
    const inputButton = document.createElement('button');
    inputButton.setAttribute('type', 'submit');
    gameName.appendChild(inputButton);
    //inputButton.classList.add('hide');
    inputButton.id = 'selectGame';
    inputButton.style.width = '2rem';
    inputButton.innerText = '>';
    setTimeout(() => {
      gameName.classList.add('show');
      gameName.classList.add('magentaGlow');
    }, 600);

    // append new player names to new save game
    const playerName1 = playerList[0];
    const playerName2 = playerList[1];

    const playerNameResponse = await fetch(
        `http://127.0.0.1:3000//add_player/${gameName}/${playerName1}/${playerName2}`);
    const jsonData = await playerNameResponse.json();
    console.log(jsonData);
    mainGame();
    /*********************** MAINGAME STARTS FROM HERE**********************/
  } else {
    document.getElementById('selectGame').addEventListener('click', mainGame);
  }
}

/*async function playerData {

}*/

function mainGame() {
  setTimeout(() => {

    const targetELem = document.getElementById('startButtonCont');
    targetELem.classList.add('mainGameContainer');
    // Clear the gamecontainer content
    targetELem.innerHTML = '';

    // Set the body height to 100%
    document.body.style.height = '100%';
    // kartta on 800x600 = 50remx37.5rem
    targetELem.style.width = '70rem';
    targetELem.style.height = '47.5rem';
    targetELem.style.border = '1px solid #19caca';
  const targetElem = document.getElementById('startButtonCont');
    const mapFrame = document.createElement('div');
    mapFrame.style.width = '800';
    mapFrame.style.height = '600';
    const mapImg = document.createElement('img');
    mapImg.src = '../img/placeholdermap_800x600.png';
    mapFrame.appendChild(mapImg);
    targetElem.appendChild(mapFrame);
    mapFrame.classList.add('hide');
    setTimeout(() => {
      targetELem.classList.add('lightblueGlow');
      targetELem.classList.add('show');
      mapFrame.classList.add('show');
    }, 600);
  }, 600);



  /*const map =L.tileLayer('https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={accessToken}', {
	attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	minZoom: 0,
	maxZoom: 22,
	subdomains: 'abcd',
	accessToken: '<your accessToken>'*/
}

/*********************** PROGRAM STARTS FROM HERE**********************/
startScreen();

document.getElementById('enterGameButton').
    addEventListener('click', selectGame);

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
