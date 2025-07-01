# String Formatting Placeholders

## Numbers
### Integers
| Verb | Meaning           | Example (`x := 42`)    | Output   |
| ---- | ----------------- | ---------------------- | -------- |
| `%d` | Decimal           | `fmt.Printf("%d", x)`  | `42`     |
| `%b` | Binary            | `fmt.Printf("%b", x)`  | `101010` |
| `%o` | Octal             | `fmt.Printf("%o", x)`  | `52`     |
| `%x` | Hex (lowercase)   | `fmt.Printf("%x", x)`  | `2a`     |
| `%X` | Hex (uppercase)   | `fmt.Printf("%X", x)`  | `2A`     |
| `%c` | Unicode character | `fmt.Printf("%c", 65)` | `A`      |

### Floating Points
| Verb | Meaning                         | Example (`f := 3.14159`) | Output         |
| ---- | ------------------------------- | ------------------------ | -------------- |
| `%f` | Decimal (fixed-point)           | `fmt.Printf("%.2f", f)`  | `3.14`         |
| `%e` | Scientific notation (lowercase) | `fmt.Printf("%e", f)`    | `3.141590e+00` |
| `%E` | Scientific notation (uppercase) | `fmt.Printf("%E", f)`    | `3.141590E+00` |
| `%g` | Smart: short %e or %f           | `fmt.Printf("%g", f)`    | `3.14159`      |
| `%G` | Smart: short %E or %f           | `fmt.Printf("%G", f)`    | `3.14159`      |

## Strings and Characters
| Verb | Meaning                | Example                  | Output |
| ---- | ---------------------- | ------------------------ | ------ |
| `%s` | Raw string             | `fmt.Printf("%s", "go")` | `go`   |
| `%q` | Quoted string          | `fmt.Printf("%q", "go")` | `"go"` |
| `%x` | Hex string (lowercase) | `fmt.Printf("%x", "go")` | `676f` |
| `%X` | Hex string (uppercase) | `fmt.Printf("%X", "go")` | `676F` |

## Structs, Interfaces, and Anything Else
| Verb  | Meaning                  | Example                     | Output                            |
| ----- | ------------------------ | --------------------------- | --------------------------------- |
| `%v`  | Default format           | `fmt.Printf("%v", x)`       | Depends on type                   |
| `%+v` | Struct with field names  | `fmt.Printf("%+v", person)` | `Name:Bob Age:30`                 |
| `%#v` | Go syntax representation | `fmt.Printf("%#v", person)` | `main.Person{Name:"Bob", Age:30}` |
| `%T`  | Type of value            | `fmt.Printf("%T", 42)`      | `int`                             |

## Booleans and Pointers
| Verb | Meaning               | Example                  | Output  |
| ---- | --------------------- | ------------------------ | ------- |
| `%t` | Boolean               | `fmt.Printf("%t", true)` | `true`  |
| `%p` | Pointer address (hex) | `fmt.Printf("%p", &x)`   | `0x...` |

## Escape Sequences for Control
| Sequence | Meaning     |
| -------- | ----------- |
| `\n`     | New line    |
| `\t`     | Tab         |
| `%%`     | Literal `%` |
