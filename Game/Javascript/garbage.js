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


//send data to python
async function send_data_python(thing){
  const value=thing
  try {
      const response = await fetch('/process', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ value })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      document.getElementById('output').innerHTML = data.result;
  } catch (error) {
      console.error('Error:', error);
  }
}



//uses data from garbage to perform actions
async function garbage_action() {
  const data=await garbage_content_java();
  console.log(data)
  console.log(Object.keys(data)[0])
  console.log(data.money)
  const action=Object.keys(data)[0]
  const amount=data.money
  if (action==='money'){
    document.querySelector('#tulostus2').innerHTML = `Löysit roskiksesta ${amount}€`;
    //do you want to double?
    const button_yes=document.querySelector('#button_yes');
    const button_no=document.querySelector('#button_no');

    // Remove previous listeners by replacing the buttons
    const new_button_yes = button_yes.cloneNode(true);
    const new_button_no = button_no.cloneNode(true);
    button_yes.replaceWith(new_button_yes);
    button_no.replaceWith(new_button_no);

    button_yes.addEventListener('click',async function(){
      const doubling_result=await doubling()
      if (typeof doubling_result==='number'){
        document.querySelector('#tulostus2').innerHTML = `Tuplaus onnistui sinulla on nyt${doubling_result}€`;
      }else if(doubling_result.result==='string'){
            document.querySelector('#tulostus2').innerHTML = `${amount}`;

            new_button_yes.disabled = true; // Disables the button
            new_button_yes.textContent = "tuplaa";
      }

    })
    button_no.addEventListener('click',async function(){
      document.querySelector('#tulostus2').innerHTML = `Säästit rahasi!`;
      new_button_no.disabled = true; // Disables the button
      new_button_no.textContent = "älä tuplaa";


    })
  }else if (action==='hole_in_charge'){
    document.querySelector('#tulostus2').innerHTML = `kolovastaava vei sinulta ${amount} makkaraa`;
  }else if (action==='robber'){
    document.querySelector('#tulostus2').innerHTML = `Rosvo vei sinulta ${amount}€`;

  }else if(action==='finnair_personel'){
    document.querySelector('#tulostus2').innerHTML = `${amount}`;

  }


//returns to normal screen
async function return_to_game(){
  button_yes.style.dispay='none';
  button_no.style.dispay='none';
}

}
garbage_action()





