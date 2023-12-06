function carregar() {
    var mensagem = document.getElementById('msg')
    var imagem = document.getElementById('imagem')
    var hoje = new Date()
    var agora = hoje.getHours()
  
    
    mensagem.innerHTML = `Agora são ${agora} horas.`

    if (agora < 12) {
        imagem.src = 'fotomanha.png'
        document.body.style.background = '#e2cd9f'
    }else if (agora < 18){
        imagem.src = 'fototarde.png'
        document.body.style.background = '#b9846f'
        
    } else {
        imagem.src= 'fotonoite.png'
        document.body.style.background = '#515154'
    }
}
