//LPA and cluster analysis resources:

use https://www.stata-press.com/data/r18/gsem_lca2, clear




// Basics---------------------------
	////Creating a standardized variable
	egen z_glucose = std(glucose) 

	////Calculating means for groups
	mean glucose insulin sspg, over(cclass)



//Cluster analysis from variables ------------------

	////Hierarchical using Wards
	cluster wardslinkage glucose insulin sspg, measure(L2Squared) name(cluster_sol)

	////Generating stopping statistics
	cluster stop cluster_sol, groups(1/3) rule(duda)

	////Generating a dendrogram
	cluster tree, cutnumber(20)

	////Generating groups from hierarchical cluster analysis
	cluster gen HierClustGroups = groups(2), name(cluster_sol)

	////K-means clustering without starting values
	cluster kmeans glucose insulin sspg, k(2) measure(L2squared) name(non_hier_clusters)

	////K-means clustering with starting values
	cluster kmeans glucose insulin sspg, k(2) measure(L2squared) name(non_hier_clusters2) start(group(HierClustGroups))



//Cluster analysis from matrices ------------------

	////Generating mahalanobis distances
	capture ssc install mahapick
	mahascores glucose insulin sspg, genmat(maha_dists) unsq compute_invcovarmat

	////Same general approach as above, slightly different syntax
	clustermat wardslinkage maha_dists, add name(clustermat_sol)
	clustermat stop clustermat_sol, groups(1/3) rule(duda) variables(glucose insulin sspg)
	cluster tree, cutnumber(20)
	clustermat gen MatHierClustGroups = groups(3), name(clustermat_sol)
	//////everything beyond this stays the same




//Latent profile analysis--------------------------

	//// Run LPA analysis
	gsem (glucose insulin sspg <- _cons), method(ml) vce(robust) nocapslatent lclass(C 2) startvalues(randomid, draws(50) seed(15)) nolog nodvheader
	estimates store model_2
	gsem (glucose insulin sspg <- _cons), method(ml) vce(robust) nocapslatent lclass(C 3) startvalues(randomid, draws(50) seed(15)) nolog nodvheader
	estimates store model_3
	gsem (glucose insulin sspg <- _cons), method(ml) vce(robust) nocapslatent lclass(C 4) startvalues(randomid, draws(50) seed(15)) nolog nodvheader
	estimates store model_4
	gsem (glucose insulin sspg <- _cons), method(ml) vce(robust) nocapslatent lclass(C 5) startvalues(randomid, draws(50) seed(15)) nolog nodvheader
	estimates store model_5
	
	//// View AIC/BIC fit statistics
	estimates stats model_*
	
	//// Calculate Entropy (for only the most recent model run)
	ssc install lcaentropy
	lcaentropy

	//// Display the estimates for a saved model again, but don't reload them for further use
	estimates replay model_5

	//// Reload the estimates for a saved model so you can continue working with it
	estimates restore model_5
	
	//// View latent class marginal probabilities and means
	estat lcprob
	estat lcmean

	//// Assign observations to predicted classes
	predict cpr*, classposteriorpr
	egen max = rowmax(cpr*)
	generate predclass = 1 if cpr1==max
	forvalues i = 2/5 {
		replace predclass = `i' if cpr`i'==max
	}
	
	




