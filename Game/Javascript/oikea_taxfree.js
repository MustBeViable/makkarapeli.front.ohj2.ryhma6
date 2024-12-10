'use strict';

async function getDataTaxfree(ide, method) {
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
    return json;
  } catch (error) {
    console.log(error);
  }
}

async function taxfree_buttons() {
  const dialog_taxfree = document.getElementById('taxfree');
  const button_taxfree = document.querySelector('#taxfree_btn');
  const close_taxfree = document.querySelector('#close_taxfree');
  const buy_sausage = document.getElementById('taxfree_buy_sausage');

  button_taxfree.addEventListener('click', async (evt) => {
    dialog_taxfree.showModal();
    const json = await getDataTaxfree(ide);
    console.log(json);
    dialog_taxfree.innerHTML = `<h3>Tervetuloa taxfree-myymälään!</h3>
                                <form method="dialog">
                                    <p id="country_sausage_name">Haluatko ostaa ${json.name}n?</p>
                                    <p id="sausage_price">(${json.value}€)</p>
                                    <button id="taxfree_buy_sausage">Kyllä kiitos!</button>
                                    <button id="close_taxfree">Sulje</button>
                                </form>`;
  });
  close_taxfree.addEventListener('click', async (evt) => {
    dialog_taxfree.close();
  });
  buy_sausage.addEventListener('click', async (evt) => {
    console.log('Tehdään kaupat');
    const method = 'payment';
    buySausage(ide);
  });
  button_taxfree.addEventListener('click', async (evt) => {
    console.log('Tervetuloa ostoksille!');
    const img = document.querySelector('#taxfree_img');
    img.src = `/Game/images_and_other/taxfree.png?random=${Date.now()}`;
    img.url('../images_and_other/taxfree.png');
  });

}
/**
<script src="/Game/Javascript/playthrought_variables_universal.js"
        defer></script>
<script src="/Game/Javascript/hole_search.js" defer></script>
<script src="/Game/Javascript/interval_functions.js" defer></script>
<script src="/Game/Javascript/oikea_taxfree.js" defer></script>
<script src="/Game/Javascript/top_5_chart.js" defer></script>
<script src="/Game/Javascript/player_count_of_all_unique_sausages.js"
        defer></script>
<script src="/Game/Javascript/game_istructions.js" defer></script>


**/

