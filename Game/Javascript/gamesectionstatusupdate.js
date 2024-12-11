

async function gamesectionstatusupdate(section,status){

  try{
    const url = `http://127.0.0.1:5000/update_status/${ide}/${section}/${status}`
    const result = getData(url)

  }
  catch (error){
    console.log(error)
  }

}