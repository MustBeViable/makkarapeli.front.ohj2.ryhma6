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
  const data=await getData(`http://127.0.0.1:5000/garbage/${ide}`);
  let garbage_content=Object.keys(data)[0];
  console.log(garbage_content);
  return data;
}
//gets data from doubling api
async function doubling(){
  const data=await getData(`http://127.0.0.1:5000/doubling/${ide}`);
  console.log(data)
  let result=data.result;
  console.log(data.result);
  return data;
}

//gets data from finnair
async function finnair() {
  const finnair_data = await getData(`http://127.0.0.1:5000/finnair/${ide}`);
  console.log(finnair_data)
  const result = finnair_data.answer;
  console.log(finnair_data.answer);
  return result;
}

async function save_money() {
  const save_money_data = await getData(`http://127.0.0.1:5000/save_money/${ide}`);
  console.log(save_money_data)

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
  const action = Object.keys(data)[0]
  const garbagemessage=document.querySelector('#garbage_message')
  const garbageresults=document.querySelector('#garbage_results')
  const buttoncontainer = document.querySelector('#garbage_button_container')
  buttoncontainer.innerHTML = ''

  //if money found from garbage, doubling actions

  if (action === 'player_found_money') {
    const amount = data.player_found_money
    garbagemessage.textContent=`Löysit roskiksesta ${amount}€`

    //created yes button for doubling
    createButton('button_yes', 'Tuplaa', buttoncontainer, async function() {
      const doubling_result = await doubling()
      //if money won
      if ((parseInt(doubling_result.result) === 0)) {
        garbagemessage.textContent=`Hävisit, parempi tuuri ensikerralla!`
        await player_money(ide)
        buttoncontainer.innerHTML = ''
      } else {
        garbagemessage.textContent=`Tuplaus onnistui sait nyt${doubling_result.result}€`;
        await player_money(ide)
      }
    });
    // no button if dont want to double and what if dont double
    createButton('button_no', 'älä tuplaa', buttoncontainer, async function() {
      garbagemessage.textContent= `Säästit rahasi!`;
      await player_money(ide)
      // Disables the buttons
      buttoncontainer.innerHTML = ''

    })

  }
  //if hole_in_charge comes from garbage
  else if (action === 'answer') {
    const kolo_amount = data.answer
    garbagemessage.textContent=`kolovastaava vei sinulta ${kolo_amount} makkaraa`;
    await player_score(ide)
    //if robber comes from garbage
  } else if (action === 'robber') {
    const robber_amount = data.robber
    garbagemessage.textContent=`Rosvo vei sinulta ${robber_amount}€`;
    await player_money(ide)
    //if finnair_personel comes from garbage
  } else if (action === 'value') {
    garbagemessage.textContent=`Haluatko lahjoittaa 500€ harvinaiseen makkaraan?`;
    createButton('finnair_button_yes', 'kyllä', buttoncontainer, async function() {
          const finnair_result = await finnair()
          await player_money(ide)
          await player_score(ide)
          await sausage_count(ide)
          garbagemessage.textContent=` ${finnair_result}`;
          // Disables the buttons
          buttoncontainer.innerHTML = ''
        });

    createButton('finnair_button_no', 'ei', buttoncontainer, function() {
      garbagemessage.textContent=`Et ostanut makkaraa`;
      // Disables the buttons
      buttoncontainer.innerHTML = ''

    })
  }
  return action
}
//buttons for opening garbage modal and closing and modal actions
const open_garbage_button=document.querySelector('#open_garbage');
const garbage_dialog=document.querySelector('#garbage_can')
const garbage_button=document.querySelector('#garbage')

open_garbage_button.addEventListener('click',()=>{
  garbage_dialog.showModal();
});

//sulje closes,
const closeButton = document.querySelector('.close');
closeButton.addEventListener('click', async() => {
  garbage_dialog.close();
  await save_money()
  await player_score(ide)
  await player_money(ide)
  await sausage_count(ide)
  document.querySelector('#intro').style.display = 'block';
  document.querySelector('#garbage_results').style.display = 'none';
  document.querySelector('#garbage_message').style.display = 'none';
  document.querySelector('#garbage_button_container').style.display = 'none';
})

//async function save_money_call() {
 //const tulos = await garbage_action();
 //console.log(tulos)
 //if (tulos === 'player_found_money'){
//   save_money()
// }
//}

const garbage_form = document.querySelector('#garbage_form');
garbage_form.addEventListener('submit', (event) => {
  event.preventDefault();
  document.querySelector('#intro').style.display = 'none';
  garbage_action()
  document.querySelector('#garbage_results').style.display = 'block';
  document.querySelector('#garbage_message').style.display='block';
  document.querySelector('#garbage_button_container').style.display='block';

});
