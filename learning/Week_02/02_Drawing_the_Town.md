# Week 2 Drawing the Town

Week 1 drew line graphs. Week 2 adds scatter plots, meeting lines, and animation. Every line has a comment saying what it does.

## 1. Scatter plots draw dots

```python
import matplotlib.pyplot as plt   # load the plotting tools

xs = [0, 1, 2]   # x positions of three dots
ys = [0, 1, 0]   # matching y positions
plt.scatter(xs, ys, color="red")   # draw one dot per (x, y) pair
plt.show()                         # display the figure
```

The town draws one dot per person. Each person's grid spot comes from their id:

```python
# given in the assignment: id 0..99 mapped onto a 10 by 10 grid
POSITIONS = [(i % 10, i // 10) for i in range(100)]
# i % 10 is the column (0 to 9); i // 10 is the row (0 to 9)
```

The spot is only for display; it does not mean people live there.

## 2. Colors come from a dictionary

```python
# given in the assignment: one color per state
COLORS = {"S": "#4C9BE0", "E": "#F0A030", "I": "#E04040", "R": "#50B060"}

plt.scatter([0], [0], color=COLORS["I"])   # draw one dot in the infectious color
```

The values like `"#E04040"` are color codes. `COLORS[state]` looks up the right color, so a person changes color when their state changes.

## 3. plot() also draws a single line between two points

In Week 1, `plot` drew a whole curve. With only two points, it draws one straight line:

```python
plt.plot([0, 7], [2, 5], color="#888888", linewidth=0.5)
# x goes from 0 to 7, y goes from 2 to 5: a thin gray line between those points
```

The town display draws one of these lines for every meeting that day, connecting the two people who met.

## 4. A function that draws one day

The assignment gives you this empty function to fill in:

```python
def draw_town(ax, states, meetings, day):
    ...
```

- `ax` is the drawing area for one figure.
- `states` is the list of 100 state letters for that day.
- `meetings` is the list of `(a, b)` meeting pairs for that day.
- `day` is the day number, used in the title.

Useful `ax` commands:

```python
ax.clear()                 # wipe the previous day before drawing this one
ax.set_title("Day 5")      # write a title
ax.scatter(xs, ys, color=COLORS["S"])   # draw the dots of one state
ax.plot([x1, x2], [y1, y2], color="#888888")   # draw one meeting line
ax.set_xticks([])          # hide the x axis numbers
ax.set_yticks([])          # hide the y axis numbers
ax.legend()                # show which color is which state
```

## 5. Saving the line graph as an image

```python
days = [0, 1, 2, 3]                 # made-up x values
steps = [4000, 5200, 6100, 4800]    # made-up y values
plt.plot(days, steps)               # draw one line from two lists, like Week 1
plt.title("My Steps This Week")
plt.savefig("results/steps_graph.png")   # write the figure to a file in results/
```

`savefig` must come before `plt.show()`, or the saved file is empty.

## 6. FuncAnimation replays the days

```python
from matplotlib.animation import FuncAnimation   # the animation tool
from IPython.display import HTML                 # lets the notebook play it

fig, ax = plt.subplots(figsize=(6, 6))   # one figure to draw into

def update(frame):                       # called once per day; frame is the day index
    draw_town(ax, town_snapshots[frame], town_meetings[frame], frame)
    # redraws the dots and lines using that day's saved snapshot

anim = FuncAnimation(fig, update, frames=len(town_snapshots), interval=300)
# frames: how many days to replay; interval: milliseconds between days

HTML(anim.to_jshtml())   # play the animation inside the notebook, no extra installs
```

The key idea: the animation only *replays* snapshots that the simulation already saved. All the disease logic happens in the run; the display just shows it.
