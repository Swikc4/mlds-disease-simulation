# Submission Guide

Use either the GitHub website or Terminal to submit your contribution. You do not need to use both.

## Returning contributors

If you have cloned this repository once, **do not clone it again**. Open your existing project folder and pull new changes when you need them.

If you already created a branch for the assignment you are continuing, **do not create that branch again**. Switch to your existing branch and carry on. You only need a new branch when starting a separate assignment after your previous work has been submitted or merged. For a new week, start from the latest `main` so you do not accidentally resubmit old changes.

On the GitHub website, simply select your existing branch using the branch selector.

In Terminal, check your work first:

```bash
git status
git branch
```

If you are continuing work on an existing branch, switch to it and pull its remote updates when available:

```bash
git switch your-existing-branch
git pull origin your-existing-branch
```

If you are starting a different week's assignment, make sure your current changes are committed or saved before switching to `main`, then update `main` and create a new weekly branch.

## Where files belong

- [assignments](assignments/) — the shared weekly Jupyter notebooks.
- [written_assignments](written_assignments/) — any individual written answers or research notes required for your assigned role. Each person has their own folder.
- [results](results/) — graphs, figures and final findings.
- [learning](learning/) — learning notes and reference material.
- [research](research/) — approved sources.

Current notebooks:
- Week 1: `assignments/Week_01_SIR_SEIR_Models.ipynb`
- Week 2: `assignments/Week_02_Building _Towns.ipynb`
- Week 3: `assignments/Week_03_Compare_Diseases.ipynb`

Use the exact existing notebook filename, including spaces, if you work on it. Complete your assigned section and preserve everyone else's work. You only need a separate Markdown file if your role specifically asks for one. If needed, save it as `written_assignments/Your_Name/Week_03.md` (change the week number to match).

## Option A: GitHub website (no Terminal needed)

### Step 1: Select or create your branch

1. Sign in to [GitHub](https://github.com/) and open [our repository](https://github.com/Swikc4/mlds-disease-simulation).
2. Above the file list, open the branch selector. If you already have a branch for this assignment, select it — do not create it again.
3. If this is a new assignment and you need a new branch, select `main`, type a name such as `jayden-week03`, then choose **Create branch from main**.
4. Check that the selector shows the branch you intend to work on before editing any files.

### Step 2: Complete your assigned work

1. Open the `assignments/` folder and find the notebook for your week.
2. Download the notebook if you need to use Jupyter, Colab or PyCharm to complete its Python cells. You cannot run notebook code on the GitHub website.
3. Complete **only your assigned role** and save the whole notebook using its original filename.
4. Return to your branch on GitHub. Open `assignments/`, choose **Add file → Upload files**, and upload the saved notebook. Make sure you are replacing the correct notebook on **your branch**, not on `main`.
5. Enter a short commit message and select **Commit changes** to save it to your branch.

If you only need to edit a Markdown file, open it on your branch, click the pencil icon, make your changes, then select **Commit changes**.

### Step 3: Add any other required files

1. If your role requires a separate written explanation, open `written_assignments/`, then your name's folder. Open or create `Week_03.md` (or the correct week number) and commit your changes.
2. If you created a graph, open `results/` on your branch, select **Add file → Upload files**, upload the image, and commit it.
3. Do not create an extra written assignment unless your role asks for one.

### Step 4: Request review

1. Open the **Pull requests** tab in the repository.
2. Choose **New pull request** (or **Compare & pull request** if GitHub offers it).
3. Check that **base** is `main` and **compare** is your branch.
4. Select **Files changed** and make sure only your intended work is included.
5. Choose **Create pull request**. The project leader will review and merge it into `main`; do not merge it yourself.

If GitHub reports a notebook conflict or warns that your upload would overwrite another teammate's work, ask the project leader to combine the changes.

## Option B: Terminal

Clone the repository only if you have not already cloned it:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

If it is already on your computer, open Terminal inside that repository folder instead of cloning again. To start a **new week's assignment**, run:

```bash
git switch main
git pull origin main
git switch -c yourname-week03
```

If you already made a branch for **this same assignment**, use `git switch your-existing-branch` instead of `git switch -c`. Do not try to create the same branch twice. Use `git status` before switching so you do not lose track of uncommitted changes.

Complete your assigned work and save the files. Check the changes before committing:

```bash
git status
git add assignments/
```

If you also changed an individual written file or added graphs, stage those specific files too, for example:

```bash
git add written_assignments/Your_Name/Week_03.md
git add results/your_graph.png
```

Then commit and push your branch:

```bash
git commit -m "Complete Week 3 contribution"
git push -u origin yourname-week03
```

Replace `yourname-week03` with your own branch name. Open a pull request to `main` on GitHub and wait for review.

## Before submitting

Check that your work is on your own branch, includes the correct files, and does not accidentally replace another teammate's work. You do not need to submit extra written homework unless the weekly assignment asks for it.

The project leader reviews the contributions, combines the approved notebook sections and merges the finished work into `main`.
