# Week 1: Introduction to SIR and SEIR

We are starting from scratch. During Week 1, we will learn two disease models, practice Python, and build simple simulations together. Our six member team will choose responsibilities at our meeting. The example values are teaching assumptions, not medical estimates.

## What are SIR and SEIR?

SIR divides 100 people into Susceptible (S), Infected (I), and Recovered (R).

Starting values:

$
\begin{aligned}
S &= 99 \\
I &= 1 \\
R &= 0
\end{aligned}
$

People move from S to I to R.

SEIR adds Exposed (E), a group infected but not yet infectious in our simplified model. People move from S to E to I to R.

SEIR starts at:

$
\begin{aligned}
S &= 99 \\
E &= 0 \\
I &= 1 \\
R &= 0
\end{aligned}
$

In SIR:

$
S + I + R = 100
$

In SEIR:

$
S + E + I + R = 100
$

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

$
\begin{aligned}
\beta &= 0.30 \\
\gamma &= 0.10
\end{aligned}
$

These are assumptions, not values for a particular disease.

New infections:

$
\text{New infections} = \frac{\beta \times S \times I}{\text{population}}
$

New recoveries:

$
\text{New recoveries} = \gamma \times I
$

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

SEIR adds sigma, which controls how quickly exposed people move to the infectious group. For practice:

$
\sigma = 0.25\text{ per day}
$

Daily changes:

From S to E:

$
\text{New exposures} = \frac{\beta \times S \times I}{\text{population}}
$

From E to I:

$
\text{New infectious cases} = \sigma \times E
$

From I to R:

$
\text{New recoveries} = \gamma \times I
$

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

Hint: SIR has no exposed stage, while SEIR includes a delay before a person becomes infectious. Do not confuse the time until symptoms with the time until infectiousness.

**YOUR EXPLANATION GOES HERE.**

## Teammate 2: SIR model

Start with 100 people, S=99, I=1, R=0. Repeat the one day formulas for 30 days and save daily values in lists.

Hints: `for day in range(1, 31):` repeats code. Use `.append(value)` to save daily values. Save day 0 first. Calculate infections and recoveries before updating the groups.

```python
# YOUR CODE GOES HERE: SIR simulation
# Use a for loop for 30 days
# Save day, S, I, and R values
```

## Teammate 3: SEIR model

Start with S=99, E=0, I=1, R=0. Use beta=0.30, sigma=0.25, gamma=0.10 for 30 days. Save all four groups.

Hint: compute new exposures, new infectious cases, and new recoveries from the previous day's values first. Then update S, E, I, R.

```python
# YOUR CODE GOES HERE: SEIR simulation
# Use four groups and save daily values
```

## Teammate 4: Graphs

Ask Teammates 2 and 3 for their results. Make two charts, one for SIR and one for SEIR. Label both axes, include a title and a legend.

Hint: use `import matplotlib.pyplot as plt`, `plt.plot(days, infected_values, label='Infected')`, `plt.legend()` and `plt.show()`.

```python
# YOUR CODE GOES HERE: SIR and SEIR charts
```

## Teammate 5: Testing

Check each day: totals stay at 100, no group is negative, S does not increase, and R does not decrease. Write down any failed day.

Hint: `abs(total - 100) < 0.000001` allows small decimal rounding differences.

```python
# YOUR CODE GOES HERE: checks for SIR and SEIR
```

## Explain your work

After finishing your assigned part, I want each of you to explain what you actually did and how it works. This helps us understand the project instead of just collecting code.

Write about **150 to 250 words**, using your own words. Keep it simple. Answer the four questions for everyone, then the questions for your role below.

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
3. How does the Exposed group change over time?

### Teammate 4: Charts

1. What does each line on your SIR and SEIR charts mean?
2. What do the horizontal and vertical axes show?
3. What differences do you notice between the two charts?

### Teammate 5: Testing

1. How did you check that the population stays at 100?
2. How did you check for negative values or calculation errors?
3. Why do we need to test the results before using the graphs?

### Where to submit your explanation

Save your writing as **`YourName_Week01_Explanation.md`** under **`our_work/explanations/`** on your branch. Include it in the same pull request as your assigned work.

The project lead will review the explanations and combine approved coding work into **`our_work/assignments/Week_01_Final.ipynb`**.

**Required Week 1 reading:** [CDC Yellow Book: Influenza](https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/influenza.html). Read the parts describing the **incubation period** and **when people can spread influenza**. You do not need to read the entire page. Use those details to think about why the SIR model is simplified and why SEIR adds an Exposed stage. **Question:** Is the time before symptoms always the same as the time before someone becomes infectious? Explain briefly in your own words.

For the SIR and SEIR formulas, use Sections 1 through 5 of **this notebook**. The CDC page is background on real disease timing, not a source for our formulas or chosen parameter values. Our **beta = 0.30, gamma = 0.10, and sigma = 0.25** are classroom assumptions, not influenza estimates. The other research links are saved in `research/README.md` for later weeks.

## GitHub submission

Complete your role on your own branch and open a pull request. Do not edit the assignment on main. You can submit a temporary file while the work is reviewed.

After reviewing everyone's contributions, I'll combine the approved explanations, SIR code, SEIR code, charts, and tests into **one `our_work/assignments/Week_01_Final.ipynb`**. We will keep this as the weekly final notebook. The pull request history will still show who contributed.

Checklist: I completed my part, can explain it, shared any needed output, checked my work, and opened a pull request.
