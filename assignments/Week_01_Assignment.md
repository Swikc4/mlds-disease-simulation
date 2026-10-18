# Week 1: Introduction to SIR and SEIR

During Week 1, we will learn two disease models, practice Python, and build simple simulations together. Our six member team will choose responsibilities at our meeting. The example values are teaching assumptions, not medical estimates.

## Brief History of SIR and SEIR

In 1927, scientists **William O. Kermack and A. G. McKendrick** published an important mathematical model of how epidemics spread. Their work helped establish the foundation for the **SIR model**, which groups people as Susceptible, Infected, or Recovered.

The **SEIR model** extends this basic idea by adding an **Exposed** group for people who have been infected but are not yet infectious. These models help us understand how infections move through a population. Our Week 1 simulation is a simplified learning example, not a prediction of a real outbreak.


## What are SIR and SEIR?

SIR divides 100 people into Susceptible (S), Infected (I), and Recovered (R). Starting values:

```math
\begin{aligned}
S &= 99 \\
I &= 1 \\
R &= 0
\end{aligned}
```

SEIR adds Exposed (E), a group infected but not yet infectious in our simplified model.

SEIR starts at:

```math
\begin{aligned}
S &= 99 \\
E &= 0 \\
I &= 1 \\
R &= 0
\end{aligned}
```

In SIR:

```math
S + I + R = 100
```

In SEIR:

```math
S + E + I + R = 100
```

We assume no births, deaths, or reinfections. The exposed stage does not necessarily equal the real disease incubation period.

## Worked Python example

Variables hold numbers. Run this cell to check the starting population.

```python
population = 100
S = 99
I = 1
R = 0
print('Total:', S + I + R)
print('Matches population:', S + I + R == population)
```

**Expected:** Total: 100 and Matches population: True.

**Practice:** Try 200 people with 5 infected and none recovered. Calculate how many are susceptible. Hint: subtract infected and recovered from the total.

```python
# YOUR CODE GOES HERE
population = 200
I = 5
R = 0
# Calculate S and print the total
```

## How a day changes

In the simple SIR model, beta controls transmission and gamma controls recovery. For practice:

```math
\begin{aligned}
\beta &= 0.30 \\
\gamma &= 0.10
\end{aligned}
```

These are assumptions, not values for a particular disease.

New infections:

```math
\text{New infections} = \frac{\beta S I}{\text{population}}
```

New recoveries:

```math
\text{New recoveries} = \gamma I
```

Calculate both from the old values before updating S, I and R. S loses new infections, I gains new infections and loses recoveries, and R gains recoveries. Decimal results are expected quantities in this mathematical model, not fractions of real people.

```python
# WORKED EXAMPLE: one day
S, I, R = 99.0, 1.0, 0.0
beta, gamma = 0.30, 0.10
new_infections = beta * S * I / 100
new_recoveries = gamma * I
S = S - new_infections
I = I + new_infections - new_recoveries
R = R + new_recoveries
print(round(S,3), round(I,3), round(R,3))
```

## What changes for SEIR?

SEIR adds sigma, which controls how quickly exposed people move to the infectious group. For practice, we use:

```math
\sigma = 0.25\ \text{per day}
```

Daily changes are:

From S to E:

```math
\text{New exposures} = \frac{\beta S I}{\text{population}}
```

From E to I:

```math
\text{New infectious cases} = \sigma E
```

From I to R:

```math
\text{New recoveries} = \gamma I
```

Hint: updated E equals previous E plus new exposures minus people moving into I. Compute all three changes before updating the four groups.

## Our six responsibilities

We have five teammates plus me. We'll decide who takes each role at the meeting.

| Person | Task | Deliverable |
| :--- | :--- | :--- |
| Teammate 1 | Explain SIR, SEIR, and assumptions | Short Markdown explanation |
| Teammate 2 | Write a 30 day SIR simulation | SIR values saved for every day |
| Teammate 3 | Write a 30 day SEIR simulation | SEIR values saved for every day |
| Teammate 4 | Plot both models | Two labeled line charts |
| Teammate 5 | Test both models | Test notebook and notes |
| Me, Project Lead | Coordinate, review, interpret, and integrate | One approved final notebook and findings |

