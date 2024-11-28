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