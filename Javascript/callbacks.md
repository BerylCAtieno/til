## Callbacks

### What is a callback?

A **callback** is just a **function passed as an argument** to another function so that it can be **called later**.

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

function processUserInput(callback) {
  const name = "Beryl";
  callback(name);
}

processUserInput(greet); // Hello, Beryl!
```

Here, `greet` is a **callback** passed to `processUserInput`.

---

## Callbacks as anonymous functions

You don’t have to pass a named function — you can pass an **inline anonymous function**.

```javascript
function processUserInput(callback) {
  const name = "Beryl";
  callback(name);
}

processUserInput(function(name) {
  console.log(`Hello, ${name}!`);
});
```

---

## Callbacks as arrow functions

Same thing — but more modern:

```javascript
processUserInput((name) => {
  console.log(`Hello, ${name}!`);
});
```

---

## Callbacks for reusable logic

A function can **use a callback to decide what to do**.

```javascript
function doOperation(x, y, operation) {
  return operation(x, y);
}

function add(a, b) {
  return a + b;
}

function multiply(a, b) {
  return a * b;
}

console.log(doOperation(5, 3, add)); // 8
console.log(doOperation(5, 3, multiply)); // 15
```

---

## Callbacks in built-in functions

Many **JS built-in methods** use callbacks: `forEach`, `map`, `filter`.

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6]
```

👉 The function `num => num * 2` is the callback for `.map`.

---

## Callbacks for asynchronous code

The original use: **handling results that come later**.
Example: `setTimeout` — run a callback after a delay.

```javascript
console.log("Before");

setTimeout(() => {
  console.log("This runs later");
}, 1000);

console.log("After");
```

---

## Callbacks with error handling (error-first pattern)

In Node.js and older async code, callbacks usually take an **error as the first argument**.

```javascript
function getData(callback) {
  const error = null; // or: new Error("Something went wrong");
  const data = "Important data";

  callback(error, data);
}

getData((err, result) => {
  if (err) {
    console.error("Error:", err);
  } else {
    console.log("Result:", result);
  }
});
```

 **Pattern:** `(err, result) => { ... }`

---

## Callback hell

When you **nest callbacks inside callbacks**, code can get messy:

```javascript
doStep1(function(result1) {
  doStep2(result1, function(result2) {
    doStep3(result2, function(result3) {
      console.log("Done:", result3);
    });
  });
});
```

This is called **callback hell** — it’s why Promises and `async/await` exist.
But you can still manage it with **good naming**, **splitting functions**, or **flattening**.

---
