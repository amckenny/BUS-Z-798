# Assignment 2: Instrument Design and Exploratory Factor Analysis

Create a new Word document in your assignments folder called ***assignment_2.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

## Part 1 - EFA Analysis

The Conway and Huffcutt article reviewed EFA practices, and provide some best-practices for conducting an EFA, and Hayton et al. describe how to conduct parallel analysis to make decisions regarding factor retention. You will be using these techniques to conduct an EFA on a new scale you've developed, The Z798 Job Attitudes Scale (data available in Canvas). In theory, the scale should be measuring three different attitudes (intent to quit, job engagement, and job satisfaction), but you will be conducting an EFA to:
1. assess item performance, and
2. determine the number of factors that emerge from the scale.

To conduct exploratory factor analysis in Stata, see the following site: https://stats.idre.ucla.edu/stata/output/factor-analysis/.

Follow their steps; however, make the following changes to their syntax:
* do not specify an *a priori* number of factors,
* do not include the `horst` command, and
* plot the Eigenvalues after the first factor analysis on the unrotated solution (command: `screeplot`) and again after you've dropped poorly performing items.

Finally, run a principal components analysis (PCA) using the command line: `pca [INSERT VAR NAMES HERE]`. Use the unrotated solution to make decisions about factor retention, and use the rotated solution to make decisions about individual item retention/performance.

### EFA Analysis Questions to Answer

1. Which items would you recommend dropping from your scale? Re-run the initial factor analyses with the dropped items excluded; how did the absence of those items changed the results? Provide any required evidence from the analyses to support this.
2. How many factors would you recommend retaining? Provide any required evidence from the analyses to support this.
3. How were the results different (or similar) using orthogonal and non-orthogonal rotation? What does this tell you about your data?
4. How did the results differ when using factor analysis vs. PCA? Why?

## Part 2 - Parallel Analysis
Conduct parallel analyses. To do this, type `findit fapara` in the Stata command window; then, click the blue install button in the window that pops up. Rerun the initial (unrotated) factor analysis, then type `fapara, reps(25)`.

### Parallel Analysis Questions to Answer

1. What do the results of the parallel analysis tell you?

### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)