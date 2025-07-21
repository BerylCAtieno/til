## String Formatting in Javascript

### ✅ **1. Basic concatenation**

The classic way — using `+` operator:

```javascript
const name = "Beryl";
const message = "Hello, " + name + "!";
console.log(message); // Hello, Beryl!
```

---

### ✅ **2. Template literals (the modern way)**

**Recommended**. Use backticks `` ` `` and `${}` for embedding expressions.

```javascript
const name = "Beryl";
const age = 25;
const message = `Hello, ${name}! You are ${age} years old.`;
console.log(message); // Hello, Beryl! You are 25 years old.
```

---

### ✅ **3. Using `String.prototype.replace`**

For simple replacements with placeholders:

```javascript
const template = "Hello, NAME!";
const message = template.replace("NAME", "Beryl");
console.log(message); // Hello, Beryl!
```

Or with regex for multiple same placeholders:

```javascript
const template = "Hi, NAME. Bye, NAME.";
const message = template.replace(/NAME/g, "Beryl");
console.log(message); // Hi, Beryl. Bye, Beryl.
```

---

### ✅ **4. Format function (DIY)**

JavaScript doesn’t have a built-in `format` method like Python.
But you can easily make one:

```javascript
function format(str, ...args) {
  return str.replace(/{(\d+)}/g, (match, number) => 
    typeof args[number] !== 'undefined' ? args[number] : match
  );
}

const message = format("Hello, {0}. You have {1} messages.", "Beryl", 5);
console.log(message); // Hello, Beryl. You have 5 messages.
```

---

### ✅ **5. Internationalization (for numbers, dates)**

For formatted dates/numbers:

```javascript
const number = 1234567.89;
console.log(new Intl.NumberFormat('en-US').format(number)); // 1,234,567.89

const date = new Date();
console.log(new Intl.DateTimeFormat('en-GB').format(date)); // e.g. 21/07/2025
```

---

