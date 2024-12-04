

//test for getting the data of 20 airports from backend
//missing IDE functionality
'use strict'
//same as get data example
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

async function getAirports(){

    const url = "http://127.0.0.1:5000/airport/1"
    try {
        return await getData(url)

    }
    catch (error){

        return error
    }
}

//works
//get airports returns a dictionary of dictionarys

