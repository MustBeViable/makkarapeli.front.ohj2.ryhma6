'use strict';

async function game_section_check (section) {
  //status comes 1 if true 0 if false
  try {
    const response = await fetch(`127.0.0.1/check_status/${ide}/${section}`)
    const json = await response.json()
    return json.section_status
  } catch (error) {
    console.log(error)
  }
}