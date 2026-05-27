# ⚠️ Exception Handling in Python

## 📌 Description

This Python program demonstrates **exception handling** using a `try-except` block.
It performs division of two numbers entered by the user and handles runtime errors gracefully.

---

## 🚀 Features

* Accepts user input
* Performs division operation
* Handles invalid input and division errors
* Prevents program crash using exception handling

---

## 🛠️ How It Works

### 1️⃣ Program Starts

```python id="m8q3pl"
print("Program starts...")
```

---

### 2️⃣ User Input

```python id="x2m7qa"
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
```

Accepts two integer values.

---

### 3️⃣ Division Operation

```python id="v5q1zx"
c = a / b
```

Performs division.

---

### 4️⃣ Exception Handling

```python id="n4m8pt"
except Exception:
```

Handles runtime errors such as:

* Division by zero
* Invalid numeric input

---

## 💻 Code

```python id="k7m2pl"
print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a / b

    print("The division of", a, "and", b, "is", c)

except Exception:
    print("Error in data")

print("Program ends...")
```

---

## ▶️ Example Output (Valid Input)

```id="p3m9qa"
Program starts...
Enter first number : 20
Enter second number : 5
The division of 20 and 5 is 4.0
Program ends...
```

---

## ▶️ Example Output (Division by Zero)

```id="u6m1zx"
Program starts...
Enter first number : 20
Enter second number : 0
Error in data
Program ends...
```

---

## ▶️ Example Output (Invalid Input)

```id="y8q4mv"
Program starts...
Enter first number : abc
Error in data
Program ends...
```

---

## 🧠 Key Concepts

### ✔ `try` Block

Contains code that may generate an error.

```python id="j5m2pt"
try:
```

---

### ✔ `except` Block

Executes when an exception occurs.

```python id="c9q7pl"
except Exception:
```

---

### ✔ Exception Handling

Prevents abnormal program termination.

---

## 📚 Concepts Used

* Exception handling
* User input
* Arithmetic operations
* `try-except` block

---

## ⚠️ Limitation of Current Code

This code catches all exceptions using:

```python id="f4m8qa"
Exception
```

👉 Not recommended for large projects because it hides specific errors.

---

## ✅ Better Version (Recommended)

```python id="d1q6zx"
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
```

This gives more meaningful error messages.

---

## 🎯 Advantages of Exception Handling

* Prevents crashes
* Improves user experience
* Makes programs robust
* Handles unexpected situations safely

---

## 🔧 Future Improvements

* Add multiple exception blocks
* Use `finally` block
* Add custom exception messages
* Create calculator with full error handling

---

## 📄 License

This project is open-source and free to use.

<img width="576" height="767" alt="image" src="https://github.com/user-attachments/assets/6a5e4a52-c64e-40e1-9afd-d43ba38fd3a0" />
