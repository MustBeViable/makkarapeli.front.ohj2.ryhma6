'use strict';

async function game_end_check() {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_money/${ide}`);
    const json = response.json;
    const player_money = json.money;
    const player_money_int = parseFloat(player_money);
    const response2 = await game_section_check('garbage');
    const json2 = await response2.json();
    const player_section_check = json2.section_status;
    const player_section_garbage = parseFloat(player_section_check);
    const response3 = await game_section_check('taxfree');
    const json3 = await response3.json();
    const player_section_check2 = json3.section_status;
    const player_section_check_taxfree = parseFloat(player_section_check2)
    await game_end_creater(player_money_int, player_section_garbage, player_section_check_taxfree)
  } catch (error) {
    console.log(error);
  }
}

async function game_end_creater (player_money_int, player_section_garbage, player_section_check_taxfree){
  if (player_money_int < 50 && player_section_garbage === 1 && player_section_check_taxfree === 1) {
      const end_dialog = document.createElement('dialog');
      end_dialog.innerHTML = `<h2>Peli loppui</h2>
<img src="/Game/images_and_other/tarkee_kuva.png" alt="lopetuskuva">
<p>Sinulta loppui rahat ja et voi tehdä pelissä enään mitään. Voit palata aloitussivulle alhaalta.</p>
<button id="game_end_button">Aloitussivulle</button>`
      body.appendChild(end_dialog)
      end_dialog.showModal()
      const game_end_button = document.querySelector('#game_end_button');
      game_end_button.addEventListener('click', () => {

      })
    }
}