# Submission Guide

This guide works for every weekly assignment. Choose one method: Section 2 for the GitHub website or Section 3 for Terminal. Beginners should use Section 2. You do not need to complete both methods.

The rule: Work on your own branch, save your work, then open a pull request so the project leader can review it. Do not edit `main` or merge your own pull request.

## 1. Get ready

1. Sign in to [GitHub](https://github.com/).
2. Accept the invitation to collaborate on [our repository](https://github.com/Swikc4/mlds-disease-simulation). If you cannot edit your branch, tell the project leader.
3. Open the [assignments folder](assignments/) and read the instructions for your week.
4. Find the [written explanations folder](team_contributions/written_explanations/). Everyone has one file with their name.

| Teammate | Personal written file |
| :--- | :--- |
| Ayush | [Ayush.md](team_contributions/written_explanations/Ayush.md) |
| Jayden | [Jayden.md](team_contributions/written_explanations/Jayden.md) |
| Ei Kay | [Ei_Kay.md](team_contributions/written_explanations/Ei_Kay.md) |
| Alex | [Alex.md](team_contributions/written_explanations/Alex.md) |
| Linh | [Linh.md](team_contributions/written_explanations/Linh.md) |

Important: Keep all weeks in the same named file. Do not make a new Markdown file each week. Your written answers are separate from the code you write in a notebook.

## 2. Submit using the GitHub website

### Step 1: Create your own branch

1. Go to [our repository](https://github.com/Swikc4/mlds-disease-simulation).
2. At the top of the file list, click the branch selector labeled `main`.
3. Type a branch name. Example: `ayush-week01`. Use your own name and the correct week.
4. Select Create branch: ayush-week01 from main (the button shows your chosen name).
5. Check the branch selector now shows `ayush-week01`, not `main`.

If you already made a branch for this assignment, select that branch instead of creating another one.

### Step 2: Write your answers in your named file

1. While still on your branch, open `team_contributions` and then `written_explanations`.
2. Click your own file. For example, Ayush opens `Ayush.md`. Jayden opens `Jayden.md`.
3. Click the pencil icon, usually labeled Edit this file.
4. Leave your name at the top. Below it, add your new weekly heading and your answers. Example:

```markdown
# Ayush

## Week 1 Assignment

Question 1: What did I do?
My answer: ...

Question 2: What did I learn?
My answer: ...

## Week 2 Assignment

My new answers go here.
```

5. Answer the actual questions at the bottom of the week's assignment notebook. The example above only shows formatting.
6. Click Commit changes (at the upper right or bottom of the editor).
7. Enter a message such as `Add Week 1 written answers`. Choose to commit to your current branch and confirm.

For Week 2, return to the same named file, keep Week 1, and add `## Week 2 Assignment` below it.

### Step 3: Add code, notebooks, or graphs if your task needs them

1. Complete the code in the assigned notebook on your computer or another notebook editor.
2. Save the completed `.ipynb` notebook. If your work is only an image, save the image as `.png`.
3. In GitHub, make sure you are still on your branch. Open the folder where the file belongs.
4. Click Add file, then Upload files. Choose the saved file and select Commit changes.
5. Graph images go in `results/`. For code work, include the notebook or relevant code file. If uploading a notebook would overwrite someone else's work, contact the project leader before doing so.

Note: GitHub's website displays Jupyter notebooks, but it is not a full notebook editor. Use a notebook editor to run and save Python cells before uploading your changes. You can use the GitHub website directly for the written `.md` file.

### Step 4: Create your pull request

1. Go back to the repository page.
2. Click Compare & pull request if GitHub shows it. If not, click Pull requests, then New pull request.
3. Set base to `main` and compare to your branch.
4. Open Files changed. Check that your named Markdown file and any code or graph files are included, with no unrelated edits.
5. Give it a title such as `Ayush Week 1 assignment`. Briefly describe your work.
6. Click Create pull request. Stop here and wait for the project leader to review it. Do not click Merge.

If something needs correction, edit the files on the same branch and commit again. The existing pull request updates automatically.

## 3. Submit using Terminal

Choose this method if you already use Git. Run these commands in order and replace the example name and week with yours.

### Step 1: Get the repository

For your first time only, open Terminal and run:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

If you cloned the repository before, open Terminal in your existing `mlds-disease-simulation` folder instead. Do not clone it again inside itself.

### Step 2: Create a branch

```bash
git switch main
git pull origin main
git switch -c ayush-week01
```

The branch name is an example. Replace it with your own name and week. If you already have a branch for the assignment, switch to it instead of using `git switch -c`.

Check which branch you are using:

```bash
git branch --show-current
```

It should show your branch, not `main`.

### Step 3: Write your assignment

1. Open `team_contributions/written_explanations/` in a text editor.
2. Open your named Markdown file. For example, Ayush edits `Ayush.md`.
3. Add `## Week 1 Assignment` followed by your answers to that week's written questions.
4. Save the file. Keep older assignments when you add future weeks.
5. Complete and save any notebook, code, or graph work required for your task.

### Step 4: Save and push your changes

To see what you changed:

```bash
git status
```

Stage only your files. For example, Ayush stages his written file:

```bash
git add team_contributions/written_explanations/Ayush.md
git commit -m "Complete my weekly assignment"
git push -u origin ayush-week01
```

Replace `Ayush.md` and `ayush-week01` with your own file and branch. If you also changed a notebook or added a graph, use an additional `git add` command for each file before `git commit`.

### Step 5: Create a pull request

1. Open [our repository](https://github.com/Swikc4/mlds-disease-simulation) in your browser.
2. Click Compare & pull request, or choose Pull requests then New pull request.
3. Select `main` as the base and your branch as the compare branch.
4. Review Files changed, then click Create pull request.
5. Wait for review. Do not merge the pull request yourself.

If changes are requested, edit your files on the same branch, then run:

```bash
git add path/to/your/changed-file
git commit -m "Fix review feedback"
git push
```

The original pull request updates automatically.

## 4. Check where your files belong

| Work | Folder or file |
| :--- | :--- |
| Weekly instructions | `assignments/` |
| Personal written answers | Your named `.md` in `team_contributions/written_explanations/` |
| Python simulations and other code | The assigned notebook or code file on your branch |
| Graph images | `results/` |
| Approved final work | Managed by the project leader |

## 5. Final submission checklist

1. Check that you are using your own branch.
2. Check that your written answers are under the correct week in your own Markdown file.
3. Check that any required Python code runs and that you have included any graph images.
4. Open your pull request and inspect Files changed.
5. Wait for the project leader's review. Do not merge your own work.

If a button or menu looks different on your device, ask the project leader and share a screenshot of the step where you got stuck.
