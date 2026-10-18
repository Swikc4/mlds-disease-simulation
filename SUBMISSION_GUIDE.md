# Submission Guide

Use this guide for every week of the project. Choose one method and follow its column from top to bottom. You do not need to use both methods.

Everyone works on a personal GitHub branch and opens a pull request for the project leader to review. Do not edit `main` or merge your own pull request.

## Before you start

1. Sign in to [GitHub](https://github.com/) and accept your invitation to [our repository](https://github.com/Swikc4/mlds-disease-simulation).
2. Open [assignments](assignments/) and read the notebook for your week.
3. Find the written questions at the bottom of that notebook.
4. Decide whether to use the GitHub website or Terminal.

## Where to put your work

| Work | Location |
| :--- | :--- |
| Weekly assignment instructions | [assignments](assignments/) |
| Python code for Week 1 | [assignments/Week_01_Assignment.ipynb](assignments/Week_01_Assignment.ipynb) |
| Graph images | [results](results/) |
| Your written answers | Your personal Markdown file in [written_explanations](team_contributions/written_explanations/) |

| Teammate | Personal written file |
| :--- | :--- |
| Ayush | [Ayush.md](team_contributions/written_explanations/Ayush.md) |
| Jayden | [Jayden.md](team_contributions/written_explanations/Jayden.md) |
| Ei Kay | [Ei_Kay.md](team_contributions/written_explanations/Ei_Kay.md) |
| Alex | [Alex.md](team_contributions/written_explanations/Alex.md) |
| Linh | [Linh.md](team_contributions/written_explanations/Linh.md) |

Each person uses the same named Markdown file every week. Add `## Week 1 Assignment`, `## Week 2 Assignment`, and later headings under your name. Keep your previous answers.

## Two ways to submit your assignment

| GitHub website (no Terminal) | Terminal and Git |
| :--- | :--- |
| Step 1. Open [our repository](https://github.com/Swikc4/mlds-disease-simulation). Above the files, click the branch selector labeled `main`. Type a name like `jayden-week01`. Click `Create branch: jayden-week01 from main`. Confirm the selector shows your new branch. | Step 1. If this is your first time, install Git and run `git clone https://github.com/Swikc4/mlds-disease-simulation.git`, then `cd mlds-disease-simulation`. Otherwise, open Terminal in the repository folder you already cloned. |
| Step 2. Open your named `.md` file inside `team_contributions/written_explanations/` while on your branch. Click the pencil icon marked `Edit this file`. Add `## Week 1 Assignment` and answer the written questions from the bottom of the weekly notebook. | Step 2. Run `git switch main`, `git pull origin main`, then `git switch -c jayden-week01`. Change the example branch name to your name and week. Use `git branch --show-current` to confirm you are not on `main`. |
| Step 3. Click `Commit changes`. Enter a message such as `Add my Week 1 written answers`. Commit to your current branch, not `main`. | Step 3. Open your personal Markdown file in a text editor, add the week's heading and answers, and save. Example: `team_contributions/written_explanations/Jayden.md`. |
| Step 4. If your task has Python code, complete and run the assignment `.ipynb` in a notebook editor, then download or save the updated notebook. On your GitHub branch, open the `assignments/` folder, click `Add file` then `Upload files`, choose the saved notebook, and commit. See the notebook instructions below. | Step 4. Open `assignments/Week_01_Assignment.ipynb` in Jupyter or VS Code, complete only your assigned cells, run them, and save the notebook. Your local copy already belongs to the Git repository, so no separate upload is needed. |
| Step 5. If you made graphs, save each as a `.png`. On your branch, open `results/`, click `Add file`, then `Upload files`, select the images, and commit. | Step 5. If you made graphs, save the `.png` images inside the repository's `results/` folder. |
| Step 6. Go to `Pull requests` then `New pull request`, or click `Compare & pull request`. Set base to `main` and compare to your branch. Check `Files changed` for your named Markdown file and any notebook or graph files. Click `Create pull request`. | Step 6. Run `git status`. Use `git add` for your named Markdown file and your other changed files. Then run `git commit -m "Complete my weekly assignment"` and `git push -u origin jayden-week01` (replace with your branch name). Go to GitHub, open `Pull requests`, select `New pull request`, and compare your branch against `main`. |
| Step 7. Wait for the project leader to review. If changes are requested, return to the same branch, fix the file, and commit again. Your pull request updates automatically. | Step 7. Wait for review. For corrections, stay on your branch, edit the file, then run `git add` for the changed file, `git commit -m "Fix review feedback"`, and `git push`. Your pull request updates automatically. |

The branch name `jayden-week01` is an example. Use your own name and the correct week. If you already created a branch for this task, select or switch to that branch instead of creating another one.

## How to run the notebook if you choose the website method

GitHub can display a Jupyter notebook, but it cannot run its Python cells on the ordinary file page. Use a notebook editor. One browser option is [Google Colab](https://colab.research.google.com/).

1. Open Google Colab and sign in.
2. Choose `File`, then `Open notebook`, then the `GitHub` tab.
3. Enter `Swikc4/mlds-disease-simulation`, find `assignments/Week_01_Assignment.ipynb`, and open it. If it is not available through the GitHub tab, download the notebook from the GitHub repository and use Colab's `Upload` tab instead.
4. Find your assigned cell. Write the Python there, run the cell, and check its result. Do not erase other teammates' cells.
5. Choose `File`, then `Download`, then `Download .ipynb`.
6. Return to GitHub and switch to your branch. Open `assignments/`, select `Add file`, then `Upload files`. Upload the notebook you downloaded and commit to your branch.
7. Check `Files changed` in your pull request. If other teammates are editing the same notebook, the project leader must review and combine the separate changes carefully. Never replace the notebook directly on `main`.

If you already use Jupyter or VS Code on your computer, you can open and save the same notebook there instead.

## How to write in your Markdown file

A Markdown file is a normal text file ending in `.md`. It displays your writing on GitHub. You do not have to learn complicated formatting.

For example, Jayden's file can look like this:

```markdown
# Jayden

## Week 1 Assignment

Question 1: How did I build the SIR model?

My answer goes here.

Question 2: What did my results show?

My answer goes here.

## Week 2 Assignment

My next assignment goes here.
```

Use the actual written questions from the bottom of each weekly notebook. Don't copy the sample answers or create a new file each week.

## Check before submitting

1. You are on your own branch, not `main`.
2. Your written answers are in your personal Markdown file under the correct week.
3. If required, your Python notebook runs and your images are in `results/`.
4. Your pull request includes all the files you worked on and nothing unrelated.
5. You opened a pull request and did not merge it yourself.

If you get stuck, send the project leader a screenshot showing where you stopped.
