## Python Generators

- Python generators are a special type of function that returns an iterator that can be used to iterate through values.
- It uses the `yield` keyword instead of `return`

### How Generators Work

1. `Lazy Evaluation` - Generators produce values on demand, only when needed. This makes them memory efficient. In comparison, normal functions produce all values at once, uses memory to store the values.
2. `State Retention` - When a generator encounters the `yield` keyword, it saves its internal state, including execution position and internal variables, and resumes the next time it is called.
3. `Iterator Protocol` - generators implement the iterator protocol, meaning they have the `__next__()` method. Meaning they can be used with iterators such as `for loops`.
4. `Yield keyword` - generators use the `yield` keyword which produces a value and pauses execution. It returns to its present state when the generator is called again.
5. `Generator Object` - When a generator function is called, it doesn't execute immediately. Instead, it returns a generator object, which is an iterator.

### Example

```python
   def my_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = my_generator(5)

for value in gen:
    print(value)

# Output:
# 0
# 1
# 2
# 3
# 4
```

### Key Differences with Normal Functions

1. `Return vs Yield`

| Feature           | `return`                            | `yield`                    |
| ----------------- | ----------------------------------- | -------------------------- |
| Stops function?   | Yes                                 | No — pauses and can resume |
| Values produced   | One                                 | Many (lazy sequence)       |
| Memory efficiency | Not memory efficient for large data | Very efficient             |
| Function type     | Regular function                    | Generator function         |

2. `state`

Regular functions lose their state after returning. Generators retain their state between successive yield statements.
Usually, a normal funcction exits after the `return` statement and everything after is not reachable. In comparison, code after `yield` can still be executed as in the examples below.

#### Example 1: Using yield
```python
def yield_example():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")

gen = yield_example()

for val in gen:
    print("Received:", val)

# Output:
  # Start
  # Received: 1
  # After first yield
  # Received: 2
  # After second yield
```
`Explanation:`

- "Start" is printed at the start.

- First yield 1 pauses the function and gives control to the loop.

- "After first yield" is run when the loop calls next() again.

- This continues until the generator is exhausted.

#### Example 2: Using return
```python
def return_example():
    print("Start")
    return 1
    print("This will NOT run")
    return 2

val = return_example()
print("Received:", val)

# Output:
  # Start
  # Received: 1
```

`Explanation:`

- "Start" is printed.

- return 1 ends the function.

- The line print("This will NOT run") is never reached.

### Generators Use Cases
1. `Working with large datasets:` Generators can process large datasets without loading them entirely into memory.
2. `Creating infinite sequences:` Generators can produce infinite sequences of values, such as the Fibonacci sequence.
3. `Stream processing:` Generators can handle data streams, processing each item as it arrives.
4. `Generating synthetic data:` Generators can create synthetic data for testing and development.
5. `Simplifying complex logic:` Generators can help simplify code by breaking down complex logic into smaller, manageable parts.
