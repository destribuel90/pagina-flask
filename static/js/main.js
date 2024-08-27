const form = document.querySelector('#miFormulario');
const button = document.querySelector("input[type='button']");
const div = document.querySelector('div');
let datos = {};
button.addEventListener('click', ()=>{
    const formulario = new FormData(form);
    formulario.forEach((value,key)=>{
        datos[key] = value;
    });
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(datos) 
    };
    fetch("http://127.0.0.1:3000/index",options)
    .then(ren => ren.json())
    .then(response => {
    const p = document.createElement('p');
    const Content = "Mensaje:"+ response['message'];
    p.textContent = Content;
    div.appendChild(p);
    })
    .catch(error => {
            error.json().then(errorData =>{
                const message = errorData['message'];
                console.error('Error:', message);
        })
    });
});





