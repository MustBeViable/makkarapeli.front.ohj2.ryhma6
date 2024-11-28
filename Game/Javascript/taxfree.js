'use strict'
async function getData(url){
  const response = await fetch(url);
  if(!response.ok) throw new Error('invalid server input')
  const data = await response.json();
  return data
}

async function taxfree() {
  try{
    const taxfree_data = await getData(`/airport/${1}`)
    console.log(taxfree_data);
  }
  catch (error){
    console.log(error);
  }

}
taxfree()