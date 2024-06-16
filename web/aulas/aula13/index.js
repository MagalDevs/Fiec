function carregaPagina(){


fetch("https://www.w3schools.com/angular/customers.php")  // pega a url
.then(r => r.json())    // converte para json
.then(data => {
 const records = data.records;
 const tabela = document.getElementById('tabela');
 let conteudo = "";

// for i in Range(len(records))
for (i=0; i<records.length; i++){
    const record = records[i];
    /*
    conteudo += "<tr>";
    conteudo += "<td>" + record.Name + "</td>";
    conteudo += "<td>" + record.City + "</td>";
    conteudo += "<td>" + record.Country + "</td>";
    conteudo += "</tr>"; 
    */
   conteudo += `
    <tr>
        <td>${record.Name}</td>
        <td>${record.City}</td>
        <td>${record.Country}</td>
    </tr>
   `
 }
 tabela.innerHTML = conteudo;

 });  // pega os dados (data) e imprime

}

carregaPagina();