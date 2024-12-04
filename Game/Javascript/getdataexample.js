//test file for function that gets data
'use strict'
//returns raw data
async function getData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
        return data
    } catch (error) {
        return error
    }
}