'use strict'

async function getData(url) {
  let element = '<div>'
    const comment = 'Makkara taxfree';
    addEventListener('click', () => {
      const response = await fetch('/taxfree/1');
      const ans = 'Tervetuloa shoppailemaan Taxfreehen! Haluaisitko ostaa tämän maan makkaran?';
      const data1 = await response.json();
      return data1
      if (ans === 'OK') {
        const respons = await fetch('/taxfree_buy/1');
        const data2 = await response.json();
        return data2
      }
    })
  element += '</ul>'

  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const data = await response.json();
  return data
}

async function taxfree(url) {

  const ans = confirm('Tervetuloa shoppailemaan Taxfreehen. Haluatko ostaa makkaran?');
  if (ans === 'OK') {
    const response = await fetch('/taxfree/1');
    const data = await response.json();
    return data;
  }
}

async function getDataMoney() {
  const money = await getData('http://127.0.0.1:5000/player_money/1')
  console.log(money)
}

async function getDataLocation() {
  const location = await getData('http://127.0.0.1:5000/player_location/1')
  console.log(location)
}

getDataMoney()
getDataLocation()