## Signaling Channels

- channels can either send data through go routines or just signals. Data channels carry actual data, such as `string`, `int`, `bool`.
- signaling channels do not need to carry any data. Hence, they can (and should) be defined as empty structs.

In a signal channel, what is sent through the channel does not matter

```go
done <- false // is a valid signal
done <- true // also a valid signal
```

- However, using data as a signal unnecessarily holds space in memory (1 byte in the case of the signal)
- There is also a risk of mistakenly using the value as part of the code logic

### Appropriate way:
```go
done := make(chan struct{})
done <- struct{}{} // signal
<-done             // wait for signal

```
