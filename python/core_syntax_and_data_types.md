# Python Core Syntax & Data Types — Study Notes

For a C++/DSA background — notes focus on what's *different* from what you already know, not on re-teaching concepts you already understand.

---

## 1. Variables & Basic Types

Python is **dynamically typed** — you don't declare a type, and a variable can be reassigned to a different type at any time.

```python
x = 5          # int
x = "hello"    # now x is a str — totally legal, no error
```

**Basic types:**
```python
a = 10          # int
b = 3.14        # float
c = "text"      # str
d = True        # bool (capital T/F, not true/false like C++)
e = None        # like nullptr / null — represents "nothing"
```

**Type conversion:**
```python
int("5")        # 5
str(5)          # "5"
float("3.14")   # 3.14
int(3.9)        # 3 (truncates, doesn't round)
```

**Common gotcha coming from C++:** there's no `int x;` with a garbage/default value — a variable doesn't exist until you assign it something.

---

## 2. Strings

Strings are **immutable** sequences of characters — similar to `const` in C++, every "modification" actually creates a new string.

**Indexing & slicing:**
```python
s = "Hello World"
s[0]        # 'H'
s[-1]       # 'd'  (negative index = from the end)
s[0:5]      # 'Hello'   (slice: start inclusive, end exclusive)
s[::-1]     # 'dlroW olleH'   (step -1 = reverse the string)
s[::2]      # 'HloWrd'   (every 2nd character)
```

**Concatenation & formatting:**
```python
name = "Niraj"
greeting = "Hi, " + name          # concatenation
greeting = f"Hi, {name}!"         # f-string (preferred — like a clean sprintf)
```

**Common methods:**
```python
s = "  Hello World  "
s.strip()          # 'Hello World'  (removes leading/trailing whitespace)
s.lower()          # '  hello world  '
s.upper()          # '  HELLO WORLD  '
s.split()          # ['Hello', 'World']  (splits on whitespace by default)
s.split(",")       # split on a specific delimiter
"-".join(["a","b","c"])   # 'a-b-c'  (opposite of split)
s.replace("World", "Python")
s.find("World")    # returns index, or -1 if not found
```

---

## 3. Lists

The closest equivalent to a `vector` in C++, but dynamically sized by default and can hold mixed types.

```python
nums = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]   # legal — lists can hold any type
```

**Indexing & slicing (same rules as strings):**
```python
nums[0]      # 1
nums[-1]     # 5 (last element)
nums[1:3]    # [2, 3]
nums[::-1]   # [5, 4, 3, 2, 1]  (reversed copy)
```

**Common operations:**
```python
nums.append(6)        # add to end
nums.insert(0, 0)      # insert 0 at index 0
nums.pop()             # remove & return last element
nums.pop(0)            # remove & return element at index 0
nums.remove(3)         # remove the *value* 3 (first occurrence)
nums.sort()            # sort in place, ascending
nums.sort(reverse=True)  # descending
len(nums)              # length
3 in nums              # True/False — check membership
```

**Nested lists (2D arrays / matrices — important for DSA):**
```python
grid = [[0]*3 for _ in range(3)]   # 3x3 matrix of zeros
grid[1][2] = 5                     # access/modify like a normal 2D array
```
⚠️ Common bug: `[[0]*3]*3` looks the same but creates **3 references to the same inner list** — modifying one row modifies all rows. Always use the list comprehension version above for matrices.

**List comprehensions (you already know these):**
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 4. Tuples

Like a list, but **immutable** — once created, it can't be changed. Faster and safer when data shouldn't change.

```python
point = (3, 4)
point[0]        # 3
point[0] = 5    # ERROR — tuples can't be modified
```

**When to use a tuple instead of a list:**
- Returning multiple values from a function
- Using as a dictionary key (lists can't be keys — they're mutable and unhashable)
- Representing fixed structures (like coordinates)

**Tuple unpacking:**
```python
a, b = 1, 2
a, b = b, a          # swap — no temp variable needed, unlike C++
def get_coords():
    return 3, 4       # actually returns a tuple (3, 4)
x, y = get_coords()
```

