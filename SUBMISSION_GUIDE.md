# Submission Guide

This guide works for Week 1 and every later week. You have two ways to submit: through the GitHub website or through Terminal. Choose one method. Both methods end with a pull request so the project leader can review your work.

## 1. Where your work belongs

Open our [GitHub repository](https://github.com/Swikc4/mlds-disease-simulation).

| Your work | Location |
| :--- | :--- |
| Assignment instructions | `assignments/` |
| Written answers | `team_contributions/written_explanations/YOUR_NAME/Week_01.md` |
| Simulation, graph, or test code | Your assigned notebook or code file |
| Saved graph images | `results/` |
| Final reviewed work | Project leader handles `team_contributions/final_assignments/` |

Each person has their own folder:

| Teammate | Personal folder | Week 1 writing file |
| :--- | :--- | :--- |
| Ayush | [Ayush](team_contributions/written_explanations/Ayush/) | [Week_01.md](team_contributions/written_explanations/Ayush/Week_01.md) |
| Jayden | [Jayden](team_contributions/written_explanations/Jayden/) | [Week_01.md](team_contributions/written_explanations/Jayden/Week_01.md) |
| Ei Kay | [Ei_Kay](team_contributions/written_explanations/Ei_Kay/) | [Week_01.md](team_contributions/written_explanations/Ei_Kay/Week_01.md) |
| Alex | [Alex](team_contributions/written_explanations/Alex/) | [Week_01.md](team_contributions/written_explanations/Alex/Week_01.md) |
| Linh | [Linh](team_contributions/written_explanations/Linh/) | [Week_01.md](team_contributions/written_explanations/Linh/Week_01.md) |

Use a different file for each week, inside the same personal folder:

```text
written_explanations/
    Ayush/
        Week_01.md
        Week_02.md
        Week_03.md
    Jayden/
        Week_01.md
        Week_02.md
    Ei_Kay/
        Week_01.md
    Alex/
        Week_01.md
    Linh/
        Week_01.md
```

Week 1 files already exist. The Week 2 and Week 3 filenames above only illustrate the future structure. Create them when those weeks are assigned.

## 2. Submit your assignment: choose one method

| Step | GitHub website | Terminal and Git |
| :--- | :--- | :--- |
| 1. Open the project | Sign in to [GitHub](https://github.com/), accept your invitation, and open [our repository](https://github.com/Swikc4/mlds-disease-simulation). | Install [Git](https://git-scm.com/downloads). The first time, run `git clone https://github.com/Swikc4/mlds-disease-simulation.git` and then `cd mlds-disease-simulation`. If you already cloned it, open that existing folder. |
| 2. Make your branch | Click the `main` branch selector above the files. Type `jayden-week01` and click `Create branch`. Confirm the selector shows your branch, not `main`. | Run `git switch main`, then `git pull origin main`, then `git switch -c jayden-week01`. Check with `git branch --show-current`. |
| 3. Write your answers | While on your branch, click `team_contributions` → `written_explanations` → your name → `Week_01.md`. Click the pencil icon, answer the questions at the bottom of the Week 1 notebook, then click `Commit changes` and choose your branch. | Open `team_contributions/written_explanations/Jayden/Week_01.md` in a text editor, type your answers, and save. Stage it with `git add team_contributions/written_explanations/Jayden/Week_01.md`. |
| 4. Submit code or graphs | Run your code in Jupyter or another notebook editor and save the `.ipynb` file. On your branch, open its destination folder, click `Add file` → `Upload files`, select it, then `Commit changes`. Upload graph `.png` files to `results/`. | Save and run your notebook locally. Stage files you actually changed, for example `git add assignments/Week_01_Assignment.ipynb` or `git add results/your_graph.png`. |
| 5. Save your changes | For every edited or uploaded file, confirm `Commit changes` saves to your branch, not `main`. | Run `git status`, then `git commit -m "Complete Week 1 work"`, then `git push -u origin jayden-week01`. |
| 6. Open a pull request | Click `Compare & pull request`. If it is not shown, go to `Pull requests` → `New pull request`. Set base to `main` and compare to your branch. | After pushing, open [the repository](https://github.com/Swikc4/mlds-disease-simulation) in a browser. Click `Compare & pull request` or `Pull requests` → `New pull request`. Set base to `main` and compare to your branch. |
| 7. Check and submit | Open `Files changed` to check your written file and any code or graphs. Click `Create pull request` and wait for review. Do not merge it. | Check `Files changed` for your files. Click `Create pull request` and wait for review. Do not merge it. |

The branch `jayden-week01` and the file `Jayden/Week_01.md` are examples. Replace Jayden with your own name and use the current week. You only need one submission method.

### For the next week

Create a new branch from the latest `main`. Keep the same personal folder but create a separate file, such as `Week_02.md` or `Week_03.md`. On the website, open your personal folder and click `Add file` → `Create new file`. In Terminal, create the new file in that folder with a text editor and stage it with `git add`. Never delete your earlier assignments.

If your pull request needs corrections, edit the same branch and commit again. For Terminal, run `git add` for the corrected file, `git commit -m "Fix review feedback"`, and `git push`. Your existing pull request updates automatically.

## 3. Final check before submitting

1. Your branch is not `main`.
2. Your written answers are in `YOUR_NAME/Week_01.md`, or the matching file for your assigned week.
3. You included your code notebook and graph files if your task requires them.
4. Your pull request includes only your intended changes.
5. You created the pull request for the project leader to review. Do not merge it yourself.

If you get stuck, share the step number and a screenshot or error message with the project leader.
