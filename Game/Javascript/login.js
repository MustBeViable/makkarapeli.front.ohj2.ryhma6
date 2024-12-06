'use strict';

const target = document.getElementById('target');
const signInText = 'Kirjaudu';
const signUpText = 'Luo tunnus';
const newGameText = 'Aloita uusi peli';
const continueText = 'Jatka vanhaa peliä';

// Starts the whole process.
createLoginPage();

/**
 * Creates the login page.
 */
function createLoginPage() {
  createNameForm(signInText, true);
  function goToSignUp() {
    target.innerHTML = ''
    createSignUpPage()
  }
  createButton('Oletko uusi? Luo tili tästä', () => goToSignUp())
}

function createSignUpPage() {
  createNameForm(signUpText, false);
  createExtraFrom();
  function returnToSignIn(){
    target.innerHTML = ''
    createLoginPage()
  }
  createButton("Oletko jo käyttäjä? Kirjaudu sisään", ()=> returnToSignIn())
}

/**
 * Creates a form for entering screen name.
 * @param {string} value Text displayed on the submit button
 * @param {boolean} signin Is this sign in or sign up
 */
function createNameForm(value, signin) {
  const formHtml = `
    <form id="nameForm">
      <input id="nameQuery" name="q" type="text" placeholder="Käyttäjätunnus">
      <input type="submit" value="${value}">
    </form>
  `;
  target.insertAdjacentHTML('beforeend', formHtml);

  const screenNameForm = document.getElementById('nameForm');
  screenNameForm.addEventListener('submit', async (event) => {
    const screenName = document.getElementById('nameQuery').value;
    event.preventDefault();
    await openProfile(screenName, signin);
  });
}

/**
 * Creates an extra form to sign up.
 */
function createExtraFrom() {
  const extraForm = document.createElement('input');
  extraForm.id = 'extraForm';
  extraForm.placeholder = 'Kengännumero';
  target.appendChild(extraForm);
}


/**
 * Opens the user's profile.
 * @param {string} screenName Käyttäjän nimi
 * @param {boolean} signIn Onko kirjautuminen vai rekisteröinti
 */
async function openProfile(screenName, signIn) {
  target.innerHTML = '';
  try {
    const profile = signIn
        ? await fetchProfile(`/signin/${screenName}`)
        : await fetchProfile(`/signup/${screenName}`, {method: 'POST'});

    const game = profile['unfinished_game'];
    if (game && Object.keys(game).length) {
      displayUnfinishedGame(game);
      await createFetchButton(continueText, () => startGame(false, screenName));
    }
    await createFetchButton(newGameText, () => startGame(true, screenName));
  } catch (error) {
    console.log('täällä');
    if (error.message === 'Failed to fetch') {
      error.message = 'Elias laita api pyörimään';
    }
    target.innerHTML = `<div>${error.message}</div>`;
    if (signIn) {
      createLoginPage()
    } else {
      createSignUpPage()
    }
  }
}

/**
 * Fetches player's profile (screen name, unfinished game)
 * @param {string} endpoint Endpoint URL
 * @param {object} options Additional data to the fetch request
 * @returns {object} Returns json
 */
async function fetchProfile(endpoint, options = {}) {
  const response = await fetch(`http://127.0.0.1:5000${endpoint}`, options);

  if (!response.ok) {
    const errorResponse = await response.json();
    console.log(errorResponse.message);
    throw new Error(errorResponse.message);
  }
  return await response.json();
}

/**
 * Shows the info of an unfinished game to the user.
 * @param {object} game Game location, makkaras, score and money
 */
function displayUnfinishedGame(game) {
  const {game_location, game_makkaras, game_score, game_money} = game;
  const gameInfoHtml = `
    <div>
      Keskeneräinen peli
      <br>Pisteet: ${game_score}
      <br>Makkarat: ${game_makkaras}
      <br>Raha: ${game_money}
      <br>Sijainti: ${game_location}
    </div>
  `;
  target.innerHTML += gameInfoHtml;
}

/**
 * Creates a button and adds an async action to it.
 * @param {string} text Text on the button
 * @param {function} onClick Action on click
 */
async function createFetchButton(text, onClick) {
  const button = document.createElement('button');
  button.textContent = text;
  target.appendChild(button);
  button.addEventListener('click', onClick);
}

/**
 * Creates a button and adds an action to it.
 * @param {string} text Text on the button
 * @param {function} onClick Action on click
 */
function createButton(text, onClick) {
  const button = document.createElement('button');
  button.textContent = text;
  target.appendChild(button);
  button.addEventListener('click', onClick);
}

/**
 *
 * @param newGame
 * @param screenName
 * @returns {Promise<void>}
 */
async function startGame(newGame, screenName) {
  try {
    const requestCreateGame = `http://127.0.0.1:5000/start_game/${screenName}/${newGame}`;
    const response = await fetch(requestCreateGame);
    if (!response.ok) throw new Error('Invalid input!');
    const id = await response.json();
    console.log(id);
  } catch (error) {
    console.log(error.message);
  }
}
