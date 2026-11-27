# Week 5 learning guide

Open the [Week 5 assignment](../../assignments/Week_05_Visual_ML.ipynb) and run the shared setup. It loads the eight weeks of data you need. Use the section below that matches your part.

## Parts 1 to 3 • Compare two lines

A weekly share tells you how much of the eight week total happened in one week. If a simulation has 40 infections over eight weeks and 10 happen in week 2, that week has a 25% share. Calculate shares separately for the simulation and the real records. This lets you compare when each series rises and falls even when the totals are very different.

Try this small example in a practice cell.

```python
import pandas as pd
import matplotlib.pyplot as plt

practice = pd.DataFrame({
    "week": [1, 2, 3],
    "model_share": [20, 50, 30],
    "real_share": [15, 40, 45]
})

practice.plot(x="week", y=["model_share", "real_share"], marker="o")
plt.ylabel("Share of total (%)")
plt.show()
```

* Alex, find the highest point on each line. In the example, `practice["model_share"].idxmax()` gives the row label. Read the week from that row with `practice.loc[row_label, "week"]`. You should get week 2 for the model. Use `plt.axvline()` to mark a peak before showing the plot.
* Linh, use `.corr()` between the two share columns to check how they move together. A value near 1 means high weeks tend to line up. A value near −1 means high weeks in one series tend to line up with low weeks in the other. Mark each peak with `plt.scatter(week, share)`.
* Aayush, add the weekly shares for the period you want. In the practice table, the first two weeks account for 70% of the model total and 55% of the real total. Apply that idea to the first four weeks in your assignment.

[Practice making charts with pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)

## Parts 4 and 5 • Train and test a model

Both models use the disease name, week and simulation index as inputs. An index of 100 means the count equals its week 1 value. An index of 150 means it is 50% higher. The setup gives each disease its own starting point. The notebook uses `pd.get_dummies()` to turn disease names into columns of zeros and ones.

Read the two Python methods in this order. `model.fit(X_train, y_train)` learns from earlier weeks. `model.predict(X_test)` uses what it learned to predict weeks 7 and 8. Keep the answers for those last two weeks aside until you score the predictions.

### Ei Kay • Predict the real index with linear regression

The target is a number, the real reporting index. On the chart, compare the actual and predicted bars for the same disease and week. If the actual index is 150 and the model predicts 130, the absolute error is 20 index points. If another prediction is off by 10, the mean absolute error across those two predictions is 15 index points.

[Python example using linear regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

### Jayden • Predict the direction with a decision tree

The target is a label. For weekly reports of 10, 14 and 14, week 2 gets a 1 because reports rose. Week 3 gets a 0 because reports stayed level. Use `.shift(1)` within each disease to look up the previous week's count. Skip week 1 because it has no previous week.

Read the tree from the first rule down to a final prediction. In the confusion matrix, rows show actual labels and columns show predicted labels. The diagonal counts correct guesses. If the tree gets four of six guesses right in a practice test, its accuracy is about 67%. In this assignment, changing one guess changes the score by about 17 percentage points.

[Python example for decision tree classification](https://scikit-learn.org/stable/modules/tree.html#classification)
