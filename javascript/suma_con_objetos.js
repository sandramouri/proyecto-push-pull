/*
  Similar a kwargs en Python

  En Js se utiliza el operador de propagación "..."
*/

function sumarConKwargs(kwargs) {
  let resultado = 0;
  for (const key in kwargs) {
      if (kwargs.hasOwnProperty(key)) {
          resultado += kwargs[key];
      }
  }
  return resultado;
}

const numeros = { numero1: 10, numero2: 20, numero3: 30 };
const resultado = sumarConKwargs(numeros);
console.log(`La suma de los números es: ${resultado}`);
