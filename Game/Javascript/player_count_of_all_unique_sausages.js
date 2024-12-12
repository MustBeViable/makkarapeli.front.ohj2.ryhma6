'use strict';

async function player_current_sausages_and_count (ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_current_makkara_list/${ide}`);
    const json = await response.json()
    return json
  } catch (error) {
    console.log(error)
  }
}

const sausage_count_dialog = document.querySelector('#player_sausages_and_count');
const sausage_count_button = document.querySelector('#player_sausages');

sausage_count_button.addEventListener('click', async () => {
  let sausage_count_dialog_content= `<h3 id="sausages_here">Sinun makkarasi ja niiden määrät</h3>`
  const list_for_makkaras = await player_current_sausages_and_count(ide)
  for (let num = 0; num < list_for_makkaras.length; num++) {
    sausage_count_dialog_content += `<p>${list_for_makkaras[num].name}: ${list_for_makkaras[num].count}</p>`
  }
  sausage_count_dialog_content += `<button id="sausage_close_button">Sulje tästä</button>`
  sausage_count_dialog.innerHTML = sausage_count_dialog_content
  const sausage_list_close_button = document.querySelector('#sausage_close_button')
  sausage_count_dialog.showModal()
  sausage_list_close_button.addEventListener('click', () => {
    sausage_count_dialog.close()
  })
})