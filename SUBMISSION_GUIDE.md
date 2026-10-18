# Submission Guide

Choose one option: GitHub website or Terminal. Both options let you submit your work for review. You do not need to follow both.

## 1. Find your files

Read your current assignment in [assignments](assignments/).

Each teammate has a folder for written answers:

- [Ayush](team_contributions/written_explanations/Ayush/)
- [Jayden](team_contributions/written_explanations/Jayden/)
- [Ei Kay](team_contributions/written_explanations/Ei_Kay/)
- [Alex](team_contributions/written_explanations/Alex/)
- [Linh](team_contributions/written_explanations/Linh/)

Inside your folder, open `Week_01.md` for Week 1. For Week 2, create `Week_02.md` in the same folder. Use one separate file per week. Do not delete your earlier work.

Simulation, graph, and test code belongs in the assigned notebook or code file. Save graph images in `results/`.

## 2. Option A: GitHub website

This option does not require Terminal.

### Step 1. Create a branch

1. Sign in to [GitHub](https://github.com/) and accept the repository collaboration invitation.
2. Open [our repository](https://github.com/Swikc4/mlds-disease-simulation).
3. Above the file list, click the button showing `main`.
4. Type your own branch name, such as `jayden-week01`.
5. Click `Create branch` from `main`.
6. Make sure the branch button now shows your new branch.

### Step 2. Submit your written answers

1. While viewing your branch, open `team_contributions`.
2. Open `written_explanations`.
3. Open your personal folder, then `Week_01.md`.
4. Click the pencil icon to edit the file.
5. Write your answers to the written questions at the bottom of the weekly assignment.
6. Click `Commit changes`, write a short message, and confirm the change is saved to your branch.

For future weeks, open your personal folder, click `Add file` then `Create new file`, and create `Week_02.md` or the correct week number.

### Step 3. Add your code or graphs

1. Complete and run your Python code in Jupyter, Colab, or another notebook editor.
2. Save your completed notebook as an `.ipynb` file.
3. On GitHub, switch to your own branch and open the `assignments/` folder.
4. Click `Add file` then `Upload files`.
5. Select your saved notebook and click `Commit changes` to your branch.
6. If you created graph images, open `results/` on your branch and upload the PNG images there.

GitHub can display notebooks, but its normal file preview cannot run their Python cells. If your notebook upload would replace a teammate's changes, ask the project leader to help combine the work before merging.

### Step 4. Request review

1. Open the repository's `Pull requests` tab.
2. Click `New pull request`.
3. Choose `main` for the base and your branch for the compare branch.
4. Click `Files changed` and confirm your written assignment and any code or graphs are included.
5. Click `Create pull request`.

Do not merge the pull request yourself. Wait for the project leader to review it.

## 3. Option B: Terminal and Git

Use this option if you prefer working on your computer. Copy one command at a time. The name `jayden-week01` is an example, so replace it with your own name and week.

### Step 1. Download the project

Run these commands once when setting up the project:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
```

```bash
cd mlds-disease-simulation
```

If you already downloaded the project with Git, open Terminal in that existing folder instead.

### Step 2. Create your branch

```bash
git switch main
```

```bash
git pull origin main
```

```bash
git switch -c jayden-week01
```

Check that you are on the right branch:

```bash
git branch --show-current
```

### Step 3. Complete your work

1. Open your personal `Week_01.md` file in a text editor. For example, Jayden's file is in `team_contributions/written_explanations/Jayden/`.
2. Write your answers and save the file.
3. Complete and save your assigned notebook or Python file. Save graph PNG images in `results/` if required.

### Step 4. Save your changes to GitHub

Add your written file. Example for Jayden:

```bash
git add team_contributions/written_explanations/Jayden/Week_01.md
```

If you changed the notebook, add it too:

```bash
git add assignments/Week_01_Assignment.ipynb
```

If you created graph files, add your actual image paths, for example:

```bash
git add results/my_graph.png
```

Check the files you staged:

```bash
git status
```

Save the commit:

```bash
git commit -m "Complete Week 1 work"
```

Upload your branch:

```bash
git push -u origin jayden-week01
```

Use your own branch name in the final command. Only add files that you actually changed.

### Step 5. Request review

1. Open [our repository](https://github.com/Swikc4/mlds-disease-simulation).
2. Click `Pull requests`, then `New pull request`.
3. Choose `main` as the base and your branch as the compare branch.
4. Check `Files changed`.
5. Click `Create pull request`. Do not merge it yourself.

## 4. Next week and corrections

For Week 2, create a new branch from the latest `main` and add a new `Week_02.md` file inside your own folder. Keep `Week_01.md`.

If the project leader asks for a correction, return to the same branch, edit the file, and commit the correction. Your existing pull request will update.

## 5. Before submitting

1. You worked on your own branch, not `main`.
2. Your answers are in your named folder and the correct week's Markdown file.
3. Your code and graphs are included if your task requires them.
4. Your pull request includes only your own intended changes.
5. You have opened a pull request and are waiting for review.

If you get stuck, share a screenshot and the step number with the project leader.
