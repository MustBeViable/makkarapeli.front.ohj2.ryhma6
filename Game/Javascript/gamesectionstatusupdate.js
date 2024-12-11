'use strict';

async function gamesectionstatusupdate(section, status) {
  try {
    const response = await fetch(
        `http://127.0.0.1:5000/update_status/${ide}/${section}/${status}`);
    return 'jee'
  } catch (error) {
    console.log(error)
    return 'ei jee'
  }
}