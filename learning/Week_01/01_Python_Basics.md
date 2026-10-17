# Week 1 — Python Basics

**Who this is for:** Anyone who has never used Python, or wants a refresher. These are general examples and **not the project solution**.

## 1. What is Python?
Python is a programming language: we give the computer instructions, and it follows them. We will use it to work with numbers, make simple models, and draw charts.

You can run Python code in a **Jupyter notebook**. A notebook has *code cells* (that you can run) and *Markdown cells* (for explanations). Run a code cell with **Shift + Enter**. Work from top to bottom; a variable must be created before you use it.

## 2. Print a result
```python
print("Hello, team!")
print(2 + 3)
```
`print()` displays something. Text goes inside quotes. Numbers do not need quotes.

## 3. Variables store values
```python
apples = 8
oranges = 4
total_fruit = apples + oranges
print(total_fruit)
```
The `=` sign assigns a value. It doesn't mean "the same as" in a math proof. Names like `total_fruit` help other people understand your code.

## 4. Numbers and arithmetic
```python
print(10 + 2)   # add
print(10 - 2)   # subtract
print(10 * 2)   # multiply
print(10 / 2)   # divide
print(2 ** 3)   # power: 2 cubed
```
Anything after `#` is a comment. Python ignores comments, but they explain the code to readers.

## 5. Update a variable
```python
score = 10
score = score + 3
print(score)  # 13
```
Python reads the value on the right and stores the new value on the left. `score += 3` is a shorter way of writing the second line.

## 6. Lists hold several values
```python
daily_sales = [5, 7, 4, 9]
print(daily_sales[0])  # first item: 5
print(len(daily_sales))  # number of items: 4
```
Python starts counting list positions at **0**, not 1.

## 7. Repeating steps with loops
```python
for day in range(3):
    print("Day number:", day)
```
A `for` loop repeats the indented line. `range(3)` gives 0, 1, 2. Indentation matters in Python.

## 8. Decisions with if
```python
temperature = 22
if temperature > 20:
    print("Warm")
else:
    print("Cool")
```
`>` means greater than. `==` checks whether two things are equal. A single `=` assigns a value.

## 9. Functions package a calculation
```python
def double_number(number):
    return number * 2

print(double_number(6))
```
`def` creates the function; `return` gives back its result. The example does not depend on our disease model.

## 10. A tiny graph
If a notebook has Matplotlib installed, try:
```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4]
pages_read = [2, 4, 3, 6]

plt.plot(days, pages_read, marker="o")
plt.xlabel("Day")
plt.ylabel("Pages read")
plt.title("Reading progress")
plt.show()
```
The horizontal (**x**) axis shows days. The vertical (**y**) axis shows pages read. `import` makes another library's tools available.

## 11. When something goes wrong
- `NameError`: check spelling; did you run the cell that creates the variable?
- `SyntaxError`: check parentheses, quotes, and colons.
- `IndentationError`: check spaces inside `for`, `if`, or `def`.
- `ModuleNotFoundError`: a library may need installing in your Python environment.

**Check yourself:** Can you explain each line in the apple, loop, and graph examples to a teammate without looking at these notes?
