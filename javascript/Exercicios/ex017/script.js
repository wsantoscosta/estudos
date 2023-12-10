function calcular() {
    let tab = document.getElementById('seltab')
    let num = document.getElementById('numero')
    if (num.value.length == 0) {
        window.alert('Erro! Digite um número.')
    } else {
        let cnum = Number(num.value)
        tab.innerHTML = ''
        for (let contador = 1; contador <= 10; contador++) {
            let item = document.createElement('option')
            item.text = `${cnum} x  ${contador} =  ${cnum * contador}`
            item.value = `tab${contador}`
            tab.appendChild(item)
        }   
    }
}
