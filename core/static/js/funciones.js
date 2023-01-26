function edad(){
    var edad,resultado; 
    edad= prompt('Ingrese la edad de tu gatito');
    if(parseInt(edad)<=2){
        resultado = parseInt(edad)*12.5;
        alert('La edad de tu gato en años humanos es: '+resultado);
    }
    else{
        resultado = 24 + (parseInt(edad)-2) *4;
        alert('La edad de tu gato en años humanos es: '+resultado);
    }
}

function Saludo(){
    alert("Sabías que un gato puede llegar a dormir hasta 16 horas al día?");
}

function Mostrar(){
    var nom="Créme Puff";
    var edad=38;
    document.write('Su nombre fue ' +nom);
    
    document.write(' y murió a los: ' + edad +' años de edad');
}

//funcion que ingresa datos
function Ingresar(){
    var nom, edad; 
    nom = prompt('Ingrese su nombre ');
    edad= prompt('Ingrese su edad ');
    document.write('El nombre de tu gato es: ' + nom + ' y tiene: ' + edad + ' años de edad');
}

function Saludar(){
    alert("Te deseamos un feliz año a ti y tu gato :)");
}

const URL = 'http://api.thecatapi.com/v1/images/search';
fetch(URL)
    .then(res => res.json())
    .then(data => {
        
        const img = document.querySelector('img');
        img.src = data[0].url;
        
    });