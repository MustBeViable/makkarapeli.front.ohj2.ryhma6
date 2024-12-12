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
    const response = await fetch(
        `http://127.0.0.1:5000/makkaras_stolen/${ide}`);
    const json = await response.json();
    console.log(json);
    const result = json.makkara;
    console.log('juu');
    console.log(result);
    return result;
  } catch (error) {
    console.log(error);
  }
}

async function removeElements(no_search, taxi, yango, dialog_hole_search, ide) {
  console.log(dialog_hole_search);
  dialog_hole_search.removeChild(taxi);
  dialog_hole_search.removeChild(yango);
  dialog_hole_search.removeChild(no_search);
  const close = document.createElement('button');
  close.id = 'close';
  close.textContent = 'Palaa lentokentälle';
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
    const img = document.querySelector('#spurdo');
    const h3 = document.querySelector('#kolovastaava');
    img.src = `/Game/images_and_other/A_white-skinned_blonde_girl_scout_resized_600x600.jpg`;
    const method = 'taxi';
    await hole_searcher(ide, method);
    const result = await hole_searcher(ide, method);
    await sausage_count(ide);
    console.log(result);
    const parag = document.querySelector('#response');
    parag.textContent = '';
    h3.textContent = 'Löysit kolovastaavan ja sait makkarasi takaisin!';
    const game_check_code = await game_end_check();
    console.log(game_check_code);
    if (game_check_code === 1) {
      console.log('jee');
    }
    await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
  });
  yango.addEventListener('click', async (evt) => {
    console.log('Yoloooo!!! :----DDD Yango on senjan lembi gulguneuvo :--DD');
    const img = document.querySelector('#spurdo');
    img.src = `/Game/images_and_other/tarkee_kuva.png?random=${Date.now()}`;
    const parag = document.querySelector('#response');
    const h3 = document.querySelector('#kolovastaava');
    parag.textContent = '';
    h3.textContent = 'Löysit kolovastaavan ja sait makkarasi takaisin!';
    const method = 'yango';
    const result = await hole_searcher(ide, method);
    console.log(result);
    if (result.makkara === 'found') {
      h3.textContent = 'Löysit kolovastaavan ja sait makkarasi takaisin!';
      await sausage_count(ide);
      const game_check_code = await game_end_check();
      console.log(game_check_code);
      if (game_check_code === 1) {
        console.log('jee');
      }
      await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
    } else {
      //const img = document.querySelector('#spurdo')
      img.src = `/Game/images_and_other/A_person_waiting_for_a_taxi_in_rainy_weather_resized_600x600.jpg`;
      h3.textContent = 'Voi harmi, Yango ajoi hitaasti ja saavuit perille myöhään, Kolovastaava ehti piiloon. Jouduit tilaamaan taksin takaisin kentälle. Tämä maksoi sinulle huomattavan summan rahaa.';
      await removeElements(no_search, taxi, yango, dialog_hole_search, ide);
      const game_check_code = await game_end_check();
      console.log(game_check_code);
      if (game_check_code === 1) {
        console.log('jee');
      }
    }
  });
}

const dialog_hole_search = document.querySelector('#search_hole');
const hole_search_button = document.querySelector('#hole_search');
hole_search_button.addEventListener('click', async () => {
  const possibility = await makkaras_stolen(ide);
  console.log('juu');
  console.log(possibility);
  if (possibility === 'stolen') {
    dialog_hole_search.showModal();
    dialog_hole_search.innerHTML = `<h3 id="kolovastaava">Lähde etsimään koloa ja kadonneita makkaroita!</h3>
                                <img id="spurdo" src="/Game/images_and_other/A_person_leaving_an_airport_terminal_and_getting_i_resized_600x600.jpg" alt="Tärkee kuva :-D">
                                <p id="response">Päätit lähteä etsimään varastettuja makkaroita. Sinulla on 2 vaihtoehtoa, taksi (300€) tai otat riskin Yangolla (50€).</p>
                                <button id="search_hole_taxi">Taksi (300€)</button>
                                <button id="search_hole_yango">Yango (50€)</button>
                                <button id="no_search">Palaa lentokentälle</button>`;
    const taxi = document.querySelector('#search_hole_taxi');
    const yango = document.querySelector('#search_hole_yango');
    const no_search = document.querySelector('#no_search');
    await addListeners(no_search, taxi, yango, dialog_hole_search, ide);
    console.log(no_search, taxi, yango, dialog_hole_search, ide);
  } else {
    dialog_hole_search.showModal();
    dialog_hole_search.innerHTML = `<h3>Koloa ei voi etsiä</h3>
         <p>Kolovastaava ei ole vienyt sinulta makkaroita ;)</p>
         <p>Varo! Saatat törmätä kolovastaavaan roskiksella.</p>
         <button id="close_no_kolo">Palaa kentälle</button>`;
    const close_no_kolo = document.querySelector('#close_no_kolo');
    close_no_kolo.addEventListener('click', async () => {
      dialog_hole_search.close();
      let game_check_code = await game_end_check();
      console.log(game_check_code);
      if (game_check_code === 1) {
        console.log('jee');
      }
    });
  }
});