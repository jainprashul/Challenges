// cat input.txt | node index.js

// https://www.codechef.com/LP1TO201/problems/TWODISH

function start(){
    process.stdin.resume();
    process.stdin.setEncoding('utf-8');
    var arr = "";
    process.stdin.on('data', function(chunk) {
        arr += chunk;
    });
    process.stdin.on('end', function() {
        arr = arr.split("\n");
        var n = parseInt(arr.shift()); // in order ot get no of test cases
        for(let i=0;i<n;i++){ //loop through no of test cases.
            var a=parseInt(arr[i].split(" ")[0]); //get first no
            var b=parseInt(arr[i].split(" ")[1]); 
            var c=parseInt(arr[i].split(" ")[2]); 
            var d=parseInt(arr[i].split(" ")[3]); 

            let res = TWODISH(a,b,c,d);
            console.log(res);
            
        }
    });
}

// N - guest 
// A  - fruits
// B  - vegetables
// C - fishes

// 2 types of dishes - 
// 1. fruits and vegetables
// 2. vegetables and fishes

// check if N dishes can be made from A,B,C

function TWODISH(N,A,B,C ){
    if (B >= N  && (A + C) >= N ) { 
        return "YES";
    }
    
    return "NO";

}

start();