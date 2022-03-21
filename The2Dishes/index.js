// cat input.txt | node index.js

// https://www.codechef.com/LP1TO201/problems/MAX_DIFF

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
            var b=parseInt(arr[i].split(" ")[1]);// get second no
            
            let res = MaxDifference(a,b);
            console.log(res);
            
        }
          
    });
}

// N - max  between tastiness of two dishes
// S - total tastiness of dishes

function MaxDifference(N , S){
    let maxdif = 0;
    let minEle = 0;

    let min = Math.min(N,S);

    for (let i = min; i >= 0; i--) {
        let t2 = S - i;
        if( i - t2 > maxdif){
            maxdif = i - t2;
        }
        if(i <= minEle){
            minEle = i;
        }
    }

    return maxdif;
}

start();


// 6057 70713