'use strict';

async function getData(url){
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("invalid server input");
    const data = await response.json();
    return data
  }
  catch (error){
    console.log(error.message);
  }
}



function airport_selection_function(evt){
  const url = "http://127.0.0.1:5000/airport/1";
  const result = getData(url)
  console.log(result)


}
airport_selection_function()