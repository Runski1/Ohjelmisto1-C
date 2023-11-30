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