---

## 5. Dictionaries

Python's built-in **hashmap** — you already understand this data structure conceptually from DSA; this is just the syntax.

```python
d = {"name": "Niraj", "age": 20}
d["name"]              # 'Niraj'
d["city"] = "Haldwani" # add a new key
d.get("age")           # 20
d.get("email", "N/A")  # 'N/A' — safe access with a default if key doesn't exist
```

**Checking existence & iterating:**
```python
"name" in d            # True — checks keys by default
d.keys()                # dict_keys(['name', 'age', 'city'])
d.values()              # dict_values(['Niraj', 20, 'Haldwani'])
d.items()               # dict_items([('name','Niraj'), ('age',20), ...])

for key, value in d.items():
    print(key, value)
```

**Dictionary comprehension:**
```python
squares = {x: x**2 for x in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}
```

**Very common DSA pattern — counting frequency:**
```python
freq = {}
for ch in "hello":
    freq[ch] = freq.get(ch, 0) + 1
# {'h':1, 'e':1, 'l':2, 'o':1}
```

---

## 6. Sets

Python's built-in **hashset** — unordered collection of unique elements.

```python
s = {1, 2, 3, 3, 3}     # {1, 2, 3} — duplicates auto-removed
s.add(4)
s.remove(2)
3 in s                  # True — O(1) lookup, same as your DSA knowledge of hashsets
```

**Set operations (very handy for DSA problems):**
```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # union → {1, 2, 3, 4}
a & b     # intersection → {2, 3}
a - b     # difference → {1}
a ^ b     # symmetric difference → {1, 4}
```

**Set comprehension:**
```python
unique_lengths = {len(word) for word in ["hi", "hey", "yo"]}
```

---

## 7. Slicing — deserves its own section

The single most powerful syntax feature that C++ doesn't really have an equivalent for. Works identically on **strings, lists, and tuples**.

```python
seq[start:stop:step]
```

- `start` — inclusive, defaults to 0
- `stop` — exclusive, defaults to end of sequence
- `step` — defaults to 1; negative step reverses direction

```python
nums = [0,1,2,3,4,5,6,7,8,9]
nums[2:5]      # [2, 3, 4]
nums[:4]       # [0, 1, 2, 3]      (omit start = from beginning)
nums[6:]       # [6, 7, 8, 9]      (omit stop = to the end)
nums[::2]      # [0, 2, 4, 6, 8]   (every other element)
nums[::-1]     # [9, 8, ..., 0]    (full reverse — very common in interviews)
nums[-3:]      # [7, 8, 9]         (last 3 elements)
```

Once this becomes second nature, it replaces a lot of manual index-tracking loops you'd write in C++.

---

## 8. Type Checking & Conversion

```python
type(5)                 # <class 'int'>
isinstance(5, int)       # True — preferred over type() for checks
isinstance(5, (int, float))  # True — check against multiple types at once
```

**Truthy / Falsy values** — trips up almost everyone coming from a strictly-typed language:

Falsy values in Python: `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `set()` (empty set), `None`, `False`.
Everything else is truthy.

```python
if []:          # this is False — empty list is falsy
    print("won't run")

if [1,2,3]:      # this is True — non-empty list is truthy
    print("runs")
```

This means you'll often see Pythonic code like:
```python
if my_list:              # instead of: if len(my_list) > 0:
    ...
```

---

## Quick Self-Test

Before moving to the next topic (Control Flow & Functions), you should be able to answer these without looking anything up:

1. What's the difference between a list and a tuple, and when would you use each?
2. How do you reverse a string in one line?
3. Why does `[[0]*3]*3` create a bug when used as a matrix?
4. How do you count character frequency in a string using a dictionary?
5. What does `nums[2:]` return if `nums` has 10 elements?
6. Is an empty dictionary `{}` truthy or falsy?

If you can answer all 6 confidently, you're solid on this section.
