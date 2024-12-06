'use strict'
async function getData(url){
  try{
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return data
  }
  catch (error){
    console.log(error);
    return error
  }


}

async function taxfree() {
  getData(`/Garbage/${1}`)


}
taxfree()