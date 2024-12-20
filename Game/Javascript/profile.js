const newGameText = 'Aloita uusi peli';
const continueText = 'Jatka vanhaa peliä';

const profileTarget = document.getElementById('profile_target');
const profilePage = document.getElementById('profile');
const loginPage = document.getElementById('login');

/**
 * Creates a button and adds an async action to it.
 * @param {string} text Text on the button
 * @param {function} onClick Action on click
 */
async function createFetchButton(text, onClick) {
  const button = document.createElement('button');
  button.textContent = text;
  profileTarget.appendChild(button);
  button.addEventListener('click', onClick);
}

/**
 * Fetches player's profile (screen name, unfinished game)
 * @param {string} endpoint Endpoint URL (sign-in or sign-up endpoint)
 * @param {object} options Additional data to the fetch request (eg POST)
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

async function displayTop5() {
  const top_5_all = await top_5_lists();
  let top5_all_HTML_content = `<h3>Kaikkien aikojen top 5:</h3>`;
  for (let key in top_5_all) {
    const entry = top_5_all[key];
    let number = parseFloat(key)
    top5_all_HTML_content += `<p>${number}. ${entry.screen_name}: ${entry.score}</p>`;
  }
  profileTarget.innerHTML += top5_all_HTML_content;
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
  profileTarget.innerHTML += gameInfoHtml;
}


/**
 * Opens the user's profile.
 * @param {string} screenName User's name
 * @param {boolean} signIn Is this sign-in (true) or sign-up (false)
 */
async function openProfile(screenName, signIn) {
  try {
    const profile = signIn
        ? await fetchProfile(`/signin/${screenName}`)
        : await fetchProfile(`/signup/${screenName}`, {method: 'POST'});

    loginPage.close();
    profilePage.showModal();
    await displayTop5()
    const game = profile['unfinished_game'];

    if (game && Object.keys(game).length) {
      displayUnfinishedGame(game);
      await createFetchButton(continueText, () => startGame(false, screenName));

      function startNewWithConfirmation() {
        if (confirm("Et voi jatkaa edellistä peliäsi enää jos aloitat uuden pelin. Oletko varma, että haluat aloittaa uuden pelin?") === true) {
          startGame(true, screenName);
        }
      }

      await createFetchButton(newGameText, () => startNewWithConfirmation());
    } else {
      await createFetchButton(newGameText, () => startGame(true, screenName));
    }
  } catch (error) {
    if (error.message === 'Failed to fetch') {
      error.message = 'Elias laita api pyörimään';
    }
    else if (error.message.includes('Unexpected token')) {
      error.message = 'Syötä käyttäjätunnus.'
    }
    else if (error.message === 'Username not found.') {
      error.message = 'Käyttäjätunnusta ei löytynyt.'
    }
    else if (error.message === 'Username is already taken.') {
      error.message = 'Käyttäjätunnus on jo käytössä.'
    }
    loginBase.innerHTML = `<div>${error.message}</div>`;
    if (signIn) {
      createSigninPage();
    } else {
      createSignupPage();
    }
  }
}

/**
 * Starts a game.
 * @param {boolean} newGame If the game starting is a new game (or an old game)
 * @param screenName Player's screen name
 * @returns {Promise<*>} Returns the id of the game that was started
 */
async function startGame(newGame, screenName) {
  try {
    const requestCreateGame = `http://127.0.0.1:5000/start_game/${screenName}/${newGame}`;
    const response = await fetch(requestCreateGame);
    if (!response.ok) throw new Error('Invalid input!');
    const id = await response.json();
    console.log(id);
    saveIde((id['game_id']).toString());
    console.log(`universaali: ${ide}`)
    console.log(`universaali: ${typeof ide}`)
    profilePage.close();
    await flag_for_html();
    await player_money(ide);
    await player_score(ide);
    await player_current_airport_info(ide);
    await sausage_count(ide);
    await airport_selection_function()
  } catch (error) {
    console.log(error.message);
  }
}