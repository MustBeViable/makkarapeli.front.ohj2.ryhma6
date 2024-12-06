//test function that formats airport selection buttons

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

async function format_airportselectionbuttons(){




}