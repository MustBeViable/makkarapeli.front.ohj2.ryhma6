'use strict';

async function top_5_lists() {
  try {
    const response = await fetch(`http://127.0.0.1:5000/top_5_all/`);
    const json = await response.json();
    return json;
  } catch (error) {
    console.log(error);
  }
}

async function player_top_5_lists(ide) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/top_5_player/${ide}`);
    const json = await response.json();
    return json;
  } catch (error) {
    console.log(error);
  }
}

const div_high_score = document.querySelector('#high_score');

div_high_score.innerHTML = `<button id="high_score_button"><h3>Näytä scoret</h3></button>
<dialog id="top_5_all"></dialog>`;

const high_score_button = document.querySelector('#high_score_button');
const top_5_diag = document.querySelector('#top_5_all');

high_score_button.addEventListener('click', async (evt) => {
  top_5_diag.showModal();
  const top_5_all = await top_5_lists();
  const player_top_5 = await player_top_5_lists(ide);
  let top5_all_HTML_content = `<h3>Kaikkien aikojen top 5:</h3>`;
  let top5_player_HTML_content = `<h3>Pelaajan top 5:</h3>`;
  //for...in iterates keys. Thats why it is that instead of for...of
  for (let key in top_5_all) {
    const entry = top_5_all[key];
    let number = parseFloat(key)
    top5_all_HTML_content += `<p>${number}. ${entry.screen_name}: ${entry.score}</p>`;
  }
  for (let key in player_top_5) {
    const entry = player_top_5[key];
    let number = parseFloat(key)
    top5_player_HTML_content += `<p>${number+1}. ${entry.screen_name}: ${entry.score}</p>`;
  }
  top_5_diag.innerHTML = `${top5_all_HTML_content}
  ${top5_player_HTML_content}
  <button id="close_top_5">Palaa peliin tästä</button>`;
  const top_5_closer = document.querySelector('#close_top_5');
  top_5_closer.addEventListener('click', () => {
    top_5_diag.close();
  });
});