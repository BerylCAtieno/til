
## 📌 JavaScript `map`, `filter`, `reduce` Cheat Sheet

---

### ✅ `map()`

**Use:** Transforms **each element** in an array and returns a **new array** of the same length.

**Syntax:**

```js
const newArray = array.map(callback);
```

**🔹 Simple Example:**

```js
const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2);
// [2, 4, 6]
```

**🔹 More Complex Example:**

```js
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const usernames = users.map(user => user.name.toUpperCase());
// ["ALICE", "BOB"]
```

---

### ✅ `filter()`

**Use:** Returns a **new array** with **only the elements that pass** the test (return `true` in callback).

**Syntax:**

```js
const newArray = array.filter(callback);
```

**🔹 Simple Example:**

```js
const nums = [1, 2, 3, 4, 5];
const evens = nums.filter(n => n % 2 === 0);
// [2, 4]
```

**🔹 More Complex Example:**

```js
const tasks = [
  { id: 1, done: true },
  { id: 2, done: false }
];

const completed = tasks.filter(task => task.done);
// [{ id: 1, done: true }]
```

---

### ✅ `reduce()`

**Use:** Reduces an array to **a single value** by applying a function to each element & an accumulator.

**Syntax:**

```js
const result = array.reduce((accumulator, currentValue) => {
  // do something
  return newAccumulator;
}, initialValue);
```

**🔹 Simple Example:**

```js
const nums = [1, 2, 3, 4];
const sum = nums.reduce((total, n) => total + n, 0);
// 10
```

**🔹 More Complex Example:**

```js
const purchases = [
  { item: "Book", price: 10 },
  { item: "Pen", price: 2 },
  { item: "Bag", price: 25 }
];

const totalCost = purchases.reduce((total, purchase) => {
  return total + purchase.price;
}, 0);
// 37
```

Or count occurrences:

```js
const fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];

const counts = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});

// { apple: 3, banana: 2, orange: 1 }
```

---

## 🔑 **Quick Reminders**

* `map` → same length, new values
* `filter` → same or shorter length, elements that pass test
* `reduce` → any single value: number, string, object, array, etc.

---

## ✔️ **Bonus Tip**

You can **chain** them:

```js
const nums = [1, 2, 3, 4, 5];

const result = nums
  .filter(n => n % 2 !== 0) // [1, 3, 5]
  .map(n => n * 2)          // [2, 6, 10]
  .reduce((sum, n) => sum + n, 0); // 18
```

---

