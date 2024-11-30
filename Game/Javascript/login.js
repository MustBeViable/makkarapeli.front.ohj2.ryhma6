'use strict';

const screenNameForm = document.getElementById('searchForm');
const screenNameInput = document.getElementById('query');

screenNameForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  try {
    const getScreenName = screenNameInput.value;
    const requestUnfinishedGame = `http://127.0.0.1:5000/signin/${getScreenName}`;
    const response = await fetch(requestUnfinishedGame);
    if (!response.ok) throw new Error('Invalid input!');
    const gameList = await response.json()
    console.log(gameList)
    const game = gameList['unfinished_game']



  } catch (error) {
    console.log(error.message);
  }
});