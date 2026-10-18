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

## 2. Two ways to submit, side by side

| Step | Method A: GitHub website | Method B: Terminal and Git |
| :--- | :--- | :--- |
| 1. Start | Sign in to [GitHub](https://github.com/), accept your collaboration invitation, and open [the repository](https://github.com/Swikc4/mlds-disease-simulation). | Install [Git](https://git-scm.com/downloads). Open Terminal, clone the repository once, and enter its folder. |
| 2. Make a branch | Above the repository file list, click `main`. Type a name such as `jayden-week01` and select `Create branch`. Make sure the selector now shows your branch. | Run `git switch main`, `git pull origin main`, then `git switch -c jayden-week01`. Use your own branch name. |
| 3. Write answers | On your branch, open `team_contributions`, then `written_explanations`, then your name, then `Week_01.md`. Click the pencil icon, write answers, and click `Commit changes` to your branch. | Open your personal `Week_01.md` in a text editor, write answers, and save. Stage the file with `git add`. |
| 4. Add code or graphs | Run the notebook in a notebook editor, then save it. On your branch, open the correct folder, click `Add file` then `Upload files` and commit. Upload graph PNG files into `results/`. | Run and save the notebook locally. Put PNG graphs in `results/`. Stage each changed code or image file with `git add`. |
| 5. Save changes | After each edit or upload, click `Commit changes` and ensure the commit is made to your branch, not `main`. | Run `git status`, then `git commit -m "Complete Week 1 assignment"` and `git push -u origin jayden-week01`. |
| 6. Submit for review | Select `Compare & pull request`, or open `Pull requests` then `New pull request`. Set base to `main` and compare to your branch. | After pushing, open the repository in a web browser. Select `Compare & pull request`, or open `Pull requests` then `New pull request`. |
| 7. Finish | Check `Files changed` includes your written file and any code or graphs, then click `Create pull request`. Do not merge. | Check `Files changed` includes your written file and any code or graphs, then click `Create pull request`. Do not merge. |

Read the specific instructions for your chosen method below.

## 3. Method A: GitHub website instructions

### Edit your weekly written assignment

1. Start from the repository homepage. Check the branch selector above the file list. It must show your branch, not `main`.
2. Click `team_contributions` → `written_explanations` → your own name → `Week_01.md`.
3. Click the pencil icon labeled `Edit this file`.
4. Under `## Week 1 Assignment`, type your answers to the questions at the end of the Week 1 notebook.
5. Click `Commit changes`. Enter a message such as `Add my Week 1 answers`. Select your current branch and confirm.
6. Return to the repository, then open a pull request to `main` after your code or other work is ready.

### For Week 2 and later

1. Switch to a new branch created from the updated `main` branch.
2. Open your personal folder, for example `written_explanations/Ayush/`.
3. Click `Add file` → `Create new file`.
4. Name the new file `Week_02.md` (or `Week_03.md` for Week 3).
5. Type a heading such as `# Ayush: Week 2 Assignment`, then answer that week's questions.
6. Click `Commit changes` to your branch and open a pull request for review.

Never erase or replace another week's file.

### Submit your Python notebook or graphs

The GitHub file preview is not a Python notebook editor. Use a notebook editor such as Jupyter or Google Colab to run and save your code first, then upload the saved `.ipynb` file to your branch. GitHub Codespaces may also allow you to work in an editor in your browser if enabled.

For example, Jayden's SIR code belongs in `assignments/Week_01_Assignment.ipynb`; Alex's graph images belong in `results/`. If multiple teammates edit the same notebook, the project leader must review and combine the changes. Do not overwrite a teammate's work on `main`.

To upload on GitHub, open the destination folder on your branch, choose `Add file` → `Upload files`, select the saved file, then `Commit changes`. Check your pull request's `Files changed` tab to confirm the files are there.

## 4. Method B: Terminal instructions

### First time only: get the project

Run one command at a time:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

If you already cloned it, open Terminal inside your existing project folder instead.

### Create your assignment branch

```bash
git switch main
git pull origin main
git switch -c jayden-week01
git branch --show-current
```

Replace `jayden-week01` with your own name and week. Create a new branch for the next assignment. Do not work directly on `main`.

### Write and save your work

Open your personal file, such as `team_contributions/written_explanations/Jayden/Week_01.md`, in a text editor. Write answers and save it. Finish and save your code or graph files as well.

Stage the exact files you changed. Example for Jayden:

```bash
git add team_contributions/written_explanations/Jayden/Week_01.md
git add assignments/Week_01_Assignment.ipynb
git status
git commit -m "Complete Week 1 work"
git push -u origin jayden-week01
```

Only stage the notebook if you actually edited it. Replace paths and the branch with your own. For Alex, stage his graph images with `git add results/your_graph.png`.

For a future week, create a new `Week_02.md` file in your existing personal folder, then stage and commit that new file. Keep `Week_01.md`.

### Open a pull request

After pushing, open the repository in a browser. Click `Compare & pull request` or `Pull requests` → `New pull request`. Set base to `main`, compare to your branch, check `Files changed`, and click `Create pull request`.

If you need to correct something later, keep the same branch, make the changes, then run:

```bash
git add path/to/changed-file
git commit -m "Fix review feedback"
git push
```

The same pull request will update.

## 5. Final check before submitting

1. Your branch is not `main`.
2. Your written answers are in `YOUR_NAME/Week_01.md`, or the matching file for your assigned week.
3. You included your code notebook and graph files if your task requires them.
4. Your pull request includes only your intended changes.
5. You created the pull request for the project leader to review. Do not merge it yourself.

If you get stuck, share the step number and a screenshot or error message with the project leader.
