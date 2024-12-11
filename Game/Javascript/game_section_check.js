'use strict';

async function game_section_check (section) {
  //status comes 1 if true 0 if false
  try {
    console.log(section)
    const response = await fetch(`http://127.0.0.1:5000/check_status/${ide}/${section}`)
    console.log(response)
    const json = await response.json()
    console.log(json)
    return json.section_status
  } catch (error) {
    console.log(error)
  }
}