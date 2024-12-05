'use strict'

async function getDataTaxfree (ide, method) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/taxfree/${ide}/${method}`)
    const json = await response.json();
    return json
  } catch (error) {
    console.log(error)
  }
}

async function buySausage (ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/taxfree_buy/${ide}`)
    const json = await response.json();
    return json
  } catch (error) {
    console.log(error)
  }
}

const dialog_taxfree = document.getElementById('taxfree');
const button_taxfree = document.querySelector('#taxfree_btn');
const close_taxfree = document.querySelector('#close_taxfree');
const buy_sausage = document.getElementById('taxfree_buy_sausage')



button_taxfree.addEventListener('click',  (evt) => {
  dialog_taxfree.showModal()
})

close_taxfree.addEventListener('click', (evt) => {
  dialog_taxfree.close();
})

buy_sausage.addEventListener('click', (evt) => {
  console.log('Tehdään kaupat');
  const method = 'payment';
  buySausage(ide)
})

button_taxfree.addEventListener('click', async(evt) => {
  console.log('Tervetuloa ostoksille!')
  const img = document.querySelector('#bagdrop')
  img.src = `/Game/images_and_other/taxfree.png?random=${Date.now()}`
  const testi = await hole_searcher(iden)
  console.log(testi)
})