'use strict'

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const data = await response.json();
  return data
}

async function getDataMoney() {
  const money = await getData('http://127.0.0.1:5000/player_money/1')
  console.log(money)
}

async function getDataLocation() {
  const location = await getData('http://127.0.0.1:5000/player_location/1')
  console.log(location)
}

async function getDataSausage() {
  const sausage = await getData('http://127.0.0.1:5000/player_location/1')
}

getDataMoney()
getDataLocation()