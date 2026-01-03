let equation = document.getElementById("equation")

function factorial(n) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  
let one = document.getElementById("1").onclick = function(){
    equation.value+=1
    
}
let two = document.getElementById("2").onclick = function(){
    equation.value += 2
}
let three= document.getElementById("3").onclick = function(){
    equation.value+=3
}
let four= document.getElementById("4").onclick = function(){
    equation.value+=4
}
let five = document.getElementById("5").onclick = function(){
    equation.value+=5
}
let six = document.getElementById("6").onclick = function(){
    equation.value+=6
}
let seven  =document.getElementById("7").onclick = function(){
    equation.value+=7
}
let eight = document.getElementById("8").onclick = function(){
    equation.value+=8
}
let nine = document.getElementById("9").onclick = function(){
    equation.value+=9
}
let zero = document.getElementById("0").onclick = function(){
    equation.value+=0
}
let equal= document.getElementById("equal").onclick = function(){
    result = eval(equation.value)
    equation.value = result
}
let ac=document.getElementById("AC").onclick = function(){
    equation.value=""
}
let prime = document.getElementById("Prime").onclick = function() {
    let number = parseInt(equation.value);
    let squareRoot = Math.floor(Math.sqrt(number));
    let isPrime = true;

    for (let i = 2; i <= squareRoot; i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }

    equation.value = isPrime;
}
let factorial_ = document.getElementById("factorial").onclick = function(){
    let inputValue = parseInt(equation.value)
    let result = factorial(inputValue)
    equation.value = result

    }

let minus = document.getElementById("-").onclick = function(){
    equation.value+="-"
}
let plus = document.getElementById("+").onclick = function(){
    equation.value+="+"
}
let devide = document.getElementById("/").onclick = function(){
    equation.value+="/"
}
let decimal = document.getElementById(".").onclick = function(){
    equation.value+="."
}
let sqaured = document.getElementById("Squared").onclick = function(){
    result = (equation.values)**2
    equation.value= result
}
let times = document.getElementById("x").onclick = function(){
    equation.value+="*"
}


/*
document.getElementById('myButton').onclick = function(){
    username = document.getElementById("myText").value;
    document.getElementById("myName").innerHTML = "Hello "+ username
}
function equation(){
    
}*/
