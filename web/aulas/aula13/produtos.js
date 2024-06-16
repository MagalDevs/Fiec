function carregaProdutos() {
    fetch("http://localhost:3000")
    .then(r => r.json())
    .then(data => {
        const produtosSection = document.getElementById("produtos");
        let conteudo = "";
        const produtos = data;
        for(i=0; i<produtos.length; i++){
            const produto = produtos[i];
            conteudo += `
            <div class="card">
            <img src="${produto.Imagem}" alt="Avatar">
            <div class="container">
              <h4><b>${produto.Preco}</b></h4>
              <p>${produto.Nome}</p>
            </div>
            </div>
            `
        }
        produtosSection.innerHTML = conteudo;
    })
}

carregaProdutos();