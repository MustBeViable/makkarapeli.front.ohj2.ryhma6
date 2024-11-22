'use strict';

//EI LOPPUOHJELMAAN TÄTÄ!!!!

const div_test = document.querySelector('#target');

const test_button = document.createElement('button');

test_button.textContent = 'query';

div_test.appendChild(test_button);

test_button.addEventListener('click', async function () {
  const url = 'http://127.0.0.1:5000/airport/1';
  try {
    let response = await fetch(url);
    console.log(response);
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    let TestJSON = await response.json();
    console.log(TestJSON);
    console.log(TestJSON['1'])
    for (let i = 0; i <= 19; i++) {
      let article = document.createElement('article');
      let paragraph = document.createElement('p');
      paragraph.textContent = TestJSON[`${i+1}`].name;
      article.appendChild(paragraph);
      div_test.appendChild(article);
    }
  } catch (error) {
    console.log(error.message);
  }
});