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

## Option A: GitHub website 

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

## Option B: Terminal or Git Bash

### Step 1: First-time Git setup (only once)

On Mac, open **Terminal** (Applications → Utilities → Terminal, or search with Spotlight). On Windows, install **Git for Windows** if necessary and open **Git Bash**. These are the apps where you type the commands below.

Check that Git is installed:

```bash
git --version
```

If Git is not installed, install it from [git-scm.com](https://git-scm.com/downloads), then open Terminal or Git Bash again.

Set the name and email associated with your Git commits, using your own details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Sign in to GitHub in your browser and accept the invitation to contribute to this repository. You do not need to connect your GitHub account merely to read or clone this public repository. When you push using HTTPS for the first time, Git may ask you to authenticate. Follow the browser sign-in flow offered by your Git credential manager. If Git requests a password directly, GitHub account passwords do not work for Git pushes; use an authorised credential manager or a personal access token instead. Never send your access token to anyone.

### Step 2: Open the repository (do not clone twice)

**If this is your first time downloading the repository:**

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

**If you already cloned it:** Open your existing `mlds-disease-simulation` folder in Terminal or Git Bash. For example, if you are in its parent folder, run:

```bash
cd mlds-disease-simulation
```

Do **not** run `git clone` again just to get new work. Git remembers the connection to `origin` after cloning. Check where you are and which branch is active:

```bash
git status
git branch
git remote -v
```

### Step 3: Choose the correct branch

**Continuing the same assignment:** If you already created a branch for it, do not create another one. First make sure any local changes are saved or committed, then:

```bash
git switch your-existing-branch
git pull origin your-existing-branch
```

If the branch has never been pushed to GitHub, the pull command is not needed yet.

**Starting a different assignment:** Once your earlier work is safely committed and submitted, update your local `main` and create a new branch for the new assignment:

```bash
git switch main
git pull origin main
git switch -c yourname-week03
```

Replace `yourname-week03` with your name and week. **Use `git switch -c` only when creating a new branch.** If you already made that branch, use `git switch yourname-week03` instead.

Do not switch branches or pull while you have unresolved merge conflicts. If Git warns about local changes or conflicts, stop and ask the project leader rather than discarding work.

### Step 4: Complete and save your assigned work

Open the weekly notebook in Jupyter, Colab or another notebook editor. Complete your own section, keep the original notebook filename, and save it. Use the organised directories described above.

Check what changed:

```bash
git status
```

Stage only the files you changed. For example:

```bash
git add "assignments/Week_03_Compare_Diseases.ipynb"
```

If your role also requires a written file or graph, stage those exact files too:

```bash
git add written_assignments/Your_Name/Week_03.md
git add results/your_graph.png
```

Do not run these optional `git add` examples if those files do not exist.

### Step 5: Commit, push and open a pull request

```bash
git status
git commit -m "Complete Week 3 contribution"
git push -u origin yourname-week03
```

Replace the sample branch name with the one shown by `git branch --show-current`. On subsequent pushes of the same branch, `git push` is normally enough after the upstream has been set.

Finally, open the repository's **Pull requests** tab on GitHub, choose **New pull request**, select `main` as the base and your branch as the compare branch, check the changed files, and submit it for review. The project leader merges approved contributions into `main`.

To get the latest shared changes later, update local `main` with `git switch main` followed by `git pull origin main` after safely saving your own work. Your own working branch does not automatically receive the latest changes from `main`; ask the project leader if you need help incorporating them.

## Before submitting

Check that your work is on your own branch, includes the correct files, and does not accidentally replace another teammate's work. You do not need to submit extra written homework unless the weekly assignment asks for it.

The project leader reviews the contributions, combines the approved notebook sections and merges the finished work into `main`.
