# Our Findings

## Week 1: SIR and SEIR

Final notebook: [Week 1 Assignment](https://github.com/Swikc4/mlds-disease-simulation/blob/main/assignments/Week_01_Assignment.ipynb)

SIR chart:

![SIR Simulation](<SIR Graph-1.png>)

SEIR chart:

![SEIR Simulation](<SEIR Graph-2.png>)

### Findings

Our 30-day simulation showed that infections spread faster in the SIR model than in the SEIR model. By Day 30, approximately 31 people were infectious in SIR compared to 8 in SEIR. This difference occurs because SEIR includes an exposed stage, which delays the transition from infection to becoming infectious.

### Limitations

We used assumed parameter values and a closed population of 100 people. These simulations demonstrate how the models behave under simplified conditions and do not represent actual disease outbreaks.