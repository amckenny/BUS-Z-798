# Assignment 4: Multilevel Methods/Analysis

Create a new Word document in your assignments folder called ***assignment_4.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

## Part 1 - Multilevel Data

The first part of this assignment is for you to manually simulate data with different multilevel characteristics. This will help you to crystallize what it means for there to be variance associated with multiple levels in your data.

Here is your scenario: You are collecting data on some construct at the within-person level in the field of your interest (e.g., entrepreneurship: entrepreneurial passion, organizational behavior: job satisfaction, etc.). You are collecting data from 10 organizations, each of which has 10 people, each of whom you survey at 5 points in time. You are interested in the extent to which the variable of interest varies within and between people and organizations. You may use any scale you'd like for your data (Likert, continuous, etc).

You will be simulating three datasets:
1. **Construct 1** - In this variable, there should be minimal variance within-person (i.e., the variable is stable over time, but not a constant), but there is substantial variance between people and organizations.
2. **Construct 2** - In this variable, there should be minimal variance within-person (i.e., the variable is stable over time, but not a constant) and between people within an organization, but there is substantial variance between organizations.
3. **Construct 3** - In this variable there should be substantial variance within-person (i.e., the variable is not stable over time), between people, and and between organizations. This variable should exhibit more within-person variance than between-person variance and between-organization variance.

### Multilevel Data Questions to Answer

1. How did you go about simulating the data to ensure that the data had the characteristics described above?
2. Calculate and interpret the necessary aggregation statistics. In Stata, you might find these pages helpful for [ICC](https://www.stata.com/manuals/ricc.pdf) and [rwg](https://ideas.repec.org/c/boc/bocode/s458422.html) statistics. Explain why these are necessary, and what they are telling you.
3. Calculate a null model for each construct. Identify the variance components and compute what percentage of the variance is at each level. See [Examples 1 and 4 in this Stata documentation](https://www.stata.com/manuals/memixed.pdf).
4. If these were real data and the variance you found was reflective of the construct's theorizing, what would this mean for the constructs you are studying with respect to level of measurement/aggregation?

## Part 2 - Multilevel Analysis

Obtain the multilevel exercise datafile from Canvas. You will be testing whether conscientiousness (an individual-level personality trait) relates positively to job engagement (an individual-level motivational state), and whether transformational leadership (a group-level leadership variable) moderates the relationship between conscientiousness and engagement. The individuals are nested within supervisors as noted by their individual and team IDs.

1. Calculate the necessary aggregation statistics (ICC1, ICC2, rwg using a uniform (4) and skewed distribution (2.9)). Note, the IRA package will not work for calculating rwg on these data, you will need to use the formulas in the LeBreton & Senter (2008, p.818) article.
    * S2x is the within-group variance on a particular construct. This can be calculated in Stata using the following code:
        * `collapse (sd) sd_VARNAME = VARNAME, by(teamid)` - creates team-level standard deviation variable
        * `gen var_trans = sd_VARNAME * sd_VARNAME` - creates team-level variance variable
    * Then, you can use the formula in LeBreton & Senter (2008, p.818) to compute the rwg for each team. Reset any values less than 0 to zero (you can do this manually, or write a short command to do this – I leave it up to you to figure out how... hint: `recode`)
2. Using uncentered data, estimate:
    * a null model (i.e., no predictors) for engagement
    * a random coefficient model with conscientiousness predicting engagement
    * an intercepts as outcomes model with conscientiousness predicting engagement and transformational leadership predicting engagement
    * a slopes as outcomes model with conscientiousness predicting engagement, transformational leadership predicting engagement, and the interaction between conscientiousness and transformational leadership predicting engagement
3. Using group mean centering *with means in level-2* (See Hoffman & Gavin, 1998), estimate the same models as in #2
    * Note: you will need to calculate the group means and centered variables yourself. You can do this using the following code:
        * `egen VARNAME_group = mean(VARNAME), by(teamid)` - calculates the group mean for each team
        * `gen VARNAME_grpcentered = VARNAME - VARNAME_group` - calculates the centered variable


### Multilevel Analysis Questions to Answer

1. Report and provide an interpretation of the results of your aggregation statistics. Explain why these are necessary, and why you computed them on the variable(s) you chose to compute them on.
2. Report the results of your two series of models (ordered simple to complex). Be sure to report the key parameter estimates associated with each model.
3. Write a short description of the results, telling me what the analyses revealed about the data. This should look like a (very short) version of a journal article's results section, half a page or so.


### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)