Teammates 2 and 3 should share their daily values with Teammates 4 and 5.

## Teammate 1: Concept explanation

Explain what S, E, I and R mean, why population stays constant, and two assumptions that make the models simpler than real disease outbreaks.

**Use this source from our [Research Sources](../research/README.md):**

[CDC Yellow Book: Influenza](https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/influenza.html)

Read about the incubation period and when influenza can spread. In your own words, explain one useful fact from the source and how it connects to SIR or SEIR. Remember that the time before symptoms does not always match the time before someone becomes infectious.

Our beta, gamma, and sigma values are practice assumptions, not numbers taken from the CDC page.

**YOUR EXPLANATION GOES HERE.**

## Teammate 2: SIR model

Start with 100 people:

```math
\begin{aligned}
S &= 99 \\
I &= 1 \\
R &= 0
\end{aligned}
```

Repeat the one day formulas for 30 days and save daily values in lists.

### Learning Material: Python For Loops

A **for loop** repeats instructions. You need one because the SIR model must calculate the changes for each day, not just once.

1. Read [Python's official tutorial on for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Focus on the examples using `for` and `range()`.
2. Practice what `range(1, 31)` means. It gives the numbers from 1 through 30.
3. Review how a list stores values and how `.append()` adds another value. See [Python's introduction to lists](https://docs.python.org/3/tutorial/introduction.html#lists).
4. In your simulation, save the starting values for day 0, then use a loop to calculate and store each following day. Work out new infections and recoveries **before** updating S, I and R.

**Practice question:** If a loop runs 30 times and you save day 0 before it starts, how many days of results will you have?

Write your solution directly in the code section below.



```python
# YOUR CODE GOES HERE: SIR simulation
# Use a for loop for 30 days
# Save day, S, I, and R values
```

## Teammate 3: SEIR model

Start with:

```math
\begin{aligned}
S &= 99 \\
E &= 0 \\
I &= 1 \\
R &= 0
\end{aligned}
```

Use these practice parameters:

```math
\begin{aligned}
\beta &= 0.30 \\
\sigma &= 0.25 \\
\gamma &= 0.10
\end{aligned}
```

Run the model for 30 days and save all four groups.

### Learning Material: Using a Loop for SEIR

You will also use a **for loop** to repeat your daily calculations for 30 days. The main difference from SIR is that you must update **four** groups, including Exposed (E).

1. Review [Python's official tutorial on for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements), especially `range()`.
2. Review [Python lists](https://docs.python.org/3/tutorial/introduction.html#lists) and the `.append()` method for keeping results from each day.
3. Save day 0 first. For every new day, calculate new exposures, new infectious cases, and new recoveries using the previous day's numbers.
4. Update S, E, I, and R only **after** calculating those three changes. Save the four updated values for that day.

**Practice question:** How many separate lists do you need to save the day, S, E, I and R values?

Write your solution directly in the code section below.



```python
# YOUR CODE GOES HERE: SEIR simulation
# Use four groups and save daily values
```

## Teammate 4: Graphs

Create two line graphs in Python using `matplotlib`. You do not need to build the disease simulations.

### Graphs to Create

**SIR graph:** Show three lines for Susceptible (S), Infected (I), and Recovered (R).

**SEIR graph:** Show four lines for Susceptible (S), Exposed (E), Infected (I), and Recovered (R).

Use your teammates' actual daily simulation results. The shape of the lines may vary.

### Instructions

1. Get the daily SIR results from **Teammate 2** and the daily SEIR results from **Teammate 3**.
2. Create one SIR graph with three lines and one SEIR graph with four lines.
3. For both graphs, label the horizontal axis **Days (0 to 30)** and the vertical axis **Number of people (0 to 100)**.
4. Add a clear title, a legend, and different colors for each group.
5. Save the finished SIR and SEIR graphs as image files in the `results/` folder.
6. Submit **both graph images and your Python code together** on your own branch in one pull request. Follow the [Submission Guide](../SUBMISSION_GUIDE.md#how-to-submit-graphs-teammate-4) for help.

### How to Make the Graphs in Python

Write your Python code **directly in the code section below this guide**. Do not create a separate notebook or Python file for this assignment.

1. **Get the data.** Ask Teammates 2 and 3 for the daily results for each group.
2. **Import Matplotlib.** Use the `matplotlib.pyplot` library to create your graphs.
3. **Plot the lines.** Use `plt.plot()` to draw one line for each group, with days on the horizontal axis and number of people on the vertical axis.
4. **Label the graphs.** Add a title, axis labels, different colors, and a legend.
5. **Check your work.** Use the actual simulation data, then save both finished graph images in the `results/` folder.

**Beginner resource:** [Matplotlib's introductory plotting guide](https://matplotlib.org/stable/tutorials/pyplot.html)

### Your Code Goes Here

Add your own Python code below. Create both the SIR and SEIR graphs here.

```python
# Write your SIR and SEIR graph code here

```

## Teammate 5: Testing

Ask Teammates 2 and 3 for their saved daily results. You do not need to write the simulations yourself.

Start with two checks for **both models**:

1. The total population stays at 100 each day.
2. No group has a negative value.

For SIR, check:

```math
S + I + R = 100
```

For SEIR, check:

```math
S + E + I + R = 100
```

**Hint:** `abs(total - 100) < 0.000001` allows small decimal rounding differences. If a check fails, write down the day and the problem. If you have time, also check that S does not increase and R does not decrease.

### Learning Material: Testing in Python

Testing means checking whether the simulation results make sense. You do not need to create the SIR or SEIR models yourself.

1. **Learn conditions.** Read [Python's guide to `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements). An `if` statement lets you check whether a condition is true.
2. **Learn loops.** Review [Python's guide to `for` loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements). You can use a loop to check every day instead of checking each day manually.
3. **Check the total.** For each day, add the SIR groups or SEIR groups. The answer should stay close to 100. Because Python uses decimals, a tiny rounding difference is okay.
4. **Check for negative numbers.** Make sure none of the groups is below zero on any day.
5. **Record your results.** If something fails, write down the day, which model it came from, and what went wrong. If all days pass, say so in your explanation.

**Practice:** If S = 70, I = 20, and R = 10, does the SIR total pass? What if one group is negative?

Write your own testing code directly in the section below. Do not create a separate notebook or Python file.

### Your Code Goes Here

```python
# Write your SIR and SEIR testing code here
```

## Explanation and submission

### Written explanation

After finishing your assigned part, explain what you did and how it works. This helps us understand the project instead of just collecting code.

Write **150 to 250 words in total for all your answers combined**, not for each question. Use your own words and keep it simple. Answer the four questions for everyone, then the questions for your role below.

### Questions for everyone

1. What part of Week 1 did I work on?
2. What steps did I take to complete it?
3. How does my part work, and why do we need it for our simulation?
4. What did I learn, check, or find difficult?

### Teammate 1: SIR and SEIR concepts

1. What does each letter in SIR and SEIR mean?
2. Why does SEIR have an Exposed group?
3. What assumptions are we making about our population?

### Teammate 2: SIR simulation

1. What do beta and gamma do in our model?
2. How does your code update the three groups each day?
3. Why did you use a loop and save the daily values?

### Teammate 3: SEIR simulation

1. How is your SEIR code different from the SIR code?
2. What does sigma represent?
3. How did you use a loop to update and save the four groups (S, E, I, R) each day?

### Teammate 4: Charts

1. What does each line on your SIR and SEIR charts mean?
2. What do the horizontal and vertical axes show?
3. What differences do you notice between the two charts?

### Teammate 5: Testing

1. How did you check that the population stays at 100?
2. How did you check for negative values or calculation errors?
3. Why do we need to test the results before using the graphs?
4. If you found an error, what was it and how did you report it? If there were no errors, how did you confirm that the results passed your checks?

### Where to submit

**Written explanation:** Follow the [Submission Guide](../SUBMISSION_GUIDE.md) to save and submit your explanation.

**Code, charts, and testing:** Follow the same [Submission Guide](../SUBMISSION_GUIDE.md) to submit your files and open a pull request.
