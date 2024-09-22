let myText = '';
let myTextRoot = 'Olá, meu nome é Roberto 😁. Sou estudante e um entusiasta apaixonado por programação 👨🏽‍💻. Desenvolvi este sistema com o intuito de demonstrar um pouco das minhas habilidades em web scraping, utilizando a linguagem de programação Python🐍. Se você gostou deste projeto ou despertou seu interesse, fique à vontade para entrar em contato comigo. Seguem meus contatos:';
const timeAleatorio = [10,50,150,10];

function digitandoTexto() {
    const textSobre = document.querySelector("div.sobre > p");// Selecionar um item aleatório do array
    const itemAleatorio = timeAleatorio[Math.floor(Math.random() * timeAleatorio.length)];

    console.log(myTextRoot.startsWith(myText))

    if (myTextRoot.startsWith(myText)) {
        const nextChar = myTextRoot[myText.length];
        myText=`${myText}${nextChar}`
        textSobre.innerText = myText;
    } else {
        myText=`${myTextRoot[0]}`
        textSobre.innerText = myText;
    }

    if (myText.length === myTextRoot.length) {
        return false
    } else {
        setTimeout(digitandoTexto,itemAleatorio);
    }
}

document.addEventListener("DOMContentLoaded",()=>{
    const inputUsername = document.getElementById("username");
    const iframe = document.getElementById("iframe-instagram");

    inputUsername.addEventListener("change",()=>{
        iframe.src = `perfil/${inputUsername.value}`;
    });

    setTimeout(digitandoTexto,500);
});