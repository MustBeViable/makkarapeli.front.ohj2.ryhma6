'use strict';

const screenNameForm = document.getElementById('searchForm');
const screenNameInput = document.getElementById('query');
let unfinishedGame = null;
const target = document.getElementById('target');


async function openProfile() {
  try {
    const getScreenName = screenNameInput.value;
    const requestUnfinishedGame = `http://127.0.0.1:5000/signin/${getScreenName}`; //checks if given screen name is valid
    const response = await fetch(requestUnfinishedGame);  //returns user's unfinished game or an empty list
    if (!response.ok) throw new Error('Invalid input!');
    const gameList = await response.json();
    console.log(gameList);
    const game = gameList['unfinished_game']; //info of the unfinished game

    target.innerHTML = '';

    console.log(Object.keys(game));

    if (Object.keys(game).length !== 0) {   //if there is an unfinished game,
      console.log(game);
      unfinishedGame = game;
      const {game_location, game_makkaras, game_money, game_score} = game;  //save its info
      await startOldGame();
    }
    await startNewGame();
  } catch (error) {
    console.log(error.message);
  }
}

function startNewGame() {
  const newGameButton = document.createElement('button')
  newGameButton.id = 'newGame';
  newGameButton.textContent = 'Aloita uusi peli';
  target.appendChild(newGameButton)
  //target.innerHTML += '<button id="newGame">Aloita uusi peli</button> ';
  //const newGameButton = document.getElementById('newGame');
  console.log(newGameButton);

  newGameButton.addEventListener('click', async (event) => {
    await jotain(true);
  });
}

function startOldGame() {
  const oldGameButton = document.createElement('button');
  oldGameButton.id = 'oldGame';
  oldGameButton.textContent = 'Jatka vanhaa peliä';
  target.appendChild(oldGameButton);
  //const oldGameButton = document.getElementById('oldGame');
  console.log(oldGameButton);

    oldGameButton.addEventListener('click', async(event) => {
      console.log('Napin klikkaus havaittu!');
      await jotain(false)
    });
}

screenNameForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  await openProfile();
});

async function jotain(newGame) {
  const screenName = screenNameInput.value;
  console.log(screenName);
  try {
    const requestCreateGame = `http://127.0.0.1:5000/start_game/${screenName}/${newGame}`;
    const response = await fetch(requestCreateGame);
    console.log(requestCreateGame);
    if (!response.ok) throw new Error('Invalid input!');
    const id = await response.json();
    console.log(id);
  } catch (error) {
    console.log(error.message);
  }
}

/*
  startGame.addEventListener('click', async (event) => {
    const screenName = screenNameInput.value;
    try {
      const requestCreateGame = `http://127.0.0.1:5000/start_game/${screenName}/${newGame}`;
      const response = await fetch(requestCreateGame);
      console.log(requestCreateGame);
      if (!response.ok) throw new Error('Invalid input!');
      const id = await response.json();
      console.log(id);
    } catch (error) {
      console.log(error.message);
    }
  });
}

function openGame() {

}
*/