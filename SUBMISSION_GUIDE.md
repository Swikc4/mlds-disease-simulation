# Submit your assignment

## On GitHub

1. Use your existing branch for this assignment. For a new week, create a branch from the latest `main`, such as `jayden-week04`.
2. Open your weekly notebook in [assignments](assignments/). Download it and use Jupyter or Colab to work on your section.
3. Save the notebook with the same filename. Upload it to the same folder on your branch and commit the change.
4. Open a pull request with `main` as the base and your branch as the compare branch. Check **Files changed** before submitting. The project leader reviews and merges it.

## In Terminal

Clone the repo once. For later assignments, open the folder you already have.

```bash
git clone https://github.com/Swikc4/mlds-disease-simulation.git
cd mlds-disease-simulation
```

For a new week, save any work in progress, then create a branch from the latest `main`:

```bash
git switch main
git pull origin main
git switch -c yourname-week04
```

If your branch already exists, use `git switch yourname-week04`. After saving your section, add only the files you changed:

```bash
git status
git add assignments/Week_04_Intereactive_Sliders.ipynb
git commit -m "Complete my Week 4 section"
git push -u origin yourname-week04
```

Replace the sample branch and notebook names with yours. Open your pull request on GitHub using step 4 above.

## Extra files

- Put written answers in [written_assignments](written_assignments/) under your name, if your role asks for them.
- Put any required graphs or shared results in [results](results/).
- If Git flags a conflict in a notebook, ask the project leader to combine the changes.
