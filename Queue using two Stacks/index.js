// mplement a Queue using 2 stacks s1 and s2 .
// A Query Q is of 2 Types
// (i) 1 x (a query of this type means  pushing 'x' into the queue)
// (ii) 2   (a query of this type means to pop element from queue and print the poped element)

// import { Stack } from "./Stack";
const Stack = require('./Stack');

class StackQueue {
    constructor() {
        this.s1 = new Stack();
        this.s2 = new Stack();
    }

    /**
     * @param {number} B
    */
    
    //Function to push an element in queue by using 2 stacks.
    push(B){
        // code here
        this.s1.push(B);

    }
    
    /**
     * @returns {number}
    */
    
    //Function to pop an element from queue by using 2 stacks.
    pop(){
        // code here
        while(!this.s1.isEmpty()){
            this.s2.push(this.s1.front());
            this.s1.pop()
        }
        let temp = this.s2.front();
        console.log(temp);
        return temp;
    }

}


// Stack 
// let queue = new StackQueue();

// queue.push(1);
// queue.push(2);
// queue.push(3);
// queue.push(4);
// queue.push(5);
// queue.pop();


function main() {
    let queue = new StackQueue();

    let n = 5;
    let str = '1 2 1 3 2 1 4 2';
    let inputArr = str.split(' ').map(x => parseInt(x));
    let index = 0;
    let res = '';
    while(n--){
        let QT = inputArr[index++];
        if(QT === 1){
            
    }
    
}
