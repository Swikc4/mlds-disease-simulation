# Submission Guide

This guide explains how to submit your work to our GitHub project. If this is your first time using GitHub, start at Step 1.

## A few words to know

- **Repository (repo):** The shared project and its files.
- **Clone:** Download a working copy of the repo to your computer.
- **Branch:** Your own version of the project where you can make changes without editing the team's main version.
- **Commit:** Save a set of changes with a short message.
- **Push:** Upload your commits to GitHub.
- **Pull request (PR):** Ask the project manager to review your changes before adding them to the main project.

## Step 1: Get ready

1. Create a free account at [GitHub](https://github.com/) if you do not have one.
2. Send your **GitHub username** to the project manager.
3. Install [Git](https://git-scm.com/downloads) and open Terminal on Mac or Git Bash/Terminal on Windows. If you prefer a visual app, [GitHub Desktop](https://desktop.github.com/) can handle cloning, branching, committing, pushing, and pull requests.
4. Find the weekly instructions in the [assignments folder](assignments/).

The steps below use Git commands. You can copy them **one line at a time**. Text in quotation marks is an example; use your own meaningful names.

## Step 2: Clone the project (first time only)

Go to the folder on your computer where you want the project. In Terminal, run:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

The first command downloads the project. The second moves Terminal into the project folder. You only need to clone **once**.

Already cloned it? Open Terminal in your existing project folder instead of cloning again.

## Step 3: Make your own branch

Before starting a new task, get the latest team version and create a branch:

```bash
git switch main
git pull origin main
git switch -c yourname-week01-task
```

Replace `yourname-week01-task` with a descriptive name, such as `alex-week01-charts`. For future tasks, use a new branch name. **Do not work directly on `main`.**

If `git switch` is not recognized, ask for help updating Git.

## Step 4: Do your work

1. Open the assignment and read what your chosen task requires.
2. Work in your own files on your branch. Keep explanations clear enough that someone new to Python can follow them.
3. Put individual written explanations in `team_contributions/written_explanations/`. Keep work related to notebooks or code in an appropriate project folder, without changing a teammate's files.
4. Run your code and check that it works before submitting. If you used an outside source or tool, acknowledge it in your explanation.

**Do not overwrite another person's work.** The project manager will organize approved contributions into the final weekly notebook.

## Step 5: Save and upload your changes

From inside the project folder in Terminal, run:

```bash
git status
```

This shows files you changed. Then add **only the files for your task**:

```bash
git add path/to/your-file
git commit -m "Complete my weekly task"
git push -u origin yourname-week01-task
```

Replace `path/to/your-file` with your actual file path and `yourname-week01-task` with your actual branch name. The commit message should briefly describe what you did.

If Git says there is nothing to commit, check `git status` and make sure your files were saved. GitHub may ask you to sign in; use the sign-in instructions it provides. Do not share passwords or access tokens in the group chat.

## Step 6: Open a pull request

1. Open our [GitHub repository](https://github.com/Swikc4/mlds-disease-simulation).
2. After pushing, look for **Compare & pull request**. If it does not appear, go to **Pull requests**, select **New pull request**, and choose your branch.
3. Check that the **base** branch is `main` and the **compare** branch is your own branch.
4. Add a title, such as `Week 1 charts`, and briefly describe what you completed, how you tested it, and any issues.
5. Click **Create pull request**. Do **not** merge it yourself.

The project manager will review your PR, ask questions or request changes if needed, and combine approved work.

## Step 7: If you are asked to fix something

Keep working on the **same branch**. Make the correction, then run:

```bash
git add path/to/your-file
git commit -m "Address review feedback"
git push
```

Your existing pull request will update automatically. You do not need to open another one.

## Where our work goes

| Work | Location |
| :--- | :--- |
| Current assignment instructions | `assignments/` |
| Your code or notebook changes | Your branch and pull request |
| Your written explanation | `team_contributions/written_explanations/` |
| Approved final weekly notebook | `team_contributions/final_assignments/` |
| Reviewed graphs and findings | `results/` |

## Before submitting

- [ ] I worked on my own branch.
- [ ] I saved and checked my work.
- [ ] I explained what I did in my own words.
- [ ] I pushed my changes to GitHub.
- [ ] I opened a pull request to `main`.

If you get stuck, share the step you reached and the exact error message with the group or the project manager. You are not expected to know every Git command already.
