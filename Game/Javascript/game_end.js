'use strict';

async function game_end_check() {
  try {
    const player_money_int = await get_money(ide)
    console.log(`rahat: ${player_money_int}`)
    const player_section_garbage_num = await game_section_check('garbage');
    const player_section_garbage = parseFloat(player_section_garbage_num);
    await game_end_creater(player_money_int, player_section_garbage);
    console.log(
        `money: ${player_money_int}, garbage: ${player_section_garbage}`);
    if (player_money_int < 50 && player_section_garbage === 1) {
      const number = 1;
      return number;
    } else {
      console.log('menee väärään');
    }
  } catch (error) {
    console.log(error);
  }
}

async function game_end_creater(player_money_int, player_section_garbage) {
  if (player_money_int < 50 && player_section_garbage === 1) {
    const end_dialog = document.createElement('dialog');
    end_dialog.innerHTML = `<h2>Peli loppui</h2>
<img src="/Game/images_and_other/tarkee_kuva.png" alt="lopetuskuva">
<p>Sinulta loppui rahat ja et voi tehdä pelissä enään mitään. Voit palata aloitussivulle alhaalta.</p>
<button id="game_end_button">Aloitussivulle</button>`;
    document.body.appendChild(end_dialog);
    end_dialog.showModal();
    const game_end_button = document.querySelector('#game_end_button');
    game_end_button.addEventListener('click', () => {
      console.log('clickity clackity')
      window.location.href = 'http://localhost:63342/makkarapeli.front.ohj2.ryhma6/Game/HTML/main.html?_ijt=l0sovjub7c0kqp6mf6av97sg80&_ij_reload=RELOAD_ON_SAVE'
    });
  }
}