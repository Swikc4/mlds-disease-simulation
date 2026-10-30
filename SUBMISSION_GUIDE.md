# Submission Guide

Use either the GitHub website or Terminal to submit your contribution. You do not need to use both.

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

## Option A: GitHub website

1. Open [the repository](https://github.com/Swikc4/mlds-disease-simulation) and create your own branch from the latest `main`, such as `jayden-week03`.
2. Open the correct file under `assignments/` and complete only your assigned work. You may edit or upload your notebook using the same filename.
3. If required, save your own Markdown explanation in `written_assignments/Your_Name/`. Put graph images in `results/`.
4. Commit your changes to your branch, not `main`.
5. Open a pull request with `main` as the base, check **Files changed**, and ask the project leader to review it. Do not merge it yourself.

Notebook files may conflict if multiple teammates edit the same notebook. If that happens, ask the project leader to combine the changes rather than overwriting another person's work.

## Option B: Terminal

Clone the repository only if you have not already cloned it:

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

If it is already on your computer, open Terminal inside that repository folder. Start a fresh branch for the week:

```bash
git switch main
git pull origin main
git switch -c yourname-week03
```

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
