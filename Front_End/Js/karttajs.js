'use strict';
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
  
      setTimeout(() => {
        targetELem.classList.add('lightblueGlow');
        targetELem.classList.add('show');
      }, 600);
  
    }, 600);
  
    const targetElem = document.getElementById('enterGame');
    const mapFrame = document.createElement('div');
    mapFrame.style.width = '800px';
    mapFrame.style.height = '600px';
    targetElem.appendChild(mapFrame);
    const mapImg = document.createElement('img');
    mapFrame.appendChild(mapImg);
    mapImg.src = '../img/placeholdermap_800x600.png';
  
    /*const map =L.tileLayer('https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={accessToken}', {
      attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      minZoom: 0,
      maxZoom: 22,
      subdomains: 'abcd',
      accessToken: '<your accessToken>'*/
  }
  mainGame()