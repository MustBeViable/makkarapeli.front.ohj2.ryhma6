'use strict'

const dialog_instructions = document.getElementById('instructions');
const button_instructions = document.getElementById('instructions_btn');


button_instructions.addEventListener('click',  async(evt) => {
  dialog_instructions.showModal();
  dialog_instructions.innerHTML = `<div class="game_board_inst">
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    </div>
                                    <h3>Pelin ohjeistus</h3>
                                    <p>Pelin tavoitteena on kerätä mahdollisimman paljon makkaroita 
                                    ja siten maksimoida pistesaalista. Makkaroita voi ostaa 
                                    lentokenttien Tax free -myymälöistä. Kullakin maalla on oma 
                                    makkaransa, ja erilaisista makkaroista saa eri määrän pisteitä. 
                                    Peli päättyy, kun pelaajalla ei ole enää rahaa ostaa lentolippua.
                                    Pelaaja kilpailee itseään ja 
                                    muita pelaajia vastaan yrittäen ylittää aiemmat piste-ennätykset. 
                                    Pelaajan edistyminen tallentuu automaattisesti.</p>
                                    
                                    <p>Saapuessa uuteen maahan, voi pelaaja koettaa onneaan
                                    penkomalla roskista. Pelaajalla on mahdollisuus ansaita lisää rahaa, 
                                    mutta toisaalta riski menettää osan rahoista tai jo kerätyistä 
                                    makkaroista. Tämän jälkeen pelaajan on mahdollista vierailla kyseisen maan 
                                    taxfree-myymälässä ostaakseen kyseisen maan makkaran. Taxfreen 
                                    jälkeen pelaajan on taas lennettävä seuraavaan maahan
                                    kasvattaakseen edelleen makkarakokoelmaa ja pistesaldoaan.</p>
                                    
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

const dynamicCloseBtn = document.getElementById('close_instructions');

dynamicCloseBtn.addEventListener('click', (evt) => {
  dialog_instructions.close();
  console.log('Instructions closed');
  });
});