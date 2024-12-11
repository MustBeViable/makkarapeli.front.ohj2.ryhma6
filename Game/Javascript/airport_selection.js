'use strict';

//event listener add close modal
//airport selection function has to happen before opening modal
//so once when the page is opened and after that in every event listener in airport selection buttons




async function getData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data
    } catch (error) {
        return error
    }

}

async function get_money(){
  //add IDE functionality to all functions when it works
  const url = `http://127.0.0.1:5000/player_money/${ide}`
  try {
    const result = await getData(url)

    const value = result.money
    return value
  }
  catch (error){

  }
}

async function airport_fly_to(airport_number){

  try{
    const url = `http://127.0.0.1:5000/airport_selected/${ide}/${airport_number}`;
    const result = await getData(url);
    return;

  }
  catch (error){

  }

}


async function airport_selection_function(){
  try {
    await gamesectionstatusupdate('garbage','false');





    const url = `http://127.0.0.1:5000/airport/${ide}`;
    const result = await getData(url)

    const result1 = await get_money()
    console.log(result)

    document.querySelector("#target12").innerHTML = ""

    await flag_for_html()
    await player_current_airport_info(ide)
    await player_money(ide)

    const location = await getData(`http://127.0.0.1:5000/player_location/${ide}`)
    airportMarkers.clearLayers()

    const locmarker = await L.marker([location.lattitude , location.longitude]).addTo(map);

     map.flyTo([location.lattitude, location.longitude],5,{
            duration: 3,             // 3 seconds duration
            easeLinearity: 0.2,      // More linear easing (easing type)
            noMoveStart: true        // Do not trigger the 'movestart' event
        })
        airportMarkers.addLayer(locmarker)

    console.log(location)

    for(let i =0;i <= 19;i++){
      const button = document.createElement("button")
      button.innerText = `Airport: ${result[`${i+1}`].name} Price: ${result[`${i+1}`].price}`;
      const buttonid = `airportbutton${i}`
      button.setAttribute("class","airport_selection_button")
      button.setAttribute("id", buttonid)
      button.style.display = "block"





      button.addEventListener("click",async() =>{
        //here should be a call to check players money
        //if money is not enough for flight returns a message that reflects that
        if (result1 < Number(result[`${i+1}`].price)){
          console.log("not enough money");
          return;
        }
        // needs a function that calls for some kind of flyto api
        // so an async function
        console.log(result[`${i + 1}`]['number'])
        await airport_fly_to(result[`${i + 1}`]['number'])
        document.querySelector("#select_airport").close()
        await airport_selection_function()








        console.log(button.id)
      })

      document.querySelector("#target12").appendChild(button)
    }


  }
  catch (error){
    console.log(error.message)
  }

}

/*
async function airport_buttons (){
  document.querySelector("#airport_selection").addEventListener("click", async () =>{
  document.querySelector("#select_airport").showModal()
})

document.querySelector("#colslaw").addEventListener("click",async ()=>{
  document.querySelector("#select_airport").close()
})
}
*/

document.querySelector("#airport_selection").addEventListener("click", () =>{
  document.querySelector("#select_airport").showModal()
})

document.querySelector("#colslaw").addEventListener("click",()=>{
  document.querySelector("#select_airport").close()
})

//asd