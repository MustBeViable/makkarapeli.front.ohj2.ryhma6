'use strict'

const dialog_instructions = document.getElementById('instructions');
const button_instructions = document.getElementById('instructions_btn');
const close_instructions = document.getElementById('close_instructions');


button_instructions.addEventListener('click',  async(evt) => {
  dialog_instructions.showModal();
  dialog_instructions.innerHTML = `<h3>Pelin ohjeistus</h3>
                                    <p>Pelin tavoite on kerätä mahdollisimman paljon makkaroita 
                                    ja siten kerryttää pistesaalista. Makkaroita voi ostaa 
                                    lentokenttien Tax free -myymälöistä. Kullakin maalla on oma 
                                    makkaransa, ja rilaisista makkaroista saa eri määrän pisteitä. 
                                    Peli päättyy, kun sinulla ei ole enää rahaa ostaa lentolippua 
                                    tai et pysty enää tuplaamaan rahojasi. Edistymisesi tallentuu 
                                    automaattisesti.</p>
                                    
                                    <p>Jokaiselta lentokentältä voi ostaa yhden kappaleen kyseisen
                                    maan makkaraa. Saapuessasi uuteen maahan, voit koettaa onneasi
                                    roskiksessa. Tämän jälkeen, mikäli sinulla on rahaa ja tahtoa,
                                    voit vierailla kyseisen maan taxfree-myymälässä ostaaksesi makkaran.
                                    Tämän jälkeen sinun on taas lennettävä seuraavaan maahan kasvattaaksesi
                                    edelleen makkarakokoelmaa ja pistesaldoasi.</p>
                                    
                                    <h3>Pelin visio</h3>
                                    <p>Makkara Mania: Airport Adventure on humoristinen tuuria ja strategiaa 
                                    yhdistävä peli, jossa pelaaja matkustaa eri maiden lentokentille ja 
                                    kerää pisteitä ostamalla paikallisia makkaroita. Jokaisella maalla on oma 
                                    erikoismakkara, jonka voi ostaa vain kyseisen maan lentokentiltä, ja uudet 
                                    makkarat kasvattavat pelaajan pistemäärää. Pelaaja kilpailee itseään ja 
                                    muita pelaajia vastaan yrittäen ylittää aiemmat piste-ennätykset.</p>
                                    
                                    <p>Pelaaja saa pelin alussa rajoitetun määrän rahaa, jota tarvitaan 
                                    uusille lentokentille lentämiseen ja makkaroiden ostamiseen. Rahaa 
                                    voi löytää lentokenttien roskiksista, mutta roskien tonkiminen on riski: 
                                    roskakorista voi löytyä kaivattua käteistä, mutta myös vastoinkäymisiä, 
                                    kuten rosvo tai kolovastaava, jotka uhkaavat pelaajan varallisuutta ja 
                                    makkarakokoelmaa. Peli päättyy, kun pelaajan rahat loppuvat.</p>
                                    
                                    <p>Pelin maailmassa on myös erikoistapahtumia. Lentokentillä pelaaja 
                                    saattaa törmätä Finnairin ympäristöedustajaan, joka pyytää lahjoituksia. 
                                    Jos pelaaja suostuu lahjoittamaan, hänet saatetaan palkita harvinaisella 
                                    makkaralla, joka on erityisen suuren pistemäärän arvoinen. Lisäksi pelissä 
                                    on muita erikoismakkaroita, kuten legendaarinen mustamakkara, jonka voi 
                                    löytää ainoastaan päättäväisellä ja onnekkaalla roskisten kaivamisella.</p>
                                    <button id="close_instructions">Sulje</button>`
});

close_instructions.addEventListener('click', (evt) => {
  dialog_instructions.close();
});