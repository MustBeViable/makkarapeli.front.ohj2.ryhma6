'use strict';

const div = document.querySelector('div');

const button = document.querySelector('#target');

button.addEventListener('click', async function test(evt) {
  try {
    const resposne = await fetch(`http://127.0.0.1:5000/garbage/1`);
    console.log(resposne);
    const result = await resposne.json();
    console.log(result);
    const p = document.createElement('p');
    p.textContent = `${result}`;
    div.appendChild(p);
  } catch (error) {
    console.log(error);
  }

});