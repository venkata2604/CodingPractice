// write a fibonacci series in javascript
// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

function fib(n) {
    if (n < 2) {
        return 1;
    }
    return fib(n-2) + fib(n-1);
}

for (var i = 0; i < 60000; i++) {
    console.log(fib(i));
}

