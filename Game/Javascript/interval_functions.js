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

async function flag_for_html() {
  const country_code = await country(ide);
  if (country_code) {
    flag_img.src = `https://flagsapi.com/${country_code}/shiny/64.png`;
    flag_img.style = 'scale: 235%; padding-left: 3.4rem; padding-bottom: 1.6rem; padding-top: 1.5rem;';
    flag.appendChild(flag_img);
  }
}

async function sausage_count(ide) {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/player_makkaras/${ide}`);
    const json = await response.json();
    const makkara_count = parseFloat(json.makkara_count);
    console.log('makkara');
    const parag = document.querySelector('#num_of_sausages');
    parag.textContent = makkara_count;
  } catch (error) {
    console.log(error);
  }
}

async function player_score(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_score/${ide}`);
    const json = await response.json();
    console.log('score');
    const score = document.querySelector('#player_score');
    score.textContent = json.score;
  } catch (error) {
    console.log(error);
  }
}

async function player_money(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/player_money/${ide}`);
    const json = await response.json();
    console.log('raha');
    const money = document.querySelector('#player_money');
    money.textContent = json.money;
    return json.money
  } catch (error) {
    console.log(error);
  }
}

async function player_current_airport_info(ide) {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/player_current_airport/${ide}`);
    const json = await response.json();
    console.log('lentsikka kentsukka');
    const player_location = document.querySelector('#player_location');
    player_location.innerHTML = `${json.name} ${json.countrycode}`;
  } catch (error) {
    console.log(error + 'Daisi dulla virhe :---DDDD');
  }
}

/**
 *

 *   const player_location = document.querySelector('#player_location')
 *   const player_info = await player_current_airport_info(ide)
 *   player_location.innerHTML = `${player_info.name} ${player_info.countrycode}`
 *
 *
 */

//const player_location = document.querySelector()