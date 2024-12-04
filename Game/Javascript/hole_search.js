'use strict';

async function hole_searcher (ide, method) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/hole_search/${ide}/${method}`)
    const json = await response.json();
    return json
  } catch (error) {
    console.log(error)
  }
}

const iden = '1'; //replace me with the id

const button1 = document.querySelector('#hole_search');
const button2 = document.querySelector('#close');
const taxi = document.querySelector('#search_hole_taxi');
const yango = document.querySelector('#search_hole_yango')
const no_search = document.querySelector('#no_search')
const dialog = document.querySelector('#search_hole')


button1.addEventListener('click',  (evt) => {
  dialog.showModal()
})

no_search.addEventListener('click', (evt) => {
  dialog.close()
})

taxi.addEventListener('click', async(evt) => {
  console.log('menid sidden daxilla :--DD')
  const method = 'taxi'
  const testi = await hole_searcher(iden, method)
  console.log(testi)
})

yango.addEventListener('click', async (evt) => {
  console.log('Yoloooo!!! :----DDD Yango on senjan lembi gulguneuvo :--DD')
  const img = document.querySelector('#spurdo')
  img.src = `/Game/images_and_other/tarkee_kuva.png?random=${Date.now()}`
  const parag = document.querySelector('#response');
  parag.textContent = ''
  const method = 'yango'
  const result = await hole_searcher(iden, method);
  console.log(result)
  if (result.makkara === 'found') {
    parag.textContent = 'Onnegsi olgoon said maggarasi dagaisin :-DDD'
  } else {
    //const img = document.querySelector('#spurdo')
    img.src = `/Game/images_and_other/toinen_tarkea_kuva.png?random=${Date.now()}`
    parag.textContent = 'Voi harmi :-D sinud ryösdeddiin :--DD'
  }
} )

no_search.addEventListener('click', (evt) => {
  console.log('Dämä ei vielä dee midään :---DD')
})
