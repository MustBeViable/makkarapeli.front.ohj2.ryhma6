//test file for function that gets money

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
//when player id works put it in parameters to getmoney
async function getMoney(){

    const url = `http://127.0.0.1:5000/player_money/1`

    try{
        const result = await  getData(url)

        const value = result.money

        if(value > 0){
            console.log("insidefunction"+ value)
        }

        return value

    }
    catch (error){
        return error
    }
}
// needs some way to make this return a number
//it returns

const res = getMoney()

console.log("outside"+ res)