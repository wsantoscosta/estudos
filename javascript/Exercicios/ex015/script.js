function verificar(){

    var ano_nascimento = document.getElementById('anonasc');
    var fsex = document.getElementsByName('radsex');
    var mensagem = document.getElementById('mensagem');
    var imagem = document.getElementById('imagem');
    
    var hoje = new Date();
    var ano_atual = hoje.getFullYear();
    
    var nascimento = Number(ano_nascimento.value);  

    if (nascimento < 1 || nascimento > ano_atual) {
        alert('[ERRO] Preencha os dados acima corretamente.')
    } else {
        var idade = ano_atual - nascimento

        if (fsex[0].checked) {
            mensagem.innerHTML = `Mulher com ${idade} anos.`


            if (idade < 10){
                imagem.src = 'foto-crianca-f.png'
            } else if (idade < 21){
                imagem.src = 'foto-jovem-f.png'
            } else if (idade < 51) {
                imagem.src = 'foto-adulto-f.png'
            } else {
                imagem.src = 'foto-idosa-f.png'
            }
        }
        
        if (fsex[1].checked) {
            mensagem.innerHTML = `Homem com ${idade} anos.`

            if (idade < 10){
                imagem.src = 'foto-crianca-m.png'
            } else if (idade < 21){
                imagem.src = 'foto-jovem-m.png'
            } else if (idade < 51) {
                imagem.src = 'foto-adulto-m.png'
            } else {
                imagem.src = 'foto-idoso-m.png'
            }
        }
        
    }
    
}
