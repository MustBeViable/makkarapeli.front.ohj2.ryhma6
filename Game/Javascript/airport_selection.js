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

async function airport_fly_to(airport_number){
  //here should be a call to check players money
  //if money is not enough for flight returns a message that reflects that

  try{

    const url = `http://127.0.0.1:5000/airport_selected/1/${airport_number}`

  }
  catch (error){

  }

}


async function airport_selection_function(evt){
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
        // needs a function that calls for some kind of flyto api
        // so an async function
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