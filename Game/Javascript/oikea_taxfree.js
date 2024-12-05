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

async function buySausage (ide, method) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/taxfree_buy/${ide}/${method}`)
    const json = await response.json();
    return json
  } catch (error) {
    console.log(error)
  }
}

const ide = '1'

const dialog = document.getElementById('taxfree');
const button = document.querySelector('#taxfree_btn');
const button2 = document.querySelector('#close');
const button3 = document.getElementById('taxfree_buy_sausage')



button.addEventListener('click',  (evt) => {
  dialog.showModal()
})

button2.addEventListener('click', (evt) => {
  dialog.close();
  const method = 'close';
})

button3.addEventListener('click', (evt) => {
  console.log('Tehdään kaupat');
  const method = 'payment';
})

button.addEventListener('click', async(evt) => {
  console.log('Tervetuloa ostoksille!')
  const img = document.querySelector('#bagdrop')
  img.src = `/Game/images_and_other/taxfree.png?random=${Date.now()}`
  const testi = await hole_searcher(iden)
  console.log(testi)
})