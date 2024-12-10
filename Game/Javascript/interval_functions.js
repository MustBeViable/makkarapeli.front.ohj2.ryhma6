'use strict';

const flag_img = document.createElement('img');
const flag = document.querySelector('#flag');

async function country() {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/player_location_for_flag/${ide}`);
    const country_code_json = await response.json();
    const country_code = country_code_json.country_code_for_flag;
    return country_code;
  } catch (error) {
    console.log(error.message);
  }
}

async function sausage_count(ide) {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/player_makkaras/${ide}`);
    const json = await response.json();
    const makkara_count = parseFloat(json.makkara_count);
    return makkara_count;
  } catch (error) {
    console.log(error);
  }
}

async function player_score(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_score/${ide}`);
    const json = await response.json();
    return json.score;
  } catch (error) {
    console.log(error);
  }
}

async function player_money(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_money/${ide}`);
    const json = await response.json();
    return json.money;
  } catch (error) {
    console.log(error);
  }
}

async function player_current_airport_info (ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_current_airport/${ide}`)
    const json = await response.json()
    return json
  } catch (error) {
    console.log(error + 'Daisi dulla virhe :---DDDD')
  }
}


setInterval(async function() {
  const country_code = await country(ide);
  if (country_code) {
    flag_img.src = `https://flagsapi.com/${country_code}/shiny/64.png`;
    flag_img.style = 'scale: 235%; padding-left: 3.4rem; padding-bottom: 1.6rem'
    flag.appendChild(flag_img);
  } else {
  } //vastaa pythonin pass, voi olla turha, mut laitoin varuilta
  const parag = document.querySelector('#num_of_sausages');
  parag.textContent = await sausage_count(ide);
  const score = document.querySelector('#player_score');
  score.textContent = await player_score(ide);
  const money = document.querySelector('#player_money');
  money.textContent = await player_money(ide);
  const player_location = document.querySelector('#player_location')
  const player_info = await player_current_airport_info(ide)
  player_location.innerHTML = `${player_info.name} ${player_info.countrycode}`
}, 3000);

//const player_location = document.querySelector()