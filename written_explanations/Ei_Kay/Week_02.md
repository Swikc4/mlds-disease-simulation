# Ei Kay

## Week 2 Assignment

### what do the dot colors and the gray lines each show? 
Each dot is one person in the town of 100. The color shows that person's state on that day: blue is susceptible, orange is exposed, red is infectious, and green is recovered. The gray lines show that day's meetings, where each line connects an infectious person to someone they met. Where a dot sits on the grid means nothing. Only the colors and the lines carry information.

### When does the infectious group peak, and why is this curve jagged when the Week 1 curves were smooth? 
The infectious group grows slowly for the first two weeks, then quickly from about Day 15 to Day 30. It peaks at 43 people on Day 31. After that it shrinks as people recover and few susceptible people are left. By Day 57 nobody is infectious, and on Day 60 the town has 98 recovered and 2 who never got sick.

### Does your town graph tell the same overall story as the Week 1 SEIR graph?
Partly. Both graphs start the same way: one infectious person, a slow start, and then infections speed up while susceptible falls and recovered rises. But the Week 1 SEIR graph only ran for 30 days and never reached its peak. By Day 30 about 76 people were still susceptible and fewer than 10 were infectious. The town graph runs for 60 days and shows the full story: a rise, a peak of 43 infectious on Day 31, and a decline to almost everyone recovered by Day 60.

The town also spreads much faster than the Week 1 SEIR model, because this week's inputs are different. Each infectious person has 3 meetings a day at a 0.15 chance, for 10 days, so one sick person infects about 4.5 others on average early on. The town's shape actually looks closer to the Week 1 SIR graph, where infectious peaked at about 31 people near Day 28. That shows why we extended the run to 60 days: 30 days was not enough to see the peak and decline. The two models don't contradict each other. They tell the same kind of story at a different speed.