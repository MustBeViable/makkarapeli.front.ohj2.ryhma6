'use strict';

const flag_img = document.createElement('img');
const flag = document.querySelector('#flag')
let ide = 1 //add here player ide check somehow

async function country(ide) {
  try {const response = await fetch(
        `http://127.0.0.1:5000/player_location_for_flag/${ide}`);
    const country_code_json = await response.json();
    const country_code = country_code_json.country_code_for_flag;
    return country_code;
  } catch (error) {
    console.log(error.message)
  }
}

setInterval(async function () {
  const country_code = await country(ide);
  if (country_code) {
    flag_img.src = `https://flagsapi.com/${country_code}/shiny/64.png`;
    flag.appendChild(flag_img)
  } else {} //vastaa pythonin pass, voi olla turha, mut laitoin varuilta
}, 1000);