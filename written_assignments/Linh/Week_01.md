# Linh

## Week 1 Assignment

I check both set of validation tests for two epidemic simulations: the SIR model (Susceptible, Infected, Recovered) and the SEIR model (which adds an Exposed group). Each simulation ran for 31 days (day 0 to day 30) and stored its results in lists, such as `sir_S`,`sir_I`, `sir_R`, and `seir_E`.
I check that the output follows rules any correct simulation should follow. Each test prints PASS or FAIL, so I can see at a glance whether something went wrong.

**What I tested and how I did it**
1. Correct number of records (31 daily entries) : 
I checked that `len(sir_days)` and `len(seir_days)` both equal 31. This confirms the simulation ran for the full 30 days plus the starting day, with no missing or extra days.

2. Population total stays at 100 : 
For each of the 31 days, I added up all the compartments and checked that the total was 100. I used `round()` to avoid false failures from tiny floating-point errors. This confirms that people move between groups but are never created or lost, which is a key property of these models.

3. No negative values : 
For each day, I checked that none of the compartments dropped below zero. A negative number of people is impossible, so this catches errors such as a transition rate that is too large and removes more people than a group contains. I used TRUE FALSE boolean variable. It is set to `True` if any compartment on that day is below zero, and `False` otherwise.

**The result of my test**
All tests passed. This means both simulations produced the right number of days, conserved the population of 100 on every day, and never produced a negative population in any compartment. That gives reasonable confidence that the model logic is sound.
