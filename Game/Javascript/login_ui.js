'use strict';

const target = document.getElementById('target');
const signInText = 'Kirjaudu';
const signUpText = 'Luo tunnus';
const signUpButtonText = 'Oletko uusi? Luo käyttäjätili'
const signInButtonText = "Onko sinulla jo tili? Kirjaudu sisään"


/**
 * Creates a button and adds an action to it.
 * @param {string} text Text on the button
 * @param {function} onClick Action on click
 */
function createButton(text, onClick) {
  const button = document.createElement('button');
  button.textContent = text;
  target.appendChild(button);
  button.addEventListener('click', onClick);
}

/**
 * Creates a form for entering screen name.
 * @param {string} value Text displayed on the submit button
 * @param {boolean} signin Is this sign in or sign up
 */
function createNameForm(value, signin) {
  const formHtml = `
    <form id="nameForm">
      <input id="nameQuery" name="q" type="text" placeholder="Käyttäjätunnus">
    </form>
  `;
  target.innerHTML += formHtml;

  const screenNameForm = document.getElementById('nameForm');

  if (!signin) {
    const input2 = document.createElement('input');
    input2.type = 'text';
    input2.name = 'shoeSize';
    input2.placeholder = 'Kengännumero';
    screenNameForm.appendChild(input2);
  }
    const submitButton = document.createElement('input');
    submitButton.type = 'submit';
    submitButton.value = value;
    screenNameForm.appendChild(submitButton);


  screenNameForm.addEventListener('submit', async (event) => {
    const screenName = document.getElementById('nameQuery').value;
    event.preventDefault();
    await openProfile(screenName, signin);
  });
}


/**
 * Creates the sign-in page with screen name form and a button that takes user to sign-up page.
 */
function createSigninPage() {
  createNameForm(signInText, true);
  function goToSignUp() {
    target.innerHTML = ''
    createSignupPage()
  }
  createButton(signUpButtonText, () => goToSignUp())
}

/**
 * Creates the sign-up page with screen name form, extra form, and a button that takes user to sign-in page.
 */
function createSignupPage() {
  createNameForm(signUpText, false);
  function returnToSignIn(){
    target.innerHTML = ''
    createSigninPage()
  }
  createButton(signInButtonText, ()=> returnToSignIn())
}


