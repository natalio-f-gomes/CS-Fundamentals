document.getElementById("Roll").onclick = function(){
    let x = Math.floor(Math.random()*6)+1 //random number between 0 and 6;
    let y = Math.floor(Math.random()*6)+1 //random number between 0 and 6;
    let z = Math.floor(Math.random()*6)+1 //random number between 0 and 6;

    document.getElementById("xlabel").innerHTML = x;
    document.getElementById("ylabel").innerHTML = y;
    document.getElementById("zlabel").innerHTML = z;
}
