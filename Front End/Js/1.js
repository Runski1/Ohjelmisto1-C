'use strict';
const targetElem = document.body;
const container = document.createElement('div');
container.id = 'container'
targetElem.appendChild(container);

const logo = document.createElement('img');
container.appendChild(logo);
logo.src = '../img/logo.png';
const enterCont = document.createElement('div')
enterCont.id='enterGame'
targetElem.appendChild(enterCont)
const enterGame = document.createElement('button')
enterGame.innerText = 'Enter the game'
enterGame.id = 'enterGameButton';
setTimeout(() => {
    enterCont.appendChild(enterGame);
}, 1000);


