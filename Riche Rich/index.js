// https://www.codechef.com/LP1TO201/problems/CHFRICH

// asset A 
// increase the value of the asset A by X per year
// alleast B amt required

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
            var x=parseInt(arr[i].split(" ")[2]);// get second no
            
            let res = calcYear(a,b,x);
            console.log(res);
            
        }
          
    });
}

function calcYear(A , B , X){
    var c=0;
    while(A<B){
        A=A+X;
        c++;
    }
    return c;
}

start();