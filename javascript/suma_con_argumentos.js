// Similar a args en Python

function sumarConArgs(...args) {
  let resultado = 0;
  for (const num of args) {
      resultado += num;
  }
  return resultado;
}

const numeros = [1, 2, 3, 4, 5];
const resultado = sumarConArgs(...numeros);
console.log(`La suma de los números es: ${resultado}`);
