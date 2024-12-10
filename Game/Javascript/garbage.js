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

//gets data from finnair
async function finnair() {
  const finnair_data = await getData(`http://127.0.0.1:5000/finnair/1`);
  console.log(finnair_data)
  const result = finnair_data.answer;
  console.log(finnair_data.answer);
  return result;
}

function createButton(id, text, parent,onClick){
  const button=document.createElement('button');
  button.id=id;
  button.textContent=text;
  button.addEventListener('click',onClick);
  parent.appendChild(button)
}

//uses data from garbage to perform actions
async function garbage_action() {
  const data = await garbage_content_java();
  console.log(data)
  console.log(Object.keys(data)[0])
  console.log(data.player_found_money)
  const action = Object.keys(data)[0]
  const buttoncontainer = document.querySelector('#garbage_button_container')
  buttoncontainer.innerHTML = ''

  //if money found from garbage, doubling actions

  if (action === 'player_found_money') {
    const amount = data.player_found_money
    document.querySelector(
        '#tulostus2').innerHTML = `Löysit roskiksesta ${amount}€`;

    //created yes button for doubling
    createButton('button_yes', 'Tuplaa', buttoncontainer, async function() {
      const doubling_result = await doubling()
      //if money won
      console.log(parseInt(doubling_result.result));
      console.log('juu');
      console.log(doubling_result.result);
      if ((parseInt(doubling_result.result) === 0)) {
        document.querySelector(
            '#tulostus2').innerHTML = `Hävisit, parempi tuuri ensikerralla!`;
        buttoncontainer.innerHTML = ''
      } else {
        document.querySelector(
            '#tulostus2').innerHTML = `Tuplaus onnistui sait nyt${doubling_result.result}€`;

      }

    });
    // no button if dont want to double and what if dont double
    createButton('button_no', 'älä tuplaa', buttoncontainer, function() {
      document.querySelector('#tulostus2').innerHTML = `Säästit rahasi!`;
      // Disables the buttons
      buttoncontainer.innerHTML = ''

    })
  }
  //if hole_in_charge comes from garbage
  else if (action === 'answer') {
    console.log(data.answer)
    const kolo_amount = data.answer
    document.querySelector(
        '#tulostus2').innerHTML = `kolovastaava vei sinulta ${kolo_amount} makkaraa`;
    //if robber comes from garbage
  } else if (action === 'robber') {
    const robber_amount = data.robber
    document.querySelector(
        '#tulostus2').innerHTML = `Rosvo vei sinulta ${robber_amount}€`;
    //if finnair_personel comes from garbage
  } else if (action === 'value') {
    document.querySelector(
        '#tulostus2').innerHTML = `Haluatko lahjoittaa 500€ harvinaiseen makkaraan?`;
    createButton('finnair_button_yes', 'kyllä', buttoncontainer,
        async function() {
          const finnair_result = await finnair()
          document.querySelector('#tulostus2').innerHTML = ` ${finnair_result}`;
          // Disables the buttons
          buttoncontainer.innerHTML = ''
        });

    createButton('finnair_button_no', 'ei', buttoncontainer, function() {
      document.querySelector('#tulostus2').innerHTML = ` et ostanut makkaraa`;
      // Disables the buttons
      buttoncontainer.innerHTML = ''

    })
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




