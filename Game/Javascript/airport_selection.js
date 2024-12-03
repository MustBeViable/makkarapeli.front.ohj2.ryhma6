'use strict';

async function getData(url){
  try {
    const response = await fetch(url);
    if (!response.ok){
      throw new Error("invalid server input");
    }
    const data = await response.json();
    return data
  }
  catch (error){
    console.log(error.message);
    return error;
  }
}

async function get_money(){
  //add IDE functionality to all functions when it works
  const url = `http://127.0.0.1:5000/player_money/1`
  try {
    const result = await getData(url)
    console.log(result)
    console.log(typeof result)
    return result
  }
  catch (error){

  }
}

async function airport_fly_to(airport_number){

  try{

    const url = `http://127.0.0.1:5000/airport_selected/1/${airport_number}`
    const result = await getData(url)
    return;

  }
  catch (error){

  }

}


async function airport_selection_function(){
  try {
    const url = "http://127.0.0.1:5000/airport/1";
    const result = await getData(url)
    console.log(result)

    document.querySelector("#target12").innerHTML = ""
    for(let i =0;i <= 19;i++){
      const button = document.createElement("button")
      button.innerText = result[`${i+1}`].name;
      const buttonid = `airportbutton${i}`
      button.setAttribute("id", buttonid)
      button.style.display = "block"
      button.addEventListener("click",() =>{
        //here should be a call to check players money
        //if money is not enough for flight returns a message that reflects that

        const result1 = get_money()
        console.log(get_money())
        if (result1 < Number(result[`${i+1}`].price)){
          console.log("not enough money");
          return;
        }
        // needs a function that calls for some kind of flyto api
        // so an async function
        console.log(result[`${i + 1}`]['number'])
        airport_fly_to(result[`${i + 1}`]['number'])


        console.log(button.id)
      })
      document.querySelector("#target12").appendChild(button)
    }


  }
  catch (error){
    console.log(error.message)
  }

}


airport_selection_function()

//asd