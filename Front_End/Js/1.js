'use strict';

import {cityData} from "./cities.js";

function startScreen() {
    const targetElem = document.body;

    // Create container for the start screen
    const logoContainer = document.createElement('div');
    logoContainer.id = 'logoContainer';
    targetElem.appendChild(logoContainer);

    // Create and add the logo
    const logo = document.createElement('img');
    logo.src = '../img/logo.png';
    logo.id = 'logo';
    logo.classList.add('cyanGlow');
    logoContainer.appendChild(logo);

    // Create container for the "Enter the game" button
    const gameContainer = document.createElement('div');
    gameContainer.id = 'gameContainer';
    targetElem.appendChild(gameContainer);

    // Create and add the "Enter the game" button
    const enterGame = document.createElement('button');
    enterGame.innerText = 'Start The Game';
    enterGame.id = 'enterGameButton';
    enterGame.classList.add('hide');

    gameContainer.appendChild(enterGame);

    // Add the 'show' class with a transition when the DOM is loaded
    document.addEventListener('DOMContentLoaded', function () {

        // Triggering the reflow/repaint before adding the 'show' class
        enterGame.offsetHeight;

        // Add a class to the button to trigger the transition
        enterGame.classList.add('magentaGlow');
        enterGame.classList.add('show');
    });
}

async function selectGame() {
    setTimeout(() => {
        const targetElem = document.getElementById('gameContainer');
        targetElem.innerHTML = '';

        // Create and add the "New game" Form
        const newGameForm = document.createElement('form');
        newGameForm.id = 'newGameForm';
        newGameForm.classList.add('hide');
        targetElem.appendChild(newGameForm);

        // Create input field for game name
        const inputNewGame = document.createElement('input');
        inputNewGame.type = 'text';
        inputNewGame.id = 'gameName';
        inputNewGame.name = 'gameName';
        inputNewGame.action = '';
        inputNewGame.classList.add('form');
        inputNewGame.placeholder = 'Enter New/Saved Game Name';

        // Add input to form
        newGameForm.appendChild(inputNewGame);

        // Create submit button
        const inputButton = document.createElement('button');
        inputButton.type = 'submit';
        targetElem.appendChild(inputButton);
        inputButton.classList.add('hide');
        inputButton.id = 'selectGame';
        inputButton.style.width = '2rem';
        inputButton.innerText = '>';

        // Add the 'show' class with a transition
        setTimeout(() => {
            newGameForm.classList.add('magentaGlow', 'show');
            inputButton.classList.add('show');

            // Add event listener for "Enter" key press on the input field
            inputNewGame.addEventListener('keypress', function (event) {
                if (event.key === 'Enter') {
                    event.preventDefault();
                    inputButton.click();
                }
            });

            // Add event listener for button click
            inputButton.addEventListener('click', async function (event) {
                event.preventDefault();
                const gameName = document.getElementById('gameName').value;
                const savedGameData = await get_saveGame(gameName);

                if (savedGameData.gameName === null) {
                    setTimeout(() => {
                        // If the saved game is not found, create a new game and update gameContainer

                        const gameContainer = document.getElementById('gameContainer');
                        gameContainer.innerHTML = '';

                        const newGameForm = document.createElement('form');
                        newGameForm.classList.add('hide');
                        newGameForm.style.display = 'flex';
                        gameContainer.appendChild(newGameForm);

                        const playerList = [];

                        for (let i = 0; i < 2; i++) {
                            const inputNewPlayer = document.createElement('input');
                            inputNewPlayer.type = 'text';
                            inputNewPlayer.id = `player${i + 1}`;
                            inputNewPlayer.classList.add('form');
                            inputNewPlayer.placeholder = `Player ${i + 1}`;
                            newGameForm.appendChild(inputNewPlayer);
                            playerList.push(inputNewPlayer);
                        }

                        const inputButton = document.createElement('button');
                        inputButton.type = 'submit';
                        gameContainer.appendChild(inputButton);
                        inputButton.classList.add('hide');
                        inputButton.id = 'addPlayer';

                        inputButton.style.width = '2rem';
                        inputButton.innerText = '>';

                        setTimeout(() => {
                            inputButton.classList.add('show');
                            newGameForm.classList.add('show');
                            newGameForm.classList.add('magentaGlow');
                        }, 200);
                        newGameForm.addEventListener('keypress', function (event) {
                            if (event.key === 'Enter') {
                                event.preventDefault();
                                inputButton.click();
                            }
                        });
                        inputButton.addEventListener('click', async function (event) {
                            event.preventDefault();
                            const playerName1 = document.getElementById('player1').value;
                            const playerName2 = document.getElementById('player2').value;
                            // add players to savegame
                            await playerSaveData(gameName, playerName1, playerName2);
                            await mainGame(gameName);

                        });
                    }, 400);
                } else {

                    await mainGame(gameName);

                }

            });
        }, 200);
    }, 300);
}

