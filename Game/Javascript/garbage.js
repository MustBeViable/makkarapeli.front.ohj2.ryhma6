'use strict'
//Gets data from API
async function getData(url){
  try{
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return data
  }
  catch (error){

    return error
  }


}
//gets data from garbage_can api
async function garbage_content_java() {
  const data=await getData(`http://127.0.0.1:5000/garbage/1`);
  console.log(data)
  let garbage_content=Object.keys(data)[0];
  console.log(garbage_content);
  document.querySelector('#tulostus').innerHTML = garbage_content;
  return data;
}
//gets data from doubling api
async function doubling(){
  const data=await getData(`http://127.0.0.1:5000/doubling/1`);
  console.log(data)
  let result=data.result;
  console.log(data.result);
  document.querySelector('#tulostus').innerHTML = result;
  return data;
}

//uses data from garbage to perform actions
async function garbage_action() {
  const data=await garbage_content_java();
  console.log(data)
  console.log(Object.keys(data)[0])
  console.log(data.money)
  const action=Object.keys(data)[0]
  const amount=data.money
  //if money found from garbage, doubling actions
  if (action==='money'){
    document.querySelector('#tulostus2').innerHTML = `Löysit roskiksesta ${amount}€`;
    //buttons for doubling
    const button_yes=document.querySelector('#button_yes');
    const button_no=document.querySelector('#button_no');

    button_yes.addEventListener('click',async function(){
      const doubling_result=await doubling()
      //if money won
      if (typeof doubling_result.result==='number'){
        document.querySelector('#tulostus2').innerHTML = `Tuplaus onnistui sait nyt${doubling_result.result}€`;
      //if lost
      }else{
            document.querySelector('#tulostus2').innerHTML = `${doubling_result.result}`;
            // Disables the buttons
            button_yes.disabled = true;
            button_no.disabled = true;
      }
    })
    //if dont want to double
    button_no.addEventListener('click',async function(){
      document.querySelector('#tulostus2').innerHTML = `Säästit rahasi!`;
      // Disables the buttons
      button_no.disabled = true;
      button_yes.disabled = true;

    })
  //if hole_in_charge comes from garbage
  }else if (action==='hole_in_charge'){
    document.querySelector('#tulostus2').innerHTML = `kolovastaava vei sinulta ${amount} makkaraa`;
  //if robber comes from garbage
  }else if (action==='robber'){
    document.querySelector('#tulostus2').innerHTML = `Rosvo vei sinulta ${amount}€`;
  //if finnair_personel comes from garbage
  }else if(action==='finnair_personel'){
    document.querySelector('#tulostus2').innerHTML = `${amount}`;

  }
}

//buttons for opening garbage modal and closing and modal actions
const open_garbage_button=document.querySelector('#open_garbage');
const garbage_modal=document.querySelector('#garbage_modal')
const close_garbage_modal=document.querySelector('#close_garbage_modal')
function showmodal(){
  garbage_modal.style.display='block';
}
function closemodal(){
    garbage_modal.style.display='none'
}
close_garbage_modal.addEventListener('click', closemodal);
open_garbage_button.addEventListener('click', async function () {
  showmodal();
  await garbage_action()
})




