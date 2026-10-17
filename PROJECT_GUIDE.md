# Updated Project Schedule and Team Guide

**ML & Data Science Club, Baruch College**  
**Status: Planning**  
**First meeting: October 16, 2026, 10:30 to 11:00 AM**  
**Showcase: December 10, 2026**

## Our research question

Why do some diseases spread much faster than others, and what slows each one down the most?

## Why the schedule changed

Our first assignment combines SIR and SEIR into Week 1. The work is divided among five teammates, so we can build the two simple models in parallel. This schedule is a plan, not a promise. We'll check what everyone knows at our first meeting and adjust deadlines if needed.

## Weekly plan

| Dates | Focus | Deliverable |
| :--- | :--- | :--- |
| Oct 17 to 23 | First meeting, Python basics, SIR and SEIR | One reviewed SIR and SEIR notebook |
| Oct 24 to 30 | Build the virtual town | One disease prototype with daily counts |
| Oct 31 to Nov 6 | Research and compare three diseases | Checked parameter table and comparison charts |
| Nov 7 to 13 | Add interactive sliders and graphs | Working Jupyter demo |
| Nov 14 to 20 | Run simulations and add basic machine learning | Linear regression, decision tree, and tests on unseen runs |
| Nov 21 to 27 | Combine and test the core | Working model, chart reviews and fixes |
| Nov 28 to Dec 4 | Finish documentation, findings, and optional improvements | Updated README, findings and slides |
| Dec 5 to 9 | Rehearse and freeze | Final tested presentation and backup demo |
| Dec 10 | Showcase | Live group presentation |

## How we will divide the work

Everyone can choose the tasks they want to work on based on their interests, experience, and what they would like to learn. We will discuss our choices as a group to make sure the work is covered and shared fairly. I will coordinate our progress, help when needed, review pull requests, and combine approved contributions. We can adjust tasks as the project develops.

## Working together on GitHub

We will post only the current assignment under `assignments/`. Everyone works on their own branch and submits a pull request. After review, I will combine accepted sections into one final notebook under `our_work/assignments/`. Teammates' individual writing will go in `our_work/explanations/`. GitHub does not automatically combine separate notebooks. We will keep checked findings under `results/` and sources under `research/`.

## Research and data

SIR and SEIR begin with teaching assumptions, not real patients. The town will generate simulated data. We already have the starting CDC and published sources from our proposal in [research/README.md](research/README.md). Every disease number must be marked SOURCED, DERIVED or ASSUMPTION, with an explanation.

## Required core and optional work

The core is a working interactive simulation for three diseases, reviewed charts, and simple machine learning tested on unseen simulated runs. Historical NYC COVID 19 comparison and gradient boosting are optional. We will not sacrifice a working demo to add them.
