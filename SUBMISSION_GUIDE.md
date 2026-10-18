# Submission Guide

This guide explains how to submit your work to our GitHub project. You can use **Method A: GitHub Website** (no Terminal needed) or **Method B: Terminal and Git**. Both methods require your own branch and a pull request for review.

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
3. Find the weekly instructions in the [assignments folder](assignments/).
4. Choose one submission method below. **No Terminal installation is needed for Method A.** If you choose Method B, install [Git](https://git-scm.com/downloads). You can also use [GitHub Desktop](https://desktop.github.com/) if you prefer a visual Git application.

## Method A: Submit using the GitHub website (beginner friendly)

You can make changes and submit files from your browser. You do not need to run Git commands.

### 1. Create your own branch

1. Sign in to [our GitHub repository](https://github.com/Swikc4/mlds-disease-simulation).
2. Above the file list, click the branch selector that says `main`.
3. Type a new branch name, such as `alex-week01-task`, then choose **Create branch** from `main`.
4. Check that the branch selector shows **your branch** before you make changes. Never edit `main` for your assignment.

### 2. Add or edit your work

1. Open the appropriate folder in the repository while on **your branch**.
2. To upload completed code, a notebook, explanations, or images saved on your computer, choose **Add file** and then **Upload files**. Drag files onto the page or select them from your computer.
3. To edit an existing text or Markdown file, open it, click the pencil icon, and make your changes. Use this option only for files you are responsible for.
4. Write a brief commit message and select **Commit changes** to **your branch**. Repeat for other files as needed.

**Charts and images:** Save graph images as PNG files and upload them into `results/`. Also submit the Python file or notebook used to create them. Put written explanations in `team_contributions/written_explanations/`.

### 3. Open your pull request

1. Open the repository and choose **Compare & pull request** if GitHub offers it. Otherwise go to **Pull requests** and select **New pull request**.
2. Set **base** to `main` and **compare** to **your branch**.
3. Check **Files changed** to make sure only your intended files are included.
4. Add a short title and description, then select **Create pull request**.
5. Wait for the project manager to review. **Do not merge your own pull request.**

If you are asked to make changes, return to **your branch**, edit or upload the corrected file, and commit it. The existing pull request will update automatically.

## Method B: Submit using Terminal and Git

Choose this method if you are comfortable using Git commands. Copy the commands **one line at a time**, and replace example branch names and file paths with your own.

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

## How to submit your written assignment

Each teammate has **one personal Markdown file** in [written_explanations](team_contributions/written_explanations/). Use the **same file every week**. Do not create another file for Week 2 or Week 3.

| Teammate | Your file |
| :--- | :--- |
| Ayush | [Ayush.md](team_contributions/written_explanations/Ayush.md) |
| Jayden | [Jayden.md](team_contributions/written_explanations/Jayden.md) |
| Ei Kay | [Ei_Kay.md](team_contributions/written_explanations/Ei_Kay.md) |
| Alex | [Alex.md](team_contributions/written_explanations/Alex.md) |
| Linh | [Linh.md](team_contributions/written_explanations/Linh.md) |

In your file, add a new heading for each week and write your answers underneath. Keep your previous weeks' work. For example:

```markdown
# Ayush

## Week 1 Assignment

Write your Week 1 answers here.

## Week 2 Assignment

Write your Week 2 answers here.
```

### Option A: GitHub website

1. Switch from `main` to **your own branch**.
2. Open `team_contributions/written_explanations/` and select your named file.
3. Click the pencil icon to edit it. Add `## Week 1 Assignment` and write your answers below. For future weeks, add `## Week 2 Assignment`, `## Week 3 Assignment`, and so on underneath.
4. Click **Commit changes** and commit to **your branch**.
5. Open a pull request to `main` for review. Include your written assignment and any code or graphs you completed.

### Option B: Terminal

1. In your cloned repository, switch to your own branch.
2. Open your named `.md` file in a text editor. Add your weekly heading and answers, then save it.
3. Stage your file, commit, and push. Replace `YOUR_NAME` and the branch name with yours:

```bash
git add team_contributions/written_explanations/YOUR_NAME.md
git commit -m "Add my Week 1 written assignment"
git push -u origin yourname-week01-task
```

4. Open a pull request to `main` for review.

**Remember:** Your named file is for all your weekly written assignments. Only edit your own file, and never erase previous weeks.

## How to submit charts and images

If your assignment includes a chart, graph, or other image, submit the image **together with the code or work used to create it**. Use Method A or Method B above.

1. **Save your images.** Export each chart as a PNG image with a clear filename, such as `my_chart.png`. If you use Matplotlib, `savefig()` can save the image.
2. **Put the files in the right folder.** Save chart images in the project's `results/` folder. Keep your Python code or notebook in the appropriate project folder on your own branch.
3. **If using Terminal, check your changes.** Inside the cloned project folder, run:

```bash
git branch --show-current
git status
```

4. **If using Terminal, submit your work.** Follow Step 5 below to add, commit, and push your files. For example, replace the filenames with your actual files:

```bash
git add results/my_chart.png
git add path/to/your-code-file
```

5. **Open a pull request.** Follow the pull request steps for your chosen method. Check that **Files changed** includes your images and related work.

**Using the website?** Follow Method A to upload both the images and related code to your branch.

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
| Your written explanation | Your named `.md` file inside `team_contributions/written_explanations/` |
| Approved final weekly notebook | `team_contributions/final_assignments/` |
| Reviewed graphs and findings | `results/` |

## Before submitting

- [ ] I worked on my own branch.
- [ ] I saved and checked my work.
- [ ] I completed my named Markdown file in `team_contributions/written_explanations/`.
- [ ] I explained what I did in my own words.
- [ ] I committed my work to my branch (and pushed it if I used Terminal).
- [ ] I opened a pull request to `main`.

If you get stuck, share the step you reached and the exact error message with the group or the project manager. You are not expected to know every Git command already.
