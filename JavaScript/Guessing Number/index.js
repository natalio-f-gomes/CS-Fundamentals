count = 0;
const number = Math.floor(Math.random() * 10) + 1;
function Play(){
    
    let numberguessed = document.getElementById("number").value;
    let feedback = document.getElementById("feedback");
    
    if (numberguessed == number){
        alert("You guessed right, after " + count + " times");
        count = 0;

    } else{
       
        if (numberguessed<number){
            alert("Higher");
            
            count += 1;
    }
        else{
            alert("Lower");
            count += 1;
           }
        }
    console.log(count);
    console.log(number);

}

MaxNum = 20
MinNum = 1
Human_Count = 0
let num = Math.floor(Math.random() * (MaxNum-MinNum) + MinNum);
var value = ""
var numbergGessed =  document.getElementById("numberGuessed");

const higher = document.getElementById("Higher").addEventListener("click", function(){
    value = "Higher";
    Human_Count+=1
    MinNum = num+1;
    num = Math.floor(Math.random() * (MaxNum-MinNum) + MinNum);
    numbergGessed.innerHTML = num;
    });
const lower = document.getElementById("Lower").addEventListener("click", function(){
    value = "Lower";
    Human_Count+=1
    console.log(Human_Count);
    MaxNum = num-1;
    num = Math.floor(Math.random() * (MaxNum-MinNum) + MinNum);
   
    numbergGessed.innerHTML = num;
})
const correct = document.getElementById("Correct").addEventListener("click", function(){
    value = "Correct";
    alert("You guessed right, after " + Human_Count + " times");
})


