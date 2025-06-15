# Today I Learned: The Circuit Breaker Pattern

## What is the Problem it Solves?

In distributed systems, services often depend on other services (e.g., your backend calling a payment gateway, or one microservice calling another). If a dependent service starts failing (e.g., slow responses, timeouts, errors), your service might:

1.  **Exhaust Resources:** Keep sending requests, leading to blocked threads/goroutines, consuming memory, and eventually crashing or becoming unresponsive itself.
2.  **Cause Cascading Failures:** A failure in one service can rapidly spread throughout the entire system, bringing down seemingly unrelated parts.
3.  **Hinder Recovery:** Continuously hammering a struggling service can prevent it from recovering.

## What is the Circuit Breaker Pattern?

The Circuit Breaker pattern is a design pattern used to prevent cascading failures by detecting when a service is unavailable and stopping requests to it for a period, giving it time to recover. It acts like an electrical circuit breaker: if too much "current" (too many failures) flows, it "trips" to prevent further damage.

## How it Works: The Three States

A circuit breaker typically operates in three states:

1.  **Closed (Normal Operation)**
    * This is the default state. Requests to the dependent service are allowed to pass through.
    * The circuit breaker monitors the success/failure rate of these requests.
    * If the number or rate of failures exceeds a predefined **threshold** (e.g., 5 failures within 10 seconds, or 50% error rate), the circuit breaker "trips" and moves to the **Open** state.

2.  **Open (Tripped State)**
    * Once in the Open state, all immediate requests to the dependent service are **blocked** by the circuit breaker. They are not even attempted.
    * The circuit breaker immediately returns an error (e.g., a `CircuitBreakerOpenException` or `Service Unavailable` status) to the caller. This provides a **fail-fast** mechanism.
    * It stays in this state for a configured **timeout period** (e.g., 30 seconds, 1 minute). This timeout gives the dependent service a chance to recover.
    * After the timeout, it automatically transitions to the **Half-Open** state.

3.  **Half-Open (Probing for Recovery)**
    * In this state, the circuit breaker allows a **limited number of requests** (often just one) to pass through to the dependent service. This acts as a "test probe."
    * **If the test request succeeds:** It indicates the dependent service might have recovered. The circuit breaker transitions back to the **Closed** state (normal operation).
    * **If the test request fails:** It means the dependent service is still struggling. The circuit breaker immediately transitions back to the **Open** state, resetting its timeout.

## Analogy

Think of an **electrical circuit breaker** in your house. If an appliance short-circuits, the breaker trips (opens), cutting power and preventing damage. After some time, you can try to flip it back on (half-open) to see if the problem is resolved. If it trips again, you know the issue persists.

## Benefits

* **Resilience:** Prevents cascading failures and protects your service from being overwhelmed by a faulty dependency.
* **Fail-Fast:** Immediately rejects requests to a known-failing service, improving user experience by avoiding long timeouts and reducing resource consumption.
* **Graceful Degradation:** Allows your application to operate in a degraded but functional state (e.g., showing a "Service temporarily unavailable" message) instead of crashing entirely.
* **Facilitates Recovery:** Gives the failing dependent service a period of relief to recover without being constantly bombarded with requests.

## Circuit Breakers vs. Retries

* **Retries** are good for **transient (short-lived) failures** where a quick re-attempt might succeed (e.g., network glitch).
* **Circuit Breakers** are for **persistent failures** where repeated retries would be counterproductive and harmful. They work together: you might retry a few times *within* a "Closed" circuit, but if errors persist, the circuit breaker will trip to prevent further attempts.

## Conceptual Flow (Pseudo-code Example)

```
function callExternalService(data):
    if circuitBreaker.isOpen():
        throw new CircuitBreakerOpenException("Service is currently unavailable.")

    try:
        response = makeActualHttpRequest(externalServiceEndpoint, data)
        circuitBreaker.recordSuccess()
        return response
    except Exception as e:
        circuitBreaker.recordFailure(e)
        throw e

class CircuitBreaker:
    state = CLOSED
    failureCount = 0
    successCount = 0
    lastTripTime = 0

    function recordSuccess():
        if state == HALF_OPEN:
            successCount++
            if successCount >= RECOVERY_THRESHOLD: // e.g., 2 successful probes
                state = CLOSED
                resetCounters()
        else if state == CLOSED:
            resetCounters() // Clear counters on success in closed state

    function recordFailure(error):
        if state == OPEN:
            // Do nothing, already open, waiting for timeout
            return

        failureCount++
        if failureCount >= FAILURE_THRESHOLD: // e.g., 5 failures
            state = OPEN
            lastTripTime = currentTime()
            log("Circuit breaker tripped to OPEN!")
        else if state == HALF_OPEN:
            // Failed during probe, go back to OPEN immediately
            state = OPEN
            lastTripTime = currentTime()
            log("Circuit breaker returned to OPEN after half-open probe failed!")

    function isOpen():
        if state == OPEN:
            if currentTime() - lastTripTime > OPEN_TIMEOUT:
                state = HALF_OPEN // Move to half-open after timeout
                return false // Allow one request
            return true // Still in open state, block request
        return false // Not open, allow request (closed or half-open)

    function resetCounters():
        failureCount = 0
        successCount = 0
```
