// cat input.txt | node index.js

// https://www.codechef.com/LP1TO201/problems/IMDB


function start(){
    process.stdin.resume();
    process.stdin.setEncoding('utf-8');
    var arr = "";
    process.stdin.on('data', function(chunk) {
        arr += chunk;
    });
    process.stdin.on('end', function() {
        arr = arr.split("\n");
        var n = parseInt(arr.shift());
         // in order ot get no of test cases

        let i = 0;
        while(arr.length > 1){
            let str = arr.shift();
            // console.log("str",str);
            let n=parseInt(str.split(" ")[0]); //get first no
            let x=parseInt(str.split(" ")[1]);// get second no
            // let list = [];

            let max = 0;

            for (let i = 0; i < n; i++) {
                let str = arr.shift();
                // console.log("str1",str);
                let s=parseInt(str.split(" ")[0]); //get first no
                let r=parseInt(str.split(" ")[1]);// get second no
                
                if(s <= x){
                    max = Math.max(max, r);
                }
            }
        
            
            // let res = Motivation(n,x,list);
            console.log(max);
            
        }
          
    });
}

// n - no of movies
// x - size max
// list contain size of movies and their ratings

function Motivation(n , x , l){
    // let temp = [];
    let max = 0;

    for (const arr of l) {
        let s = arr[0];
        let r = arr[1];

        // console.log("s",s, r);

        // temp will contain the list of movies with ratings less than x size
        if(s <= x){
            max = Math.max(max, r);
        }
    }

    // max will contain the max rating of movies with size less than x
    return max;
}

start();


// 6057 70713