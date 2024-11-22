'use strict';

const div_test = document.querySelector('#target');

const test_button = document.createElement('button');

test_button.textContent = 'query';

div_test.appendChild(test_button);

test_button.addEventListener('click', async () => {
  const url = 'http://127.0.0.1:5000/airport/?ide=1';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    let TestJSON = response.json();
    for (let i = 0; i < 19; i++) {
      let article = document.createElement('article');
      let paragraph = document.createElement('p');
      i.toString();
      paragraph.textContent = TestJSON.i;
      article.appendChild(paragraph);
      div_test.appendChild(article);
    }
  } catch (error) {
    console.log(error.message);
  }
});