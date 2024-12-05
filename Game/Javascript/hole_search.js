'use strict';

async function hole_searcher(ide, method) {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/hole_search/${ide}/${method}`);
    const json = await response.json();
    return json;
  } catch (error) {
    console.log(error);
  }
}

function removeElements(no_search, taxi, yango) {
  dialog.removeChild(taxi);
  dialog.removeChild(yango);
  dialog.removeChild(no_search);
  const close = document.createElement('button');
  close.id = 'close';
  close.textContent = 'Däsdä bääsed bois :---D';
  dialog.appendChild(close);
  close.addEventListener('click', (evt) => {
    dialog.close();
    console.log(evt + ' gliggasid hiirellä :---D midä sinä däällä deed? :-DDD');
  });
}

function addListeners (no_search, taxi, yango) {
  no_search.addEventListener('click', (evt) => {
  dialog.close();
});
  taxi.addEventListener('click', async (evt) => {
  console.log('menid sidden daxilla :--DD');
  const method = 'taxi';
  const testi = await hole_searcher(ide, method);
  console.log(testi);
});
  yango.addEventListener('click', async (evt) => {
  console.log('Yoloooo!!! :----DDD Yango on senjan lembi gulguneuvo :--DD');
  const img = document.querySelector('#spurdo');
  img.src = `/Game/images_and_other/tarkee_kuva.png?random=${Date.now()}`;
  const parag = document.querySelector('#response');
  parag.textContent = '';
  const method = 'yango';
  const result = await hole_searcher(ide, method);
  console.log(result);
  if (result.makkara === 'found') {
    parag.textContent = 'Onnegsi olgoon said maggarasi dagaisin :-DDD';
    removeElements(no_search, taxi, yango);
  } else {
    //const img = document.querySelector('#spurdo')
    img.src = `/Game/images_and_other/toinen_tarkea_kuva.png?random=${Date.now()}`;
    parag.textContent = 'Voi harmi :-D sinud ryösdeddiin :--DD';
    removeElements(no_search, taxi, yango);
  }
});

}


const dialog = document.querySelector('#search_hole');
const button1 = document.querySelector('#hole_search');

button1.addEventListener('click', (evt) => {
  dialog.showModal();
  dialog.innerHTML = `<p>Golon edsindä modal :---DDD</p>
                                <img id="spurdo" src="/Game/images_and_other/tarkee_kuva.png" alt="Tärkee kuva :-D">
                                <p id="response">Dämä on Golon edsindä :--D. Jogo mened daxilla :-D (300€) dai odad risgin Yangolla :--DDD (50€)</p>
                                <button id="search_hole_taxi">Edsi golo :---DDD daxilla</button>
                                <button id="search_hole_yango">Edsi golo :---DDD yangolla</button>
                                <button id="no_search">En edsiggään :---DDD</button>`;
  const taxi = document.querySelector('#search_hole_taxi');
  const yango = document.querySelector('#search_hole_yango');
  const no_search = document.querySelector('#no_search');
  addListeners(no_search, taxi, yango)
});