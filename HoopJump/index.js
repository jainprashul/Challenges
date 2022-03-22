// cat input.txt | node index.js

// https://www.codechef.com/LP1TO201/problems/HOOPS

// t1 Tastiness & T2 Tastiness 0 to N 
// t1 + t2 = S
// 0 ≤ T1,T2≤ N

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

            let res = Hoops(a);
            console.log(res);
            
        }
          
    });
}

// N hoops |(|odd)
// 1 - n 
// 2 - n-1
// r - n-r

function Hoops(n){
    let ptr1 = 1;
    let ptr2 = n;

    return Math.floor(n/2) + 1;

    // while (n > 0){
    //     if (ptr1 === ptr2){
    //         return ptr1;
    //     }
    //     ptr1++;
    //     ptr2--;
    //     n--;
    // }
        
}


start();
