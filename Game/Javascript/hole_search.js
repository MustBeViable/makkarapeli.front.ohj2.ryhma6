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

async function makkaras_stolen(ide) {

  try {
    const response = await fetch(`http://127.0.0.1:5000/makkaras_stolen/${ide}`);
    const json = await response.json();
    console.log(json)
    const result = json.makkara
    console.log('juu')
    console.log(result)
    return result;
  } catch (error) {
    console.log(error);
  }
}


async function removeElements(no_search, taxi, yango, dialog_hole_search, ide) {
  console.log(dialog_hole_search)
  dialog_hole_search.removeChild(taxi);
  dialog_hole_search.removeChild(yango);
  dialog_hole_search.removeChild(no_search);
  const close = document.createElement('button');
  close.id = 'close';
  close.textContent = 'Däsdä bääsed bois :---D';
  dialog_hole_search.appendChild(close);
  close.addEventListener('click', (evt) => {
    dialog_hole_search.close();
    console.log(evt + ' gliggasid hiirellä :---D midä sinä däällä deed? :-DDD');
  });
}

function addListeners(no_search, taxi, yango, dialog_hole_search, ide) {
  no_search.addEventListener('click', (evt) => {
    dialog_hole_search.close();
  });
  taxi.addEventListener('click', async (evt) => {
    console.log('menid sidden daxilla :--DD');
    const method = 'taxi';
    await hole_searcher(ide, method);
    const result = await hole_searcher(ide, method);
    console.log(result)
    const parag = document.querySelector('#response');
    parag.textContent = 'Onnegsi olgoon said maggarasi dagaisin :-DDD';
    await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
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
      await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
    } else {
      //const img = document.querySelector('#spurdo')
      img.src = `/Game/images_and_other/toinen_tarkea_kuva.png?random=${Date.now()}`;
      parag.textContent = 'Voi harmi :-D sinud ryösdeddiin :--DD';
      await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
    }
  });
}

const dialog_hole_search = document.querySelector('#search_hole');
const hole_search_button = document.querySelector('#hole_search');
  hole_search_button.addEventListener('click', async () => {
    const possibility=await makkaras_stolen()
    console.log('juu')
    console.log(possibility)
    if (possibility==='stolen') {
      dialog_hole_search.showModal();
      dialog_hole_search.innerHTML = `<h3>Lähde etsimään koloa ja kadonneita makkaroita!</h3>
                                <img id="spurdo" src="/Game/images_and_other/tarkee_kuva.png" alt="Tärkee kuva :-D">
                                <p id="response">Dämä on Golon edsindä :--D. Jogo mened daxilla :-D (300€) dai odad risgin Yangolla :--DDD (50€)</p>
                                <button id="search_hole_taxi">Edsi golo :---DDD daxilla</button>
                                <button id="search_hole_yango">Edsi golo :---DDD yangolla</button>
                                <button id="no_search">En edsiggään :---DDD</button>`;
      const taxi = document.querySelector('#search_hole_taxi');
      const yango = document.querySelector('#search_hole_yango');
      const no_search = document.querySelector('#no_search');
      await addListeners(no_search, taxi, yango, dialog_hole_search, ide);
      console.log(no_search, taxi, yango, dialog_hole_search, ide);
    } else {
        dialog_hole_search.showModal()
        dialog_hole_search.innerHTML = `<h3>Koloa ei voi etsiä</h3>
         <p>Kolovastaava ei ole vienyt sinulta makkaroita ;)</p>
         <p>Varo! Saatat törmätä kolovastaavaan roskiksella.</p>
         <button id="close_no_kolo">pois!</button>`;
        const close_no_kolo = document.querySelector('#close_no_kolo');
        close_no_kolo.addEventListener('click',()=>{
          dialog_hole_search.close();
        });
    }
  });