'use strict';

const loginBase = document.getElementById('login_target');
const loginHeader = document.getElementById('loginheader');
const signInText = 'Kirjaudu';
const signUpText = 'Luo tunnus';
const signUpButtonText = 'Oletko uusi? Luo käyttäjätili';
const signInButtonText = 'Onko sinulla jo tili? Kirjaudu sisään';
const signInHeader = 'Kirjaudu sisään';
const signUpHeader = 'Rekisteröidy';

/**
 * Creates a button and adds an action to it.
 * @param {string} text Text on the button
 * @param {function} onClick Action on click
 */
function createLoginButton(text, onClick) {
  const loginButton = document.createElement('button');
  loginButton.textContent = text;
  loginBase.appendChild(loginButton);
  loginButton.addEventListener('click', onClick);
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
  loginBase.innerHTML += formHtml;

  const screenNameForm = document.getElementById('nameForm');

  if (!signin) {
    const extraformInput = document.createElement('input');
    extraformInput.type = 'text';
    extraformInput.name = 'shoeSize';
    extraformInput.placeholder = 'Kengännumero';
    screenNameForm.appendChild(extraformInput);
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
  loginHeader.innerText = signInHeader;
  createNameForm(signInText, true);

  function goToSignUp() {
    loginBase.innerHTML = '';
    createSignupPage();
  }
  createLoginButton(signUpButtonText, () => goToSignUp());
}

/**
 * Creates the sign-up page with screen name form, extra form, and a button that takes user to sign-in page.
 */
function createSignupPage() {
  loginHeader.innerText = signUpHeader;
  createNameForm(signUpText, false);

  function returnToSignIn() {
    loginBase.innerHTML = '';
    createSigninPage();

  }
  createLoginButton(signInButtonText, () => returnToSignIn());
}