async function get_saveGame(gameName) {
    // makes json request from Flask-server

    const gameNameResponse = await fetch(
        `http://127.0.0.2:3000/get_saveGame/${gameName}`);
    const jsonData = await gameNameResponse.json();
    console.log(jsonData)
    return jsonData;
}

async function playerSaveData(gameName, playerName1, playerName2) {
    const addPlayerResponse = await fetch(
        `http://127.0.0.2:3000//add_player/${gameName}/${playerName1}/${playerName2}`);
    const jsonData = await addPlayerResponse.json();
    //console.log('saved games list:', jsonData.gameName);
    //console.log('pelaaja1', jsonData.players.player2.player_name);
    //palauttaa pelin nimen jsonData.game.game_name);
}

//asd
function mainGame(gameName) {

    setTimeout(() => {

        const gameContainer = document.getElementById('gameContainer');
        // Clear the gamecontainer content
        gameContainer.innerHTML = '';

        // Set the body height to 100%
        document.body.style.height = '100%';
        gameContainer.classList.add('mainGame');

        //gameContainer.style.border = '1px solid #19caca';

        //make map // map is 800x600 = 50rem x 37.5rem

        const mapFrame = document.createElement('div');
        mapFrame.setAttribute('id', 'map');
        gameContainer.appendChild(mapFrame);
        mapFrame.classList.add('map');
        mapFrame.classList.add('hide');
        const accessToken = 'c6moPjpSN7QLOooqQRQkhGSswG714yj1foLNEIYWMqAcvVJVqx1LFPDqpl9tCvet';
        const map = L.map('map').setView([50.1103, 30.5697], 3);
        L.tileLayer(
            `https://tile.jawg.io/jawg-dark/{z}/{x}/{y}.png?access-token=${accessToken}`, {
                attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank" class="jawg-attrib">&copy; <b>Jawg</b>Maps</a> | <a href="https://www.openstreetmap.org/copyright" title="OpenStreetMap is open data licensed under ODbL" target="_blank" class="osm-attrib">&copy; OSM contributors</a>',
                maxZoom: 22
            }
        ).addTo(map);
        // Adding different markers
        let greenMarker = new L.Icon({
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [12, 20],
            iconAnchor: [12, 20],
            popupAnchor: [-5, -15],
            shadowSize: [20, 20]
        });
        let greyMarker = new L.Icon({
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-grey.png',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [12, 20],
            iconAnchor: [12, 20],
            popupAnchor: [-5, -15],
            shadowSize: [20, 20]
        });
        let redMarker = new L.Icon({
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [12, 20],
            iconAnchor: [12, 20],
            popupAnchor: [-5, -15],
            shadowSize: [20, 20]
        });
       


        //gameContainer.appendChild(uiCont);

        // add player action buttons


        const sideBar = document.createElement('div');
        gameContainer.appendChild(sideBar);
        sideBar.classList.add('sideBar');
        sideBar.classList.add('hide')
        const infoCont = document.createElement('div');

        infoCont.classList.add('infoContainer');
        const nameCont = document.createElement('div');
        nameCont.classList.add('nameContainer');

        const flyButton = document.createElement('button');
        const hikeButton = document.createElement('button');
        const sailButton = document.createElement('button');
        const searchButton = document.createElement('button');
        const currentPlayer = document.createElement('p');
        const currentPlayerName = document.createElement('p');
        currentPlayer.classList.add('staticCurrentPlayer');
        const PlayerData = document.createElement('p');

        //console.log('p1', get_saveGame(gameName).players.player_name.player1, 'p2',
        //get_saveGame(gameName).players.player_name.player2);
        currentPlayer.textContent = `Current player:`;

        async function printPlayername(selectedButton) {

            const gameState = await get_saveGame(gameName);
            const player1 = gameState.players.player1;
            const player2 = gameState.players.player2;
            let currentPlayer
            if (gameState.game.round_counter % 2 == 1) {
                currentPlayer = player2
            } else {
                currentPlayer = player1
            }
            currentPlayerName.textContent = currentPlayer.screen_name;
            PlayerData.textContent = currentPlayer.current_pp + ' PP';

            // First we unpack cities in range in three arrays
            let flyCities = [];
            let hikeCities = [];
            let sailCities = [];
            for (let flyCity of currentPlayer.cities_in_range.fly) {
                flyCities.push(flyCity[0]);
            }
            for (let hikeCity of currentPlayer.cities_in_range.hike) {
                hikeCities.push(hikeCity[0]);
            }
            for (let sailCity of currentPlayer.cities_in_range.sail) {
                sailCities.push(sailCity[0]);
            }
            console.log('These are cities to hike', hikeCities);
            console.log('these are cities to fly', flyCities);
            console.log('these are cities to sail', sailCities);
            console.log('citydata', cityData)
            // Here we render all markers on map
            for (let city of cityData) {
                if (selectedButton === hikeButton) {
                    if (hikeCities.includes(Number(city.id))) { // city.id is string by default
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: redMarker}).addTo(map);
                        marker.bindPopup(city.name);
                        console.log('hike')
                    } else {
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: greyMarker}).addTo(map);
                    }
                } else if (selectedButton === sailButton) {
                    if (sailCities.includes(Number(city.id))) { // city.id is string by default
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: redMarker}).addTo(map);
                        marker.bindPopup(city.name);
                        console.log('sail');
                    } else {
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: greyMarker}).addTo(map);
                    }
                } else {
                    if (flyCities.includes(Number(city.id))) { // city.id is string by default
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: redMarker}).addTo(map);
                        marker.bindPopup(city.name);
                        console.log('fly');
                    } else {
                        let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: greyMarker}).addTo(map);
                    }
                }
            }


        }


        


        flyButton.classList.add('actionButtons');
        hikeButton.classList.add('actionButtons');
        sailButton.classList.add('actionButtons');
        searchButton.classList.add('workButton');


        const plane = document.createElement('img');
        const walk = document.createElement('img');
        const ship = document.createElement('img');

        plane.src = '../img/plane_cyan.png';
        walk.src = '../img/walking_cyan.png';
        ship.src = '../img/ship_cyan.png';

        flyButton.appendChild(plane);
        hikeButton.appendChild(walk);
        sailButton.appendChild(ship);

        plane.classList.add('icon')
        walk.classList.add('icon')
        ship.classList.add('icon')
        searchButton.innerHTML = '$&ensp;&ensp;&ensp;&ensp;work&ensp;&ensp;&ensp;&ensp;$';


        sideBar.appendChild(flyButton);
        sideBar.appendChild(hikeButton);
        sideBar.appendChild(sailButton);
        sideBar.appendChild(searchButton);
        sideBar.appendChild(infoCont);
        infoCont.appendChild(nameCont)
        nameCont.appendChild(currentPlayer);
        nameCont.appendChild(currentPlayerName);
        infoCont.appendChild(PlayerData);

        function handleButtonClick(selectedButton, otherButton1, otherButton2) {
            selectedButton.classList.add('selected');
            otherButton1.classList.remove('selected');
            otherButton2.classList.remove('selected');
        }

        flyButton.addEventListener("click", function () {
            handleButtonClick(flyButton, hikeButton, sailButton);
            printPlayername(flyButton);
        });

        hikeButton.addEventListener("click", function () {
            handleButtonClick(hikeButton, flyButton, sailButton);
            printPlayername(hikeButton);
        });

        sailButton.addEventListener("click", function () {
            handleButtonClick(sailButton, hikeButton, flyButton);
            printPlayername(sailButton);
        });

        flyButton.click();
        setTimeout(() => {
            sideBar.classList.add('show')
            gameContainer.classList.add('lightblueGlow');
            gameContainer.classList.add('show');
            mapFrame.classList.add('show');
        }, 600);

        /*const map =L.tileLayer('https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={accessToken}', {
     attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
     minZoom: 0,
     maxZoom: 22,
     subdomains: 'abcd',
     accessToken: '<your accessToken>'*/
    }, 600);


}

/*********************** PROGRAM STARTS FROM HERE**********************/
startScreen();
document.getElementById('enterGameButton').addEventListener('click', selectGame);

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
