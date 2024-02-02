# Assignment 7: Profile Analysis

Create a new Word document in your assignments folder called ***assignment_7.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

## Part 1 - Latent Profile Analysis

The first part of this assignment is for you to use the data uploaded to Canvas to identify the number and composition of the profiles reflected in the following five variable components of entrepreneurial orientation: Autonomy `auto`, Competitive Aggressiveness `compagg`, Innovativeness `innov`, Proactiveness `proact`, and Risk Taking `riskt`. If you'd like to see where this construct comes from: [here](https://journals.aom.org/doi/abs/10.5465/amr.1996.9602161568)

If using Stata, the documentation for running latent profile analysis models is [here](https://www.stata.com/manuals/semexample52g.pdf). You will also want to take a look at the documentation for latent *class* analysis [here](https://www.stata.com/manuals/semexample50g.pdf), but only for the postestimation commands for identifying the latent class marginal means and probabilities (these commands are the same whethr you are doing LPA or LCA). Here is a resources [.do file](./do_files/profiles_resources.do) to get you started.

For your LPA, you should compare the model fit statistics for everything from 2 latent classes through 10 latent classes.

### Latent Profile Analysis Questions to Answer

1. What is the best fitting model? How did you determine this?
2. What percentage of the sample does each profile comprise?
3. What are the composition of the profiles? That is, what are the mean values of each of the five variables for each profile?
4. Does profile membership significantly influence firm performance as reflected in Return on Assets `roa`? How so?

## Part 2 - Cluster Analysis

Using the same data, run a cluster analysis to identify the number and composition of the clusters reflected in the same five variables.

If using Stata, the documentation for running cluster analysis models is [here](https://www.stata.com/manuals13/mvcluster.pdf).

Follow the Ketchen and Shook (1996) best practice guidelines for using a hierarchical clustering algorithm to identify the number of clusters and then k-means clustering to assign cases to clusters. To do this you will want to save the results of your hierarchical clustering and then use those results as the starting values for your k-means clustering.

Two notes:
* Stata does not include a built-in way to calculate a CCC; however, it does generate dendrograms, and the Duda-Hart and Calinski-Harabasz indices are strong alternatives to CCC. These are options in `cluster stop` in Stata. Use those instead to triangulate the number of clusters to use.
* Do not worry about multicollinearity in this assignment - the data are highly correlated, and moreso than would be expected in real data. However, these data were generated to be clearly interpretable and comparable between the two parts of the assignment, not to minimize multicollinearity. If you would like to address it, I suggest using mahalanobis distance as the distance measure in your cluster analysis rather than the orthogonal factor rotation method as this will preserve the interpretability/comparability of the results to part 1.

Mahalanobis distances are one of the best distance measures for cluster analysis. Unfortunately, as far as I know, Stata does not support Mahalanobis distance in its cluster analysis commands out of the box. However, the `mahapick` package does. You can install this package by typing `ssc install mahapick` in the Stata command window. Then, you can use the `mahascores` command to generate a Mahalanobis distance matrix, which you can then use as the distance matrix in your cluster analysis. For example:

* `ssc install mahapick`
* `mahascores <<your variables>>, genmat(zdistance) unsq compute_invcovarmat` creates the Mahalanobis distance matrix and saves it to a variable called zdistance
* You then use [clustermat](https://www.stata.com/manuals13/mvclustermat.pdf) to run the cluster analysis using the Mahalanobis distance matrix instead of `cluster`

You do not need to use Mahalanobis distances for this assignment, but if you think you might use this technique in the future, I recommend doing so.

### Cluster Analysis Questions to Answer

1. Report the same information as in Part 1, but for clusters instead of profiles. However, make sure to include the distinctive key decisions you made and why you made them (e.g., in cluster analysis you have to choose a linkage method, you don't in LPA).
2. Produce a dendrogram and the Duda-Hart and Calinski-Harabasz stopping indices of the hierarchical clustering results. How many clusters do they suggest and what criteria did you apply to make this assessment? Use the `cutnumber` option for the dendogram if using Stata to make the dendrogram easier to read.
3. How do the results from the cluster analyses compare to your latent profile analysis results?

### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)
