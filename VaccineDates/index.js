// cat input.txt | node index.js

// https://www.codechef.com/LP1TO201/problems/VDATES

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
            var b=parseInt(arr[i].split(" ")[1]);// get second no
            var c=parseInt(arr[i].split(" ")[2]);// get second no
            
            let res = VDATES(a,b,c);
            console.log(res);
            
        }
          
    });
}

// first doese D - days agos
//  second doese - no less than L days and no more than R days 
function VDATES(D , L , R) {
//     Too Late
// Too Early
// Take second dose now

    if(D < L){
        return "Too Early";
    } else if(D > R){
        return "Too Late";
    } else {
        return "Take second dose now";
    }
}

start();
