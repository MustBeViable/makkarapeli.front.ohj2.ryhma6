'use strict';

import {openProfile} from './profile.js';

const target = document.getElementById('target');
const signInText = 'Kirjaudu';
const signUpText = 'Luo tunnus';
const signUpButtonText = 'Oletko uusi? Luo tili tästä'
const signInButtonText = "Oletko jo käyttäjä? Kirjaudu sisään"


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
      <input type="submit" value="${value}">
    </form>
  `;
  target.insertAdjacentHTML('beforeend', formHtml);

  const screenNameForm = document.getElementById('nameForm');
  screenNameForm.addEventListener('submit', async (event) => {
    const screenName = document.getElementById('nameQuery').value;
    event.preventDefault();
    await openProfile(screenName, signin);
  });
}

/**
 * Creates an extra form for sign up page.
 */
function createExtraFrom() {
  const extraForm = document.createElement('input');
  extraForm.id = 'extraForm';
  extraForm.placeholder = 'Kengännumero';
  target.appendChild(extraForm);
}

/**
 * Creates the sign-in page.
 */
export function createSigninPage() {
  createNameForm(signInText, true);
  function goToSignUp() {
    target.innerHTML = ''
    createSignupPage()
  }
  createButton(signUpButtonText, () => goToSignUp())
}

/**
 * Creates the sign-up page.
 */
export function createSignupPage() {
  createNameForm(signUpText, false);
  createExtraFrom();
  function returnToSignIn(){
    target.innerHTML = ''
    createSigninPage()
  }
  createButton(signInButtonText, ()=> returnToSignIn())
}