let x = Math.floor(Math.random()*6)+1;
let y = Math.floor(Math.random()*6)+1;
let z = Math.floor(Math.random()*6)+1;
let lst = [1,2,3,4];



const uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
const digits = [1,2,3,4,5,6,7,8,9,0];
const ponctuation = ['!', "''", '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', "]", "^", "_", '`', '{', '|', '}', "~"]
const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';




decrement = document.getElementById("decrement").onclick = function(){
    let len =  document.getElementById("lenght").value-=1
    if(len<9){
        window.alert("Lentgh cannot be less than 8")
        let len =  document.getElementById("lenght").value = 8
    }
 
}

increment = document.getElementById("increment").onclick = function(){
    let len =  parseInt(document.getElementById("lenght").value) + 1
    
    if(isNaN(len)){

        document.getElementById("lenght").value = 8
       
    }else{
        document.getElementById("lenght").value = len
    
    }
    
}
generate = document.getElementById("generate").onclick = function() {
  let empty = document.getElementById("display").value = "";
  let len = document.getElementById("lenght").value;
  let password = "";

  for (let i = 0; i < len; i++) {
    let random_index = Math.floor(Math.random() * characters.length);
    console.log(random_index)
    password += characters[random_index];

  }

  document.getElementById("display").value = password;
}
