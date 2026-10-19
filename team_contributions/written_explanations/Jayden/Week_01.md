# Jayden

## Week 1 Assignment
The first step in building the SIR simulation was to create four empty lists: `sir_days` to track the number of days, `sir_S` to track the number of susceptible individuals, `sir_I` to track the number of infected individuals, and `sir_R` to track the number of recovered individuals. The next step was to set the initial values of `S`, `I`, `R`, `N`, `beta`, and `gamma` to be used in later calculations. After that, I could now append the starting values of the four previously created lists. 

Now that the setup was complete, I started to create the loop to perform the daily calculations from Day 0 to Day 30. The `for` loop used ‘day’ as the iteration variable through the `range(1,31)`. Within the loop, I established the formulas for the daily `new_infections` and `new_recoveries`. Then, those variables were used to update the values for the previous `S`, `I`, and `R` variables. I included an `if` statement to ensure that `S` + `I` + `R` = 100, accounting for minor decimal differences. The last step of the loop was to append each day's value as a new index in the initial four created lists accordingly. The last step was to print the 31 total values for each of the initial lists.

The susceptible group decreased over time, the infectious group increased over time, and the recovered group also increased over time. Towards the end of the 30 days, the general relationship between the groups was: susceptible individuals < infectious individuals < recovered individuals. 
