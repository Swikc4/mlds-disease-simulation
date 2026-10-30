# Ei Kay

## Week 1 Assignment

I built the SEIR simulation using Python to see how a disease spreads over 30 days. I started with 100 people: 99 susceptible (S), 0 exposed (E), 1 infectious (I), and 0 recovered (R). I used three parameters: beta = 0.30, sigma = 0.20, and gamma = 0.10, which control the infection, progression, and recovery rates.

I created five lists to store the results and used a `for` loop to calculate the changes each day. First, I calculated new exposures (`beta * S * I / N`), new infectious cases (`sigma * E`), and new recoveries (`gamma * I`). Then I updated the four groups and saved the results using `append()`. I also checked that the total population remained 100 every day.

Over the 30 days, the susceptible group gradually decreased as more people were exposed. The exposed and infectious groups increased as the disease spread, while the recovered group continued to grow. The infectious group initially decreased slightly before increasing as more exposed people became infectious.

This simulation helped me understand how mathematical formulas and Python loops can model disease transmission over time. I also learned how the four groups are connected and how changes in one group affect the others.
