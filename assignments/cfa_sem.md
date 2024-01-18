# Assignment 3: Confirmatory Factor Analysis and SEM

Create a new Word document in your assignments folder called ***assignment_3.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

## Part 1 - CFA Analysis

Review this website: [https://www.stata.com/features/overview/structural-equation-modeling/](https://www.stata.com/features/overview/structural-equation-modeling/) **

**A few notes:
1. STATA automatically reads any variable entered into the model syntax with the first letter capitalized as latent; to remove this, enter "`, nocapslatent`" after your model syntax.
2. To see the fit indices, enter the following command after you run the CFA: `estat gof stats(all)`.
3. To see modification indices, enter the following command after you run the CFA: `estat mindices`.

### CFA Analysis Questions to Answer

1. What are the distinctions between exploratory and confirmatory factor analysis? Pay particular attention to:
    * the correspondence between the confirmatory measurement model and the notion of true score and error variance in classical test theory,
    * the meaning and importance of unidimensional measurement, and
    * the concept of a two-step modeling approach.
2. There are various models relating constructs to measures and criteria for choosing among those models. What are the implications of these models for developing and evaluating measures in your area?
3. Using last week's EFA dataset loaded to canvas, conduct 2 CFA analyses using the `sem` command in STATA (see the [website above](https://www.stata.com/features/overview/structural-equation-modeling/)). Both models should be basic with 2 latent factors (engagement and job satisfaction). However, the difference will be the items used to measure the latent factors. Model 1 should use Y23, Y28, and Y36 for engagement and Y10, Y11, and Y12 for job satisfaction. Model 2 should use Y28, Y31, and Y32 for engagement and Y11, Y12, and Y13 for job satisfaction.
    * Report the chi-square, degrees of freedom, RMSEA, CFI, and SRMR for each and interpret the findings.
    * Which model fit better?
    * Did the indicators appropriately load onto their respective factors?
4. The third model you run should be on the same items as model 2, but instead of running a 2 factor CFA with engagement and job satisfaction, I want you to have all the items load onto a single factor.
    * Report and interpret the fit statistics.
    * Are the items appropriate for a single factor?

## Part 2 - SEM Analysis
Review this website: [https://stats.idre.ucla.edu/stata/faq/how-can-i-do-mediation-analysis-with-the-sem-command/](https://stats.idre.ucla.edu/stata/faq/how-can-i-do-mediation-analysis-with-the-sem-command/). Search the page for “`bias-corrected`” and follow those instructions to compute bias-corrected confidence intervals (CIs). Run this using 1,000 replications. Don’t worry about computing the proportion or ratio of mediated effects, just estimate the indirect effects and related CIs.

### SEM Analysis Questions to Answer

1. Using the SEM dataset uploaded to Canvas, run two SEM models with at least 2 exogenous latent variables, at least one latent mediator variable, and at least one latent outcome variable (all of your choosing).
    * Report the chi-square and accompanying fit statistics for the fully mediated Structural model, and a partially mediated Structural model.
    * Regarding the 2 SEMs, which model would you retain and why?
2. Using the same dataset and variables as in question 1, test the hypothesis that the proposed mediator(s) mediate(s) the relation between the independent variables and the outcome variable. To test this hypothesis, use the steps described in the link above to compute bias-corrected 95% confidence intervals around the indirect effect, in addition to the relevant model statistics. Report the results of the relevant analyses you conducted to arrive at your conclusion.

### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)
