'use strict';

async function getDataTaxfree(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/taxfree/${ide}`);
    const json = await response.json();
    return json;
  } catch (error) {
    console.log(error);
  }
}

async function buySausage(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/taxfree_buy/${ide}`);
    const json = await response.json();
  } catch (error) {
    console.log(error);
  }
}
const button_taxfree = document.querySelector('#taxfree_btn');
const dialog_taxfree = document.getElementById('taxfree');

button_taxfree.addEventListener('click', async (evt) => {
  const game_check_code = await game_end_check()
  console.log(game_check_code)
  if (game_check_code === 1) {
    console.log('jee')
  } else {dialog_taxfree.showModal();
  const json = await getDataTaxfree(ide);
  console.log(json);
  dialog_taxfree.innerHTML = `<h3>Tervetuloa taxfree-myymälään!</h3>
                                    <div class="taxfree_img">
                                        <br>
                                        <br>
                                        <br>
                                        <br>
                                        <br>
                                        <br>
                                    </div>
                                    <p id="country_sausage_name">Haluatko ostaa ${json.name}n?</p>
                                    <p id="sausage_price">(${json.value}€)</p>
                                    <button id="taxfree_buy_sausage">Kyllä kiitos!</button>
                                    <button id="close_taxfree">Sulje</button>`;
  const close_taxfree = document.querySelector('#close_taxfree');
  const buy_sausage = document.getElementById('taxfree_buy_sausage');
  buy_sausage.addEventListener('click', async (evt) => {
    console.log('Tehdään kaupat');
    await buySausage(ide);
    await player_score(ide)
    await player_money(ide)
    await sausage_count(ide)
    await game_end_check()
    dialog_taxfree.close();
  });
  close_taxfree.addEventListener('click', (evt) => {
    dialog_taxfree.close();
  });}

});

button_taxfree.addEventListener('click', async (evt) => {
  console.log('Tervetuloa ostoksille!');
});