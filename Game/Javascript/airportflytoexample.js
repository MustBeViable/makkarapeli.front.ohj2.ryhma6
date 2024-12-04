//test for function that chooses one of the 20 airports and sends info to backend inside the get
//inside this function get money is needed to check if player has money to travel or maybe the check is in the event listener. probably in the event listener.
'use strict'
//same as get data example
async function getData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data
    } catch (error) {
        return error
    }
}

async function getAirports(){

    const url = "http://127.0.0.1:5000/airport/1"
    try {
        const result = await getData(url)
        console.log(result)
        return result

    }
    catch (error){

        return error
    }
}



// flyto func will get ide and number from 1 to 20 as parameters and fly to airport with directory key == parameter
//from what i understand backend will store the 20 airports user GETs with getArport and when user calls with flyto backend will flyto the selected one
async function flyto(airport_num){
    //again needs IDE functionality
    //will add later
    try {

        const url = `http://127.0.0.1:5000/airport_selected/1/${airport_num}`
        const result= await getData(url)

        return result;
    }
    catch (error){
        return error
    }
}


// there can be problems with flyto happening before getAirports
// so basically flyto uses the table stored in python while getairports does a bigger mysql query so its slower
// using .then( ) it should work but it doesnt
// i have to use these inside a async function i thinc that will work




