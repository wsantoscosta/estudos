//alert("Olá");
let numeros = []
let res = document.getElementById('res')  


function adicionar(){
    
    if (res.querySelector('#resumo')){
        let ritem = document.getElementById('resumo')
        res.removeChild(ritem)
    }
    
    let aux_numero = document.getElementById('num')
    
    if (aux_numero.value.length == 0){
        alert('Erro: Preencha com um número válido.')
    } else {
        let numero = Number(aux_numero.value)
        if (numero < 1 || numero > 100 ) {
            alert('Número inválido.')
        } else {

            if (numeros.indexOf(numero) == -1){
                let selecao = document.getElementById('selecao')
                let item = document.createElement('option')
                
                item.text = `Valor ${numero} inserido`
                selecao.appendChild(item)
                numeros.push(numero)
                
            } else {
                alert(`Valor: ${numero} já existe na lista`)
            }
        }
    }
    aux_numero.value = ''
    aux_numero.focus()
    
}

function resumo(){
   
    if (numeros.length < 1) {
        alert('ERRO: Não foi informado os valores')
    } else {        
        
        let total_numeros = numeros.length
        let maior_numero = numeros[0]
        let menor_numero = numeros[0]
        let soma_numeros = 0
        
        for (let valor in numeros) {
            soma_numeros += numeros[valor]
            if ( numeros[valor] > maior_numero) {
                maior_numero = numeros[valor]
            } if (numeros[valor] < menor_numero) {
                menor_numero = numeros[valor]
            }
        }
    
        let media_numeros = soma_numeros / total_numeros

        resumo_final = `<p>Ao todo temos, <strong>${total_numeros}</strong> inseridos.</p>
                        <p>O maior número inserido foi ${maior_numero}.</p>
                        <p>O menor número inserido foi ${menor_numero}.</p>
                        <p>O total dos números inseridos foi ${soma_numeros}.</p>
                        <p>A média dos números inseridos foi ${media_numeros}.</p>`
        let item = document.createElement('div')
        item.id = 'resumo'
        item.innerHTML = resumo_final
        res.appendChild(item)
    }
}