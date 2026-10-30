# Linh

## Week 2 Assignment

I started with an empty list called town and used a for loop to run 100 times (ids 0 to 99). Each pass created a new dictionary for one person and appended it to the list. After the loop, I set person 0’s state to "I" so there’s one infectious person on Day 0.

Each person’s dictionary stores four things:

id: the person’s number (0 to 99) 

state: their current status, one of "S" (susceptible), "E" (exposed), "I" (infectious), or "R" (recovered)

days_exposed: how many days they’ve been in the exposed group

days_infectious: how many days they’ve been infectious
