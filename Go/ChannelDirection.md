When you declare a channel:

```go
ch := make(chan struct{})
```

`chan struct{}` means **a bidirectional channel** — you can both send **and** receive on it.

But in a **function parameter**, you can be explicit and say:

* **Receive-only channel:**

  ```go
  start <-chan struct{}
  ```

  This means: *Inside this function, you can only read from (`<-`) this channel.*
  Sending will be a compile-time error.

* **Send-only channel:**

  ```go
  next chan<- struct{}
  ```

  This means: *Inside this function, you can only send to this channel.*
  Receiving will be a compile-time error.

---

## **Why this is useful**

1. **Safety** — prevents accidental misuse of channels.
   Example:

   ```go
   func worker(input <-chan int, output chan<- int) { ... }
   ```

   This makes it impossible for `worker` to send to `input` or receive from `output` by mistake.

2. **Clearer intent** — the function signature tells you exactly how data is flowing.

   * `input <-chan int` → “I’m only reading from here.”
   * `output chan<- int` → “I’m only writing here.”

3. **Better API design** — helps others use your functions correctly without reading all the code.

---

## **Analogy**

Think of a channel like a **pipe**:

* `chan T` → You have a pipe that you can both pour water into and drink from.
* `<-chan T` → You only have the drinking end.
* `chan<- T` → You only have the pouring end.

---

## **Quick example**

```go
func sender(ch chan<- string) {
    ch <- "hello"    //  allowed
    // fmt.Println(<-ch) // compile error
}

func receiver(ch <-chan string) {
    fmt.Println(<-ch) //  allowed
    // ch <- "hi"      //  compile error
}

func main() {
    ch := make(chan string)

    go sender(ch)
    receiver(ch)
}
```

---

If you like, I can **rewrite your exercise 1** with comments showing exactly how `<-chan` and `chan<-` protect your channel usage so you can see the benefit in practice.
Want me to do that?
