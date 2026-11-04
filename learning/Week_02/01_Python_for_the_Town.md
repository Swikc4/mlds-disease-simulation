# Week 2 Python for the Town

Week 1 taught variables, lists, loops, and functions. Week 2 needs a few new ideas. Try each example in a notebook before starting the assignment. Every line has a comment saying what it does.

## 1. Dictionaries describe one thing with named parts

A list holds many values. A **dictionary** holds one thing with named parts:

```python
# one person, with four named parts
person = {"id": 0, "state": "S", "days_exposed": 0, "days_infectious": 0}

print(person["state"])    # read one part: prints "S"
person["state"] = "E"     # change one part: now the person is exposed
person["days_exposed"] += 1   # add 1 to their exposed-day counter
```

In our town, every person is a dictionary like this, and the town is a list of 100 of them.

```python
town[0]             # the first person's whole dictionary
town[0]["state"]    # just that person's state
```

## 2. Functions package a job you reuse

You met functions in Week 1, and this week you will write a small helper function that several roles reuse, so it is worth practicing the shape on a made-up example:

```python
def average_score(scores):            # def starts a function; scores is its input
    total = 0                         # start a running total at 0
    for score in scores:              # visit each value once
        total += score                # add it to the total
    return total / len(scores)        # send the finished result back

result = average_score([8, 9, 7])   # call the function and keep what it returns
```

`def` names the function, the indented lines are its body, and `return` hands back the result. A helper that counts things works the same way: start the counters, loop once, add to the right counter, then return.

## 3. The random module makes each run different

```python
import random            # load Python's random tools

random.seed(42)          # start the random generator the same way every time
print(random.random())   # one number between 0 and 1, for example 0.639...
```

- `random.random() < 0.15` is how we decide whether infection passes in one meeting: random numbers land below 0.15 about 15 times out of 100.
- `random.choice(town)` picks one random person from the list. That is one meeting.
- `random.seed(42)` makes the random numbers come out in the same order every run. Same seed, same result, so teammates can check each other's work.

## 4. Tuples record pairs

A **tuple** is a small fixed group written with parentheses:

```python
meeting = (3, 47)    # person 3 met person 47
print(meeting[0])    # the first id: 3
```

We save each day's meetings as a list of tuples, so the drawing code can connect the two people who met.

## 5. List comprehensions build a list in one line

```python
# for every person in town, take their state, and collect all 100 into a new list
states = [person["state"] for person in town]
```

We use this to save a snapshot of the whole town each day, which the animation replays later.

## 6. Appending builds a list day by day

```python
temperatures = []       # start empty
temperatures.append(18) # add the first day
# inside a loop:
temperatures.append(21) # add each new day at the end
```

`append()` adds one item to the end of a list. This is how the assignment's count lists and snapshots will grow, one day at a time.

## 7. Comparing text with if and elif

```python
if person["state"] == "I":       # == compares; one = would assign instead
    print("infectious")
elif person["state"] == "E":     # otherwise, check the next case
    print("exposed")
else:                            # anything left over
    print("not spreading")
```

Text comparisons need quotes on both sides.

## 8. Checking your work with len() and loops (for Teammate 5)

Testing code uses the same tools you already know, applied to a question about the data. On a made-up example:

```python
steps = [4000, 5200, 6100, 4800, 7000, 5600, 6300]   # one week of daily steps

len(steps) == 7        # True when the list holds the whole week
steps[3] >= 0          # True when one value is not negative

# loop version: check every day, not just one
for day in range(7):
    if steps[day] < 0:
        print("negative value on day", day)

# the reporting pattern: print PASS only when the check succeeds
if len(steps) == 7:
    print("7 daily records: PASS")
else:
    print("7 daily records: FAIL")
```

Week 2's checks follow this same pattern, but with the town's lists and the rules in the assignment.
