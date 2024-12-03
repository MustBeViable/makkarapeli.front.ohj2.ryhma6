'use strict';
const target = document.getElementById('target');

createLoginPage()

function createLoginPage() {
  createNameForm();
  createSignupButton()
}

function createNameForm() {
  const screenNameForm = document.createElement('form');
  screenNameForm.id = 'nameForm';
  screenNameForm.innerHTML =
      '<input id="nameQuery" name="q" type="text" placeholder="Syötä käyttäjätunnus"> ' +
      '<input type="submit" value="Kirjaudu">';
  target.appendChild(screenNameForm);
  const screenNameInput = document.getElementById('nameQuery');

  // When screen name form's button 'submit' is pushed, opens the user's profile.
  screenNameForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    await openProfile(screenNameInput.value);
  });
}

function createSignupButton() {
  const signUpButton = document.createElement('button');
  signUpButton.id = 'signUp';
  signUpButton.textContent = 'Eikö sinulla ole käyttäjätunnusta? Luo uusi tili tästä';

  signUpButton.addEventListener('click', (event) => {
    const extraForm = document.createElement('input');
    extraForm.id = 'extraForm';
    extraForm.placeholder = 'Kengännumero';
    target.appendChild(extraForm);
    signUpButton.remove();
  });
  target.appendChild(signUpButton);
}


async function openProfile(screenName) {
  try {
    const requestUnfinishedGame = `http://127.0.0.1:5000/signin/${screenName}`; //checks if given screen name is valid
    const response = await fetch(requestUnfinishedGame);  //returns user's unfinished game or an empty list
    if (!response.ok) throw new Error('Käyttäjänimeä ei löytynyt.');
    const gameList = await response.json();
    const game = gameList['unfinished_game']; //info of the unfinished game

    target.innerHTML = '';

    if (Object.keys(game).length !== 0) {   //if there is an unfinished game,
      const {game_location, game_makkaras, game_money, game_score} = game;  //save its info
      const oldGameInfo = document.createElement('div');
      oldGameInfo.innerText = `
      Keskeneräinen peli
      Pisteet: ${game_score}
      Makkarat: ${game_makkaras}
      Raha: ${game_money}
      Lentokenttä: ${game_location}`
      target.appendChild(oldGameInfo);
      await startOldGameButton(screenName);
    }
    await startNewGameButton(screenName);
  } catch (error) {
    console.log(error.message);
    target.innerHTML = `<div>${error.message}</div>`;
    createNameForm();
  }
}


// Creates a button for starting a new game. Button creates and starts a new game when clicked.
function startNewGameButton(screenName) {
  const newGameButton = document.createElement('button');
  newGameButton.id = 'newGame';
  newGameButton.textContent = 'Aloita uusi peli';
  target.appendChild(newGameButton);

  newGameButton.addEventListener('click', async (event) => {
    await startGame(true, screenName);
  });
}

// Creates a button for continuing a game. Starts the player's unfinished game when pushed.
function startOldGameButton(screenName) {
  const oldGameButton = document.createElement('button');
  oldGameButton.id = 'oldGame';
  oldGameButton.textContent = 'Jatka vanhaa peliä';
  target.appendChild(oldGameButton);

  oldGameButton.addEventListener('click', async (event) => {
    await startGame(false, screenName);
  });
}

// If parameter newGame is true, creates a new game and returns its id.
// If it's false, returns the id of the user's unfinished game.
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

function signin(screenName) {
  //checks if given screen name is valid
  return `http://127.0.0.1:5000/signin/${screenName}`;
}

function signup(screenName) {
  return `http://127.0.0.1:5000/signup/${screenName}`; //checks if given screen name is valid
}