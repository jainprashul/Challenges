class Stack {
    constructor () {
        this.arr = [];
        this.top = -1;
    }

    push (value) {
        this.arr.push(value);
        this.top++;
        // console.log(this.arr);
    }

    pop () {
        this.top--;
        this.arr.pop();
    }

    front () {
        return this.arr[this.top];
    }

    isEmpty () {
        return this.top === -1;
    }
}

module.exports = Stack;