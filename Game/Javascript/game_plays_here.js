'use strict';

async function game_plays_here(ide) {
  await airport_buttons();
  let [airportMarkers, map] = await map_js_juttu();
  await airport_selection_function(ide, airportMarkers, map);
  await hole_search_buttons(ide)
}

game_plays_here(1);