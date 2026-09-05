# Python Control Flow & Functions — Study Notes

Continuing from Core Syntax & Data Types. Same approach — focused on what's genuinely different from C++, since the underlying logic (if/else, loops, functions) is something you already understand deeply from DSA.

---

## 1. if / elif / else

No parentheses required around the condition, and no curly braces — Python uses **indentation** to define blocks. This is not optional style, it's actual syntax.

```python
x = 10

if x > 15:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

⚠️ **Indentation is mandatory and must be consistent.** Mixing tabs and spaces, or inconsistent indent levels, causes an `IndentationError`. Most editors handle this for you, but be aware it's a real syntax rule, not just formatting.

**Chained comparisons (Python-only convenience):**
```python
if 5 < x < 10:      # equivalent to: 5 < x and x < 10
    print("in range")
```

**Ternary (conditional) expression:**
```python
status = "adult" if age >= 18 else "minor"
```

---

## 2. for loops

Python's `for` loop is fundamentally different from C++'s — it's a **for-each loop**, not an index-based counter loop. There's no `for(int i=0; i<n; i++)` equivalent by default.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**When you need an index (like a C++ for loop):**
```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # start=2, stop=10, step=2 -> 2,4,6,8
    print(i)
```

**When you need both index AND value:**
```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

**Looping over a dictionary:**
```python
d = {"a": 1, "b": 2}
for key in d:                 # loops over keys by default
    print(key)
for key, value in d.items():  # loops over key-value pairs
    print(key, value)
```

**Looping over multiple sequences together — `zip`:**
```python
names = ["Niraj", "Amit"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
```

---

## 3. while loops

Behaves like C++, with the same indentation rule.

```python
n = 5
while n > 0:
    print(n)
    n -= 1     # no n-- in Python! must use n -= 1
```

⚠️ **Python has no `++` or `--` operators.** You must write `n += 1` / `n -= 1`.

---

## 4. break, continue, else (loop-else — Python-only feature)

`break` and `continue` work exactly like C++.

**The `else` clause on a loop is unique to Python** — it runs only if the loop completed *without* hitting a `break`. Useful for search patterns.

```python
def find_target(nums, target):
    for n in nums:
        if n == target:
            print("Found it")
            break
    else:
        print("Not found")   # runs only if break never happened
```

---

## 5. Defining Functions

```python
def add(a, b):
    return a + b

result = add(3, 5)   # 8
```

No return type or parameter types need to be declared (though you *can* add optional type hints — see below).

**Default arguments:**
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Niraj")                # "Hello, Niraj!"
greet("Niraj", "Hi")           # "Hi, Niraj!"
```

⚠️ **Common trap:** never use a mutable default argument like a list or dict.
```python
def add_item(item, my_list=[]):   # BAD — the same list is reused across calls!
    my_list.append(item)
    return my_list
```
Instead:
```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

**Returning multiple values (actually returns a tuple):**
```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])   # lo=1, hi=5
```

---

## 6. *args and **kwargs

Lets a function accept a variable number of arguments — very common in real-world code and interview questions.

**`*args`** — collects extra positional arguments into a tuple:
```python
def total(*args):
    return sum(args)

total(1, 2, 3)        # 6
total(1, 2, 3, 4, 5)  # 15
```

**`**kwargs`** — collects extra keyword arguments into a dictionary:
```python
def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe(name="Niraj", age=20)
# name: Niraj
# age: 20
```

**Combining both:**
```python
def example(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

example(1, 2, 3, 4, x=5, y=6)
# 1 2 (3, 4) {'x': 5, 'y': 6}
```

---

## 7. Lambda functions (anonymous functions)

A quick, throwaway function written in one line — mainly used when you need a small function briefly (e.g., as an argument to another function).

```python
square = lambda x: x**2
square(5)   # 25

# Very common use: as a "key" for sorting
words = ["banana", "kiwi", "apple"]
words.sort(key=lambda w: len(w))   # sort by length instead of alphabetically
```

Equivalent full function, for comparison:
```python
def square(x):
    return x**2
```

---

## 8. Useful built-in functions for functional-style code

These come up constantly in real code and in interviews:

```python
map(func, iterable)      # applies func to every element
list(map(lambda x: x*2, [1,2,3]))   # [2, 4, 6]

filter(func, iterable)   # keeps elements where func returns True
list(filter(lambda x: x % 2 == 0, [1,2,3,4]))   # [2, 4]

sorted(iterable, key=..., reverse=...)
sorted([3,1,2])                     # [1, 2, 3]
sorted(["bb","a","ccc"], key=len)   # ['a', 'bb', 'ccc']

sum(iterable)
max(iterable) / min(iterable)
any(iterable)   # True if at least one element is truthy
all(iterable)   # True if all elements are truthy
```

---

## 9. (Optional but good practice) Type Hints

Not enforced by Python at runtime, but increasingly expected in professional codebases and makes your code more readable/interview-ready.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

---

## Quick Self-Test

1. Why doesn't Python have curly braces for if/for/while blocks, and what replaces them?
2. What's wrong with `for(int i=0; i<n; i++)` style thinking in Python — what should you use instead when you need an index?
3. What does `n--` do in Python? (Trick question.)
4. What does a loop's `else` clause actually mean?
5. Why is `def f(x, my_list=[])` dangerous?
6. What does `*args` collect, and what does `**kwargs` collect?
7. Write a one-line lambda that returns whether a number is even.

If you can answer all 7 confidently, you're ready for practice problems on this section.
