# Manual agent review packet

> Gold fields below are shown only for post-execution human audit. Mechanical/AI hints are not official labels.

## dev/hybrid · q01

- **Type:** answerable
- **Question:** In Section 2, what two essential components define Double/Debiased Machine Learning?
- **Gold / expected behavior (post-run audit only):** Neyman orthogonality and cross-fitting.
- **Agent status:** `answered`
- **Agent answer:** Section 2 identifies the two essential components of Double/Debiased Machine Learning as **Neyman orthogonality** and **cross-fitting**. [19cea224507fdb1853fa43fc456ece5c | page 9]
- **Citation IDs:** `19cea224507fdb1853fa43fc456ece5c`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1066, output=96, total=1162
- **Latency / estimated cost:** 5046.456 ms / $0.0001546
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:1`

### Cited passages

**`19cea224507fdb1853fa43fc456ece5c` · rank 3 · page 9 · https://arxiv.org/pdf/2504.08324v2**

2 Key Ingredients of DML

This section describes the two essential components that define DML: Neyman orthogonality and cross-fitting. Together, they help control the sensitivity of the target estimator to nuisance estimation, which can substantially improve both the reliability of point estimates and the quality of conventional asymptotic approximations. By alleviating this sensitivity, DML further opens the door for researchers to use a wide range of flexible estimators, including many modern machine learners, for estimating nuisance parameters.

### Final context

**Rank 1 · `a4c0e1caa19672c2a733be154e7e303b` · page 1 · https://arxiv.org/pdf/2504.08324v2**

An Introduction to Double/Debiased Machine Learning Achim Ahrens Victor Chernozhukov Christian Hansen Damian Kozbur Mark Schaffer Thomas Wiemann ∗ February 16, 2026 This paper provides an introduction to Double/Debiased Machine Learning (DML). DML is a general approach to performing inference about a target parameter in the presence of nuisance functions: objects that are needed to identify the target parameter but are not of primary interest. Nuisance functions arise naturally in many settings, such as when controlling for confounding variables or leveraging instruments. The paper describes two biases that arise from nuisance function estimation and explains how DML alleviates these biases.

**Rank 2 · `3ffc2c62e978bf0784ac4705f6eea4b6` · page 4 · https://arxiv.org/pdf/2504.08324v2**

As such, mitigating these biases is the focus of a large and rapidly growing literature in statistics and econometrics that builds from classic ideas in semiparametric and nonparametric estimation. One method that provides a solution in a wide variety of empirical settings, and that is the topic of this review, is double/debiased machine learning (henceforth DML; Chernozhukov et al., 2018). DML provides a blueprint for alleviating both regularization and overfitting bias. At its core, DML combines two classical ideas from the rich literature on semiparametric inference—using Neyman orthogonal scores1 to alleviate regularization bias and using cross-fitting to alleviate overfitting bias—in a common methodological framework.

**Rank 3 · `19cea224507fdb1853fa43fc456ece5c` · page 9 · https://arxiv.org/pdf/2504.08324v2**

2 Key Ingredients of DML

This section describes the two essential components that define DML: Neyman orthogonality and cross-fitting. Together, they help control the sensitivity of the target estimator to nuisance estimation, which can substantially improve both the reliability of point estimates and the quality of conventional asymptotic approximations. By alleviating this sensitivity, DML further opens the door for researchers to use a wide range of flexible estimators, including many modern machine learners, for estimating nuisance parameters.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q02

- **Type:** answerable
- **Question:** Within the semiparametric framework, what kind of object is the target parameter theta-zero?
- **Gold / expected behavior (post-run audit only):** It is a low-dimensional parameter, such as an average treatment effect or a fixed vector of regression coefficients.
- **Agent status:** `answered`
- **Agent answer:** The target parameter \(\theta_0\) is a low-dimensional object of interest, such as an average treatment effect or a fixed vector of regression coefficients. It is often defined as the solution to a moment condition, \(E[m(W;\theta_0,\eta_0)]=0\). [3fc918bfa4346bbf4d5a72f77e0f146a | page 9] [1bb190e771af1499aa40fa479e948ffb | page 3]
- **Citation IDs:** `1bb190e771af1499aa40fa479e948ffb`, `3fc918bfa4346bbf4d5a72f77e0f146a`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1266, output=157, total=1423
- **Latency / estimated cost:** 5755.721 ms / $0.0002051
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:2`

### Cited passages

**`1bb190e771af1499aa40fa479e948ffb` · rank 3 · page 3 · https://arxiv.org/pdf/2504.08324v2**

function rather than committing to a low-dimensional functional form. In contrast to the low-dimensional linear case, whereg0(X) =X′β0 reduces to estimating a small set of coefficients, estimation ofg0(·) must then also accommodate rich nonlinear variation. This regression setup illustrates a broader template common in empirical research, in which the target parameterθ0 is defined as the solution to a moment condition: θ0 : E[m(W ;θ0,η 0)] = 0. (1) Here,m is a score (or moment) function andW again denotes observed random variables. The parameterη0 denotes a nuisance object, which is not of direct interest but is used to defineθ0. η0 is often high-dimensional. For example,η0 will represent a vector of conditional expectation functions in many interesting cases. Thissemi-parametric structure encompasses the regression example above, where the target parameter is the coefficient on D.

**`3fc918bfa4346bbf4d5a72f77e0f146a` · rank 2 · page 9 · https://arxiv.org/pdf/2504.08324v2**

2.1 A Semiparametric Framework for DML

We frame our discussion of DML within a relatively general semiparametric framework. There are two key elements of the framework. First, we have a target parameter of interest, θ0, which is low-dimensional; e.g.,θ0 may be an average treatment effect or a fixed vector of regression coefficients. Second, we have a nuisance parameterη0 which may be high-dimensional and potentially complex. In many examples, η0 is a vector of conditional expectation functions, such as outcome regressions and propensity scores, though it may take other forms. Throughout this review, we focus on the case where we observe ani.i.d. sample{Wi : i = 1,...,n } from a random vector W. Each Wi collects the variables relevant for individual i. For example, Wi might include an outcomeYi, a treatment variableDi, a vector of controlsXi, and excluded instruments Zi.

### Final context

**Rank 1 · `0c0a34021ebe7fd8dd477f93c06ff82e` · page 10 · https://arxiv.org/pdf/2504.08324v2**

asymptotically normal inference forθ0 would be achievable ifη0 were known.5 This semiparametric framework captures a large range of common parameters of interest in empirical research. We discuss four illustrative examples below. Example 1. Linear Regression Coefficient.Consider linear regression with a single variable of interestD and ap× 1 vector of controlsX that may include a constant: Y =θ0D +X′β0 +ε, E[Dε] = 0, E[Xε] = 0p (3) where 0p denotes ap× 1 vector of zeros. The coefficientθ0 onD is the target parameter. The vector of coefficientsβ0 on controlsX is the nuisance parameter. The traditional textbook approach is to estimate bothθ0 and β0 by applying OLS to equation (3). This problem can be framed as a semiparametric estimation task by explicitly targetingθ0 separately from the nuisance parameters.

**Rank 2 · `3fc918bfa4346bbf4d5a72f77e0f146a` · page 9 · https://arxiv.org/pdf/2504.08324v2**

2.1 A Semiparametric Framework for DML

We frame our discussion of DML within a relatively general semiparametric framework. There are two key elements of the framework. First, we have a target parameter of interest, θ0, which is low-dimensional; e.g.,θ0 may be an average treatment effect or a fixed vector of regression coefficients. Second, we have a nuisance parameterη0 which may be high-dimensional and potentially complex. In many examples, η0 is a vector of conditional expectation functions, such as outcome regressions and propensity scores, though it may take other forms. Throughout this review, we focus on the case where we observe ani.i.d. sample{Wi : i = 1,...,n } from a random vector W. Each Wi collects the variables relevant for individual i. For example, Wi might include an outcomeYi, a treatment variableDi, a vector of controlsXi, and excluded instruments Zi.

**Rank 3 · `1bb190e771af1499aa40fa479e948ffb` · page 3 · https://arxiv.org/pdf/2504.08324v2**

function rather than committing to a low-dimensional functional form. In contrast to the low-dimensional linear case, whereg0(X) =X′β0 reduces to estimating a small set of coefficients, estimation ofg0(·) must then also accommodate rich nonlinear variation. This regression setup illustrates a broader template common in empirical research, in which the target parameterθ0 is defined as the solution to a moment condition: θ0 : E[m(W ;θ0,η 0)] = 0. (1) Here,m is a score (or moment) function andW again denotes observed random variables. The parameterη0 denotes a nuisance object, which is not of direct interest but is used to defineθ0. η0 is often high-dimensional. For example,η0 will represent a vector of conditional expectation functions in many interesting cases. Thissemi-parametric structure encompasses the regression example above, where the target parameter is the coefficient on D.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q03

- **Type:** answerable
- **Question:** According to Section 2.3.1, how does Neyman orthogonality change sensitivity to small nuisance-parameter errors?
- **Gold / expected behavior (post-run audit only):** Small nuisance perturbations do not create first-order changes in the moment function, reducing regularization bias.
- **Agent status:** `answered`
- **Agent answer:** Neyman orthogonality makes the estimator less sensitive to nuisance-parameter estimation errors: small deviations from the true nuisance value do not change the moment function to first order. [90c3b5213c632d1e7a0b1b069959fc95 | page 16]
- **Citation IDs:** `90c3b5213c632d1e7a0b1b069959fc95`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1474, output=112, total=1586
- **Latency / estimated cost:** 4889.080 ms / $0.0002034
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:3`

### Cited passages

**`90c3b5213c632d1e7a0b1b069959fc95` · rank 1 · page 16 · https://arxiv.org/pdf/2504.08324v2**

2.3.1 Neyman Orthogonality

The chief difficulty in using the plug-in estimatorˆθ is its dependence on the nuisance parameter estimatorˆη. Neyman orthogonalityis a local robustness property of the score function in (2) that decreases sensitivity ofˆθ to errors in estimatingη0. Formally, in addition to identifying the target parameter by satisfying (2), aNeyman orthogonal scorealso satisfies ∂ ∂λ { E [m(W ;θ0,η 0 +λ(η−η0))] }⏐⏐⏐ λ=0 = 0, ∀η∈T , (15) whereη denotes a candidate value for the nuisance parameter andλ indexes the size of a localdeviationawayfromthetrue η0. Intuitively, (15)requiresthat, whenwemakeasmall move away fromη0 in any directionη−η0, the moment condition remains unchanged.10 In other words, small perturbations of the nuisance parameter away from the true value do not create first-order changes in the moment function.

### Final context

**Rank 1 · `90c3b5213c632d1e7a0b1b069959fc95` · page 16 · https://arxiv.org/pdf/2504.08324v2**

2.3.1 Neyman Orthogonality

The chief difficulty in using the plug-in estimatorˆθ is its dependence on the nuisance parameter estimatorˆη. Neyman orthogonalityis a local robustness property of the score function in (2) that decreases sensitivity ofˆθ to errors in estimatingη0. Formally, in addition to identifying the target parameter by satisfying (2), aNeyman orthogonal scorealso satisfies ∂ ∂λ { E [m(W ;θ0,η 0 +λ(η−η0))] }⏐⏐⏐ λ=0 = 0, ∀η∈T , (15) whereη denotes a candidate value for the nuisance parameter andλ indexes the size of a localdeviationawayfromthetrue η0. Intuitively, (15)requiresthat, whenwemakeasmall move away fromη0 in any directionη−η0, the moment condition remains unchanged.10 In other words, small perturbations of the nuisance parameter away from the true value do not create first-order changes in the moment function.

**Rank 2 · `5c8a30f7f67fbfebaba359ead1992435` · page 43 · https://arxiv.org/pdf/2504.08324v2**

A Verification of Neyman Orthogonality

In this appendix, we verify Neyman orthogonality of the linear regression, linear IV, and AIPW scores presented in Examples 1, 3, and 4. We also verify that the IPW score from Example 4 does not satisfy Neyman orthogonality. Example 1 (continued). Neyman Orthogonality of the Linear Regression Score. In the linear regression score (5), the nuisance parametersηY andηD are vectors. The second condition in (15) then reduces to ∂ ∂ηY E[mLM(W ;θ0,η )] ⏐⏐⏐ η=η0 =−E[X(D−X′ηD,0)] = 0p ∂ ∂ηD E[mLM(W ;θ0,η )] ⏐⏐⏐ η=η0 = 2θ0E[X(D−X′ηD,0)]− E[X(Y−X′ηY,0)] = 0p by applying (4). □ Example 3 (continued). Neyman Orthogonality of the Linear IV Score.For the linear IV score (9), the nuisance function isη(Z) with true valueη0(Z) = E[D|Z].

**Rank 3 · `326b23a87a2f123ef0494842d11f541e` · page 46 · https://arxiv.org/pdf/2504.08324v2**

(γ(h)0 ,α (h)0 )Hh=1. To verify that the score in (28) indeed satisfies Neyman orthogonality, note first that the orthogonality condition (27) implies thatψ and m identify the same target parameter. Then, by the chain rule ∂ ∂λ { E [ψ(W ; θ0,η 0 +λ∆η)] }⏐⏐⏐ λ=0 = H∑ h=1 E [( mh(W ;θ0,γ 0)−α(h)0 (B(h))) ∆γ(h)(B(h))] + H∑ h=1 E [ ∆α(h)(B(h))(A(h)−γ(h)0 (B(h)))] = 0, where the final equality follows from (26) and the law of iterated expectations. Mirroring the familiar approach in multiple linear regression (Example 1) or partially linear regression (Example 2), the score (28) is thus constructed to “partial out” the first-order impact of estimating the nuisance functions: for eachh, small errors in eitherγ(h)0 (B(h)) or α(h)0 (B(h)) can be offset by the other, making estimation more robust.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q04

- **Type:** answerable
- **Question:** In Section 2.3.2, what is cross-fitting intended to reduce?
- **Gold / expected behavior (post-run audit only):** It reduces dependence between first-step nuisance-estimation error and the data used to estimate the target parameter.
- **Agent status:** `answered`
- **Agent answer:** Cross-fitting is intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. [46b3d3c66f0f888a2ab9bfced5cddb51 | page 20]
- **Citation IDs:** `46b3d3c66f0f888a2ab9bfced5cddb51`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1259, output=94, total=1353
- **Latency / estimated cost:** 3915.890 ms / $0.0001729
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:4`

### Cited passages

**`46b3d3c66f0f888a2ab9bfced5cddb51` · rank 1 · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

### Final context

**Rank 1 · `46b3d3c66f0f888a2ab9bfced5cddb51` · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

**Rank 2 · `1f08942ad4e9a13de6702d8342e6f305` · page 37 · https://arxiv.org/pdf/2504.08324v2**

We useK = 3 cross-fitting folds, implemented by randomlyassigningrecruiterstofolds, andreportmedianaggregatedestimatesobtainedusing S = 5 cross-fittingrepetitions. The number of observations isN = 258, 352. The diagnostics reported are the cross-fittedR2, the CVCp-value, and the short-stacking weights; each averaged across cross-fitting repetitions. We consider the following nuisance estimators: OLS; CV-lasso (lasso with tuning parameter selected by cross-validation); CV-ridge (ridge with tuning parameter selected by cross-validation); three types of random forest labeled RF 1 (600 trees), RF 2 (600 trees, minimum terminal node size of 500) and RF 3 (600 trees, minimum terminal node size of 2000); three types ofXGBoost labeled XGB 1 (800 trees, early stopping after 10 rounds), XGB 2 (800 trees, minimum node size of 500) and XGB 3 (800 trees, minimum node size of 2000).

**Rank 3 · `acdd8fc9e3a5cd0ea3fab7d797f387e0` · page 15 · https://arxiv.org/pdf/2504.08324v2**

Our usage emphasizes that overfitting in nuisance estimation can lead to bias in target parameter estimation, because it inflates the dependence between nuisance estimation error and the data. The second key ingredient of DML—cross-fitting, also discussed in Section 2.3— addresses overfitting bias by using sample splitting to ensure (approximate) independence between the estimation error in the nuisance function and the observations used in the sample moment condition. This independence implies that the product in the numerator of (⋆) is mean zero whenever either term is mean zero. The two main ingredients of DML, discussed in Section 2.3, are meant to alleviate the first-order impact of nuisance estimation. Estimation of nuisance parameters also generally affects the target parameter through the “higher order terms” in (14).

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q05

- **Type:** answerable
- **Question:** Why does rotating folds in cross-fitting avoid the efficiency loss of a simple one-time sample split?
- **Gold / expected behavior (post-run audit only):** Rotation lets every observation contribute to nuisance estimation and target estimation across folds.
- **Agent status:** `answered`
- **Agent answer:** A one-time split leaves some observations out of nuisance estimation and others out of target-parameter estimation, so each step uses only a subset of the data. Cross-fitting rotates the folds: each fold is used in turn to estimate the target while the other folds estimate the nuisance parameters. Thus, across rotations, all observations contribute to both steps, avoiding the efficiency loss of using only a subset for either task. [a1b3a5c7ca75cea978cdfddf08d10a18 | page 20] [46b3d3c66f0f888a2ab9bfced5cddb51 | page 20]
- **Citation IDs:** `46b3d3c66f0f888a2ab9bfced5cddb51`, `a1b3a5c7ca75cea978cdfddf08d10a18`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1152, output=192, total=1344
- **Latency / estimated cost:** 3688.548 ms / $0.0002112
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:5`

### Cited passages

**`46b3d3c66f0f888a2ab9bfced5cddb51` · rank 3 · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

**`a1b3a5c7ca75cea978cdfddf08d10a18` · rank 1 · page 20 · https://arxiv.org/pdf/2504.08324v2**

Cross-fitting restores asymptotic efficiency by rotating which folds are used for each task, so all observations contribute to both steps. The cross-fit version of the plug-in estimator with a generic score defined in (13) is ˆθ×-fit : 1n K∑k=1∑i∈Ikm(Wi;ˆθ×-fit,ˆη−k) = 0. (17) Here,{Ik}Kk=1 is a random partition of the sample of units{1,...,n } intoK subsamples of approximately equal size, and ˆη−k denotes a first-step nuisance parameter estimate constructed using only observationsexcluding those in the subsampleIk. Because ˆη−k uses only observationsnot in subsamplek, the estimation error inˆη−k is independent of observations in subsamplek, which alleviates overfitting bias.

### Final context

**Rank 1 · `a1b3a5c7ca75cea978cdfddf08d10a18` · page 20 · https://arxiv.org/pdf/2504.08324v2**

Cross-fitting restores asymptotic efficiency by rotating which folds are used for each task, so all observations contribute to both steps. The cross-fit version of the plug-in estimator with a generic score defined in (13) is ˆθ×-fit : 1n K∑k=1∑i∈Ikm(Wi;ˆθ×-fit,ˆη−k) = 0. (17) Here,{Ik}Kk=1 is a random partition of the sample of units{1,...,n } intoK subsamples of approximately equal size, and ˆη−k denotes a first-step nuisance parameter estimate constructed using only observationsexcluding those in the subsampleIk. Because ˆη−k uses only observationsnot in subsamplek, the estimation error inˆη−k is independent of observations in subsamplek, which alleviates overfitting bias.

**Rank 2 · `f126a9f8370e3d1fc0b6e69b1117fce3` · page 20 · https://arxiv.org/pdf/2504.08324v2**

By rotating (“crossing”) samplesfortheestimationofnuisanceparametersandtheestimationoftargetparameters, cross-fitting asymptotically avoids losing efficiency relative to the hypothetical full-sample estimator that makes use of the true values of the nuisance parameters. As a byproduct that comes at no additional computational cost, cross-fitting produces 20

**Rank 3 · `46b3d3c66f0f888a2ab9bfced5cddb51` · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q06

- **Type:** answerable
- **Question:** What two ingredients are combined by the DML estimator defined in the estimation and inference section?
- **Gold / expected behavior (post-run audit only):** Neyman orthogonal scores and cross-fitting.
- **Agent status:** `answered`
- **Agent answer:** The DML estimator combines Neyman orthogonal scores with cross-fitting. [0394cbc044adaf0319490b78f7cfa5e6 | page 22]
- **Citation IDs:** `0394cbc044adaf0319490b78f7cfa5e6`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1082, output=82, total=1164
- **Latency / estimated cost:** 4209.418 ms / $0.0001492
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:6`

### Cited passages

**`0394cbc044adaf0319490b78f7cfa5e6` · rank 2 · page 22 · https://arxiv.org/pdf/2504.08324v2**

In this section, we define the DML estimator, present an implementation algorithm, and summarize its asymptotic properties. We remain in the general semiparametric setting of Section 2. That is, our focus is estimation and inference for a low-dimensional target parameter θ0, which is defined by moment conditions (2) and depends on an unknown (potentially high-dimensional) nuisance parameterη0. Within this general setting, a DML estimator is a plug-in estimator that combines both Neyman orthogonal scores and cross-fitting. The DML estimator ofθ0 is then ˆθDML : 1n K∑k=1∑i∈Ikm(Wi;ˆθDML,ˆη−k) = 0, (18) where m is a Neyman orthogonal score (i.e., a score that satisfies (2) and (15)),{Ik}Kk=1 is a random partition of the sample of individuals{1,...,n } into K subsamples of approximately equal size, and{ˆη−k}Kk=1 are cross-fitted nuisance parameter estimators. Chernozhukov et al.

### Final context

**Rank 1 · `19cea224507fdb1853fa43fc456ece5c` · page 9 · https://arxiv.org/pdf/2504.08324v2**

2 Key Ingredients of DML

This section describes the two essential components that define DML: Neyman orthogonality and cross-fitting. Together, they help control the sensitivity of the target estimator to nuisance estimation, which can substantially improve both the reliability of point estimates and the quality of conventional asymptotic approximations. By alleviating this sensitivity, DML further opens the door for researchers to use a wide range of flexible estimators, including many modern machine learners, for estimating nuisance parameters.

**Rank 2 · `0394cbc044adaf0319490b78f7cfa5e6` · page 22 · https://arxiv.org/pdf/2504.08324v2**

In this section, we define the DML estimator, present an implementation algorithm, and summarize its asymptotic properties. We remain in the general semiparametric setting of Section 2. That is, our focus is estimation and inference for a low-dimensional target parameter θ0, which is defined by moment conditions (2) and depends on an unknown (potentially high-dimensional) nuisance parameterη0. Within this general setting, a DML estimator is a plug-in estimator that combines both Neyman orthogonal scores and cross-fitting. The DML estimator ofθ0 is then ˆθDML : 1n K∑k=1∑i∈Ikm(Wi;ˆθDML,ˆη−k) = 0, (18) where m is a Neyman orthogonal score (i.e., a score that satisfies (2) and (15)),{Ik}Kk=1 is a random partition of the sample of individuals{1,...,n } into K subsamples of approximately equal size, and{ˆη−k}Kk=1 are cross-fitted nuisance parameter estimators. Chernozhukov et al.

**Rank 3 · `920a867c43048bbc847008ac6b260b56` · page 16 · https://arxiv.org/pdf/2504.08324v2**

2.3 Ingredients of DML

To reduce the dependence of estimators forθ0 on the estimation of high-dimensional nuisances η0, DML estimators rely on two essential components—estimation based on Neyman orthogonal scores and cross-fitting—that mitigate regularization and overfitting bias. We now discuss each in turn.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q07

- **Type:** answerable
- **Question:** In Section 3, what practical simplification applies when computing standard errors for the DML estimator?
- **Gold / expected behavior (post-run audit only):** They can be computed as if the nuisance functions were known.
- **Agent status:** `answered`
- **Agent answer:** With Neyman-orthogonal scores and cross-fitting, standard errors for the DML estimator can be computed as if the nuisance functions were known. [00179456a14aa5a51f9f6f107ae6ec73 | page 22]
- **Citation IDs:** `00179456a14aa5a51f9f6f107ae6ec73`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1261, output=99, total=1360
- **Latency / estimated cost:** 3939.166 ms / $0.0001756
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:7`

### Cited passages

**`00179456a14aa5a51f9f6f107ae6ec73` · rank 1 · page 22 · https://arxiv.org/pdf/2504.08324v2**

(2018) provide conditions that allow researchers to make valid inferential statements aboutθ0 using the DML estimatorˆθDML. These conditions involve conventional sampling and regularity conditions along with the assumption that the nuisance parameter estimator,ˆη, converges sufficiently quickly, as discussed in Section 2.2. Under these assumptions, the DML estimator is asymptotically normal: √nˆΣ−1/2(ˆθDML−θ0) d→N (0, I), where ˆΣ =ˆJ−1   1 n K∑ k=1 ∑ i∈Ik m(Wi;ˆθDML,ˆη−k)m(Wi;ˆθDML,ˆη−k)⊤   ˆJ−1⊤, ˆJ = 1n K∑k=1∑i∈Ik ∂∂θ{m(Wi;θ,ˆη−k)}⏐⏐⏐θ=ˆθDM L. (19) Standard errors forˆθ are thus given by square-roots of the diagonal values ofˆΣ/n. A key practical implication of using both Neyman orthogonal scores and cross-fitting is that standard errors for ˆθDML can be computed as if the nuisance functions were known.

### Final context

**Rank 1 · `00179456a14aa5a51f9f6f107ae6ec73` · page 22 · https://arxiv.org/pdf/2504.08324v2**

(2018) provide conditions that allow researchers to make valid inferential statements aboutθ0 using the DML estimatorˆθDML. These conditions involve conventional sampling and regularity conditions along with the assumption that the nuisance parameter estimator,ˆη, converges sufficiently quickly, as discussed in Section 2.2. Under these assumptions, the DML estimator is asymptotically normal: √nˆΣ−1/2(ˆθDML−θ0) d→N (0, I), where ˆΣ =ˆJ−1   1 n K∑ k=1 ∑ i∈Ik m(Wi;ˆθDML,ˆη−k)m(Wi;ˆθDML,ˆη−k)⊤   ˆJ−1⊤, ˆJ = 1n K∑k=1∑i∈Ik ∂∂θ{m(Wi;θ,ˆη−k)}⏐⏐⏐θ=ˆθDM L. (19) Standard errors forˆθ are thus given by square-roots of the diagonal values ofˆΣ/n. A key practical implication of using both Neyman orthogonal scores and cross-fitting is that standard errors for ˆθDML can be computed as if the nuisance functions were known.

**Rank 2 · `dfe8d60cf75ca862168033fdcaf17034` · page 5 · https://arxiv.org/pdf/2504.08324v2**

Section 2 discusses the practical implications of nuisance estimation and the role of DML’s two key components in their remedy. Section 3 summarizes the asymptotic properties of DML and contains algorithmic details on implementation of generic DML estimators. In the second part of the paper, we turn to simulations and empirical applications, found in Section 4 through Section 6. These examples illustrate DML and provide discussion of key issues that arise in its implementation. In Section 4, we present results from two simulation examples. The first is a simple linear IV example that demonstrates the importance of cross-fitting. The second compares the benefits of the DML average treatment effect estimator with inverse propensity 5

**Rank 3 · `ca97c57761d80d4666d1dd1f33d5fc4f` · page 37 · https://arxiv.org/pdf/2504.08324v2**

Finally, to account for possible dependence in the data, we implement cross-fitting by recruiter, assigning all observations from a given recruiter to the same fold, and compute standard errors clustered at the recruiter level.19 Table 5 shows that DML estimates can be highly sensitive to the choice of nuisance estimator, with point estimates ranging from−3.9 to 2.1. These differences highlight a practical challenge with DML: ML offers a rich set of methods, but different learners may yield qualitatively distinct results. This challenge has been noted in the literature. For example, through calibrated simulations, Ahrens et al. (2025) illustrate stark differences in inferential results for target parameters estimated with DML with different nuisance estimators;

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q08

- **Type:** answerable
- **Question:** Why does the many-instrument IV simulation isolate overfitting rather than regularization bias?
- **Gold / expected behavior (post-run audit only):** All compared IV approaches use Neyman orthogonal scores, leaving cross-fitting as the relevant difference.
- **Agent status:** `answered`
- **Agent answer:** Because the IV comparison uses Neyman-orthogonal scores for each approach, the authors treat regularization bias as controlled for and interpret differences as the effect of overfitting and cross-fitting. [4196f4c01d9f15d9a55e56eb873f055f | page 24] The setup is the canonical many-instrument linear IV model, with 200 instruments but signal in only the first six. [15a078cdc96d38c502da20e2aac41eac | page 24]
- **Citation IDs:** `15a078cdc96d38c502da20e2aac41eac`, `4196f4c01d9f15d9a55e56eb873f055f`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1183, output=299, total=1482
- **Latency / estimated cost:** 4268.937 ms / $0.0002678
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:8`

### Cited passages

**`15a078cdc96d38c502da20e2aac41eac` · rank 3 · page 24 · https://arxiv.org/pdf/2504.08324v2**

4.1 Instrumental Variables with Many Instruments

We present simulation results from the canonical many-instrument linear IV model (see Example 3). We generate data asi.i.d. realizations from Y =θ0D +ε, D =g0(Z) +ν, (ε,ν )′⊥Z. HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution. We define the nuisance functionas g0(Z) =Z′π0, wherethefirstsixelementsof π0 aresetto0.1andtheremaining entries are set to 0. That is, only the first six instruments carry any signal. In our setting, OLS suffers from an upward bias of around 0.5. All results are based on a sample size of 24

**`4196f4c01d9f15d9a55e56eb873f055f` · rank 2 · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

### Final context

**Rank 1 · `716c1388156f01f96544338c5d9cac9c` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4 Two Simulation Illustrations

This section employs two simulation exercises to illustrate the consequences of relying on non-Neyman orthogonal scores and of failing to perform cross-fitting when using flexible nuisance estimators such as ML methods. We discuss two simulations to underscore that bias dominates in some contexts, while regularization bias prevails in others The first simulation focuses on the role of cross-fitting in the linear IV setting with many instruments. This problem has been thoroughly studied since the mid-1990s (e.g., Bekker, 1994). One of the recommendations to emerge from this literature is to use sample-splitting to reduce overfitting bias (often termed “many instruments bias” in this context). Our simulation revisits this classical many instrument setup by comparing linear IV estimation with ML-based IV estimation.

**Rank 2 · `4196f4c01d9f15d9a55e56eb873f055f` · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

**Rank 3 · `15a078cdc96d38c502da20e2aac41eac` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4.1 Instrumental Variables with Many Instruments

We present simulation results from the canonical many-instrument linear IV model (see Example 3). We generate data asi.i.d. realizations from Y =θ0D +ε, D =g0(Z) +ν, (ε,ν )′⊥Z. HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution. We define the nuisance functionas g0(Z) =Z′π0, wherethefirstsixelementsof π0 aresetto0.1andtheremaining entries are set to 0. That is, only the first six instruments carry any signal. In our setting, OLS suffers from an upward bias of around 0.5. All results are based on a sample size of 24

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q09

- **Type:** answerable
- **Question:** How many instruments are generated in the paper's many-instrument simulation?
- **Gold / expected behavior (post-run audit only):** Two hundred simulated instruments.
- **Agent status:** `answered`
- **Agent answer:** The simulation generates 200 instruments. [15a078cdc96d38c502da20e2aac41eac | page 24]
- **Citation IDs:** `15a078cdc96d38c502da20e2aac41eac`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1222, output=70, total=1292
- **Latency / estimated cost:** 3491.021 ms / $0.0001572
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:9`

### Cited passages

**`15a078cdc96d38c502da20e2aac41eac` · rank 1 · page 24 · https://arxiv.org/pdf/2504.08324v2**

4.1 Instrumental Variables with Many Instruments

We present simulation results from the canonical many-instrument linear IV model (see Example 3). We generate data asi.i.d. realizations from Y =θ0D +ε, D =g0(Z) +ν, (ε,ν )′⊥Z. HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution. We define the nuisance functionas g0(Z) =Z′π0, wherethefirstsixelementsof π0 aresetto0.1andtheremaining entries are set to 0. That is, only the first six instruments carry any signal. In our setting, OLS suffers from an upward bias of around 0.5. All results are based on a sample size of 24

### Final context

**Rank 1 · `15a078cdc96d38c502da20e2aac41eac` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4.1 Instrumental Variables with Many Instruments

We present simulation results from the canonical many-instrument linear IV model (see Example 3). We generate data asi.i.d. realizations from Y =θ0D +ε, D =g0(Z) +ν, (ε,ν )′⊥Z. HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution. We define the nuisance functionas g0(Z) =Z′π0, wherethefirstsixelementsof π0 aresetto0.1andtheremaining entries are set to 0. That is, only the first six instruments carry any signal. In our setting, OLS suffers from an upward bias of around 0.5. All results are based on a sample size of 24

**Rank 2 · `716c1388156f01f96544338c5d9cac9c` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4 Two Simulation Illustrations

This section employs two simulation exercises to illustrate the consequences of relying on non-Neyman orthogonal scores and of failing to perform cross-fitting when using flexible nuisance estimators such as ML methods. We discuss two simulations to underscore that bias dominates in some contexts, while regularization bias prevails in others The first simulation focuses on the role of cross-fitting in the linear IV setting with many instruments. This problem has been thoroughly studied since the mid-1990s (e.g., Bekker, 1994). One of the recommendations to emerge from this literature is to use sample-splitting to reduce overfitting bias (often termed “many instruments bias” in this context). Our simulation revisits this classical many instrument setup by comparing linear IV estimation with ML-based IV estimation.

**Rank 3 · `d15eecb188cf25f3e4318f2c2e17f2f7` · page 25 · https://arxiv.org/pdf/2504.08324v2**

This estimator is infeasible in practice but serves as an efficient baseline. We next consider two-stage least squares using all 200 instruments (2SLS). As is well-known from the many-instruments literature, 2SLS performs poorly when the number of instruments is large. We implement DML with a linear first stage regression using all 200 instruments. Note that this DML estimator is essentially split-sample IV (SSIV; Angrist and Krueger, 1995a; Angrist, Imbens, and Krueger, 1999).12 One can thus view DML in this context as an extension of SSIV that also accommodates the use of flexible first stage estimators, for example, because the researcher does not want assume linearity and is unsure about which instruments matter. To this end, we also estimate the first stage using gradient boosted trees, both without cross-fitting (Boosted Trees) and with cross-fitting (DML with Boosted Trees).

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q10

- **Type:** answerable
- **Question:** What combination produced reliable sampling behavior in the calibrated average-treatment-effect simulation?
- **Gold / expected behavior (post-run audit only):** The combination of Neyman orthogonality and cross-fitting.
- **Agent status:** `answered`
- **Agent answer:** DML using Neyman-orthogonal scores produced the reliable behavior: its estimates were approximately unbiased, and its confidence intervals had coverage close to the nominal level [65b78ec3ae991057ae7fd46a0eb16772 | page 17].
- **Citation IDs:** `65b78ec3ae991057ae7fd46a0eb16772`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1005, output=298, total=1303
- **Latency / estimated cost:** 4963.480 ms / $0.0002495
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:10`

### Cited passages

**`65b78ec3ae991057ae7fd46a0eb16772` · rank 3 · page 17 · https://arxiv.org/pdf/2504.08324v2**

By alleviating the first-order impact of nuisance estimation, Neyman orthogonality makes it possible to combine such methods with standard asymptotic approximations, enabling formally valid inference forθ0 while exploiting modern flexible estimators for nuisance parameters. We illustrate the importance of using Neyman orthogonal scores for obtaining reliable finite-sample inference in Section 4. There, we present simulation results demonstrating that estimators of the average treatment effect (ATE) based on non-orthogonal scores may exhibit substantial bias, and the associated confidence intervals are often severely distorted. In contrast, DML estimators, which incorporate Neyman orthogonal scores as a core component, are approximately unbiased, and their confidence intervals achieve coverage rates close to the nominal level. Neyman orthogonal scores for common parameters.

### Final context

**Rank 1 · `5ac06bfcf639759067e75417d127d083` · page 26 · https://arxiv.org/pdf/2504.08324v2**

4.2 Average Treatment Effect Estimation

This section uses a calibrated simulation to illustrate the importance of Neyman orthogonality for valid inference. We focus on estimation of the average treatment effect (ATE) 26

**Rank 2 · `dfe8d60cf75ca862168033fdcaf17034` · page 5 · https://arxiv.org/pdf/2504.08324v2**

Section 2 discusses the practical implications of nuisance estimation and the role of DML’s two key components in their remedy. Section 3 summarizes the asymptotic properties of DML and contains algorithmic details on implementation of generic DML estimators. In the second part of the paper, we turn to simulations and empirical applications, found in Section 4 through Section 6. These examples illustrate DML and provide discussion of key issues that arise in its implementation. In Section 4, we present results from two simulation examples. The first is a simple linear IV example that demonstrates the importance of cross-fitting. The second compares the benefits of the DML average treatment effect estimator with inverse propensity 5

**Rank 3 · `65b78ec3ae991057ae7fd46a0eb16772` · page 17 · https://arxiv.org/pdf/2504.08324v2**

By alleviating the first-order impact of nuisance estimation, Neyman orthogonality makes it possible to combine such methods with standard asymptotic approximations, enabling formally valid inference forθ0 while exploiting modern flexible estimators for nuisance parameters. We illustrate the importance of using Neyman orthogonal scores for obtaining reliable finite-sample inference in Section 4. There, we present simulation results demonstrating that estimators of the average treatment effect (ATE) based on non-orthogonal scores may exhibit substantial bias, and the associated confidence intervals are often severely distorted. In contrast, DML estimators, which incorporate Neyman orthogonal scores as a core component, are approximately unbiased, and their confidence intervals achieve coverage rates close to the nominal level. Neyman orthogonal scores for common parameters.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q11

- **Type:** answerable
- **Question:** What was the size and wave range of the balanced HRS panel used in the hospitalization application?
- **Gold / expected behavior (post-run audit only):** 656 households observed over waves 7 through 11.
- **Agent status:** `answered`
- **Agent answer:** The balanced HRS panel contained 656 households, observed from waves 7 through 11. [aba1a68f17ebf1eebfedd4c86eaff838 | page 29]
- **Citation IDs:** `aba1a68f17ebf1eebfedd4c86eaff838`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1194, output=85, total=1279
- **Latency / estimated cost:** 3700.363 ms / $0.0001619
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:11`

### Cited passages

**`aba1a68f17ebf1eebfedd4c86eaff838` · rank 1 · page 29 · https://arxiv.org/pdf/2504.08324v2**

(2018) analyze the causal effect of hospital admission on several economic outcomes, including out-of-pocket medical spending, using conventional two-way fixed effects applied to a panel of U.S. households from the Health and Retirement Study (HRS). Sun and Abraham (2021) extend this analysis by estimating dynamic effects using more flexible methods that allow for treatment effect heterogeneity. We use the same data as Sun and Abraham (2021), which consist of a balanced panel of 656 households observed over waves 7 through 11 of the HRS.15 We proceed in two steps. In Section 5.1, we estimate the change in out-of-pocket medical spending at time periodt caused by hospitalization at timeg for all potential pairs (t,g ) in the data. In Section 5.2, we then aggregate these estimates for inference 15See Table 2 of Sun and Abraham (2021) for summary statistics of the HRS sample we use. 29

### Final context

**Rank 1 · `aba1a68f17ebf1eebfedd4c86eaff838` · page 29 · https://arxiv.org/pdf/2504.08324v2**

(2018) analyze the causal effect of hospital admission on several economic outcomes, including out-of-pocket medical spending, using conventional two-way fixed effects applied to a panel of U.S. households from the Health and Retirement Study (HRS). Sun and Abraham (2021) extend this analysis by estimating dynamic effects using more flexible methods that allow for treatment effect heterogeneity. We use the same data as Sun and Abraham (2021), which consist of a balanced panel of 656 households observed over waves 7 through 11 of the HRS.15 We proceed in two steps. In Section 5.1, we estimate the change in out-of-pocket medical spending at time periodt caused by hospitalization at timeg for all potential pairs (t,g ) in the data. In Section 5.2, we then aggregate these estimates for inference 15See Table 2 of Sun and Abraham (2021) for summary statistics of the HRS sample we use. 29

**Rank 2 · `cc7f74b55c93016a267c008dd5f8cf3c` · page 34 · https://arxiv.org/pdf/2504.08324v2**

Figure 3 displays the estimated dynamic effects of hospitalization obtained from the different GT-ATT estimators considered previously. Across methods, we find no statistically significant effects in the pre-treatment period and a large, significant increase in out-of-pocket medical spending immediately following hospitalization. DML estimates and the parametric AIPW alternative are quantitatively similar overall, and the variation in DML across different cross-fitting splits is quite small. One notable difference is at event time−3: the DML estimate is substantially less precise than the parametric alternative. Because only group 10 has outcomes observed three periods before hospitalization, this dynamic effect corresponds exactly to group 10’s pre-treatment effect in Wave 7, which we discussed in the preceding section.

**Rank 3 · `875ff9f481bc4cae91e9ab5d6af07133` · page 29 · https://arxiv.org/pdf/2504.08324v2**

5 Economic Consequences of Hospital Admission

To demonstrate the flexibility of DML, we apply it in a staggered adoption panel setting to estimate group-time average treatment effects on the treated and dynamic average treatment effects as discussed in Callaway and Sant’Anna (2021). Outside of illustrating the application of DML in a canonical panel data setting, we further use this example to discuss the additional randomness introduced in DML due to the use of sample splitting. We show that simply repeating the DML estimation can help us gauge the robustness of conclusions to particular sample splits. We then outline the median aggregation approach presented in Chernozhukov et al. (2018) as a way to summarize results across repetitions. Our example builds on Dobkin et al. (2018) and Sun and Abraham (2021). Dobkin et al.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q12

- **Type:** answerable
- **Question:** What does repeating DML estimation help assess in the hospitalization example?
- **Gold / expected behavior (post-run audit only):** It helps assess whether conclusions are robust to particular random sample splits.
- **Agent status:** `answered`
- **Agent answer:** Repeating the DML estimation helps assess how robust the conclusions are to the particular sample splits used. The paper also describes median aggregation as a way to summarize results across repetitions. [875ff9f481bc4cae91e9ab5d6af07133 | page 29]
- **Citation IDs:** `875ff9f481bc4cae91e9ab5d6af07133`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1130, output=101, total=1231
- **Latency / estimated cost:** 3212.468 ms / $0.0001635
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:12`

### Cited passages

**`875ff9f481bc4cae91e9ab5d6af07133` · rank 1 · page 29 · https://arxiv.org/pdf/2504.08324v2**

5 Economic Consequences of Hospital Admission

To demonstrate the flexibility of DML, we apply it in a staggered adoption panel setting to estimate group-time average treatment effects on the treated and dynamic average treatment effects as discussed in Callaway and Sant’Anna (2021). Outside of illustrating the application of DML in a canonical panel data setting, we further use this example to discuss the additional randomness introduced in DML due to the use of sample splitting. We show that simply repeating the DML estimation can help us gauge the robustness of conclusions to particular sample splits. We then outline the median aggregation approach presented in Chernozhukov et al. (2018) as a way to summarize results across repetitions. Our example builds on Dobkin et al. (2018) and Sun and Abraham (2021). Dobkin et al.

### Final context

**Rank 1 · `875ff9f481bc4cae91e9ab5d6af07133` · page 29 · https://arxiv.org/pdf/2504.08324v2**

5 Economic Consequences of Hospital Admission

To demonstrate the flexibility of DML, we apply it in a staggered adoption panel setting to estimate group-time average treatment effects on the treated and dynamic average treatment effects as discussed in Callaway and Sant’Anna (2021). Outside of illustrating the application of DML in a canonical panel data setting, we further use this example to discuss the additional randomness introduced in DML due to the use of sample splitting. We show that simply repeating the DML estimation can help us gauge the robustness of conclusions to particular sample splits. We then outline the median aggregation approach presented in Chernozhukov et al. (2018) as a way to summarize results across repetitions. Our example builds on Dobkin et al. (2018) and Sun and Abraham (2021). Dobkin et al.

**Rank 2 · `cc7f74b55c93016a267c008dd5f8cf3c` · page 34 · https://arxiv.org/pdf/2504.08324v2**

Figure 3 displays the estimated dynamic effects of hospitalization obtained from the different GT-ATT estimators considered previously. Across methods, we find no statistically significant effects in the pre-treatment period and a large, significant increase in out-of-pocket medical spending immediately following hospitalization. DML estimates and the parametric AIPW alternative are quantitatively similar overall, and the variation in DML across different cross-fitting splits is quite small. One notable difference is at event time−3: the DML estimate is substantially less precise than the parametric alternative. Because only group 10 has outcomes observed three periods before hospitalization, this dynamic effect corresponds exactly to group 10’s pre-treatment effect in Wave 7, which we discussed in the preceding section.

**Rank 3 · `e46eebc5dce82e6a997dee7d3282fcab` · page 32 · https://arxiv.org/pdf/2504.08324v2**

The results strengthen the economic conclusions of Dobkin et al. (2018) and Sun and Abraham (2021). When we use DML to estimate the same effects allowing for parallel trends to hold only conditional on controls and using a flexible method to include those controls, we continue to estimate that hospitalization causes a substantial and significant increase in out-of-pocket medical spending in the period immediately following the event. This conclusion holds for all three cohorts considered in our analysis. We also compare the DML estimates to those obtained using the parametric AIPW estimator proposed by Sant’Anna and Zhao (2020). This estimator relies on the same AIPW score as DML but differs in how the nuisance functions are estimated.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q13

- **Type:** answerable
- **Question:** Which online labor platform is studied in the paper's monopsony application?
- **Gold / expected behavior (post-run audit only):** Amazon MTurk.
- **Agent status:** `answered`
- **Agent answer:** The paper studies monopsony on Amazon MTurk, an online platform for hiring workers to perform tasks. [c7a398e572f892c424d0b76ece0ed77a | page 35]
- **Citation IDs:** `c7a398e572f892c424d0b76ece0ed77a`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1059, output=86, total=1145
- **Latency / estimated cost:** 3397.562 ms / $0.0001489
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:13`

### Cited passages

**`c7a398e572f892c424d0b76ece0ed77a` · rank 1 · page 35 · https://arxiv.org/pdf/2504.08324v2**

6 Monopsony in Online Markets

We revisit the Dube et al. (2020) paper on monopsony power on Amazon MTurk, an online platform for hiring workers to perform tasks. The research falls into the wider literature estimating the labor supply elasticity (see reviews in Sokolova and Sorensen, 35

### Final context

**Rank 1 · `c7a398e572f892c424d0b76ece0ed77a` · page 35 · https://arxiv.org/pdf/2504.08324v2**

6 Monopsony in Online Markets

We revisit the Dube et al. (2020) paper on monopsony power on Amazon MTurk, an online platform for hiring workers to perform tasks. The research falls into the wider literature estimating the labor supply elasticity (see reviews in Sokolova and Sorensen, 35

**Rank 2 · `6c0058e8d831482825782702a5e184dc` · page 6 · https://arxiv.org/pdf/2504.08324v2**

(2020) who apply DML to estimate the labor supply elasticity in online labor markets using textual controls. We have two main goals in this section: to illustrate the use of complex non-tabular data and, more importantly, to illustrate that DML estimates can vary substantially across otherwise reasonable choices of machinelearners (i.e., algorithms used to estimate nuisance functions). This sensitivity can lead to qualitatively different conclusions about economically meaningful parameters. Because it seems difficult to knowex ante exactly which learner one should choose in these situations, we use this example to discuss robustness checks and suggest strategies for selecting ML algorithms. Section 7 concludes by summarizing takeaways, raising some caveats, and pointing to potential directions for further research.

**Rank 3 · `840481e38cf0d634a7f107be2c05cae0` · page 2 · https://arxiv.org/pdf/2504.08324v2**

summarizing these relationships, including average treatment effects or regression coefficients, frequently depend onnuisances—auxiliary objects that must be accounted for to identify the parameter of interest but are not themselves of primary interest, such as regression coefficients on control variables. As a concrete example that we will revisit in our empirical illustrations, consider Dube et al. (2020), who study monopsony power on the online platform MTurk using partially linear regression: Y =θ0D +g0(X) +ε where Y is the logarithm of the time it takes for a posted job to be filled,D is the logarithm of the reward of the job,X denotes observed features of tasks including their type and complexity, andε is assumed to be uncorrelated withD and mean independent of X, i.e., E[Dε] = 0 and E[ε|X] = 0.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q14

- **Type:** answerable
- **Question:** Which tools do the authors recommend for evaluating choices among nuisance-function estimators?
- **Gold / expected behavior (post-run audit only):** Cross-fitted performance metrics such as R-squared, the CVC test, and model averaging.
- **Agent status:** `answered`
- **Agent answer:** The authors recommend cross-fitted performance metrics such as \(R^2\), the CVC test, and model-averaging approaches for evaluating nuisance-function estimator choices. [20bcc1b0d7906926f811987d806147ea | page 39]
- **Citation IDs:** `20bcc1b0d7906926f811987d806147ea`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1031, output=98, total=1129
- **Latency / estimated cost:** 3734.664 ms / $0.0001521
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:14`

### Cited passages

**`20bcc1b0d7906926f811987d806147ea` · rank 1 · page 39 · https://arxiv.org/pdf/2504.08324v2**

In practice, we recommend using a diverse set of nuisance function estimators to increase the credibility of DML estimates. Appropriate tools for evaluating these choices include cross-fitted performance metrics such asR2, the CVC test, and model averaging approaches.

### Final context

**Rank 1 · `20bcc1b0d7906926f811987d806147ea` · page 39 · https://arxiv.org/pdf/2504.08324v2**

In practice, we recommend using a diverse set of nuisance function estimators to increase the credibility of DML estimates. Appropriate tools for evaluating these choices include cross-fitted performance metrics such asR2, the CVC test, and model averaging approaches.

**Rank 2 · `7ce34352406f03c7e28872629980203f` · page 36 · https://arxiv.org/pdf/2504.08324v2**

2021; Langella and Manning, 2021). This example is useful for at least two reasons. First, it illustrates how DML can incorporate complex, non-tabular data, such as text or images, which are increasingly common in empirical economics (e.g., Ash and Hansen, 2023). Second, it provides an interesting setting for discussing the choice of ML method for nuisance estimation. In particular, it highlights the importance of selecting learners and tuning parameters to support credible inference. We use this example to discuss methods for evaluating such choices. Dube et al. (2020) consider multiple identification strategies and datasets for studying monopsony power. We focus here on their analysis of a cross-sectional sample compiled by Ipeirotis (2010). The parameter of interest is the partially linear regression coefficientθ0 introduced in Example 2.

**Rank 3 · `ce0411f70dd2ee464ccbf2358eddf7ab` · page 40 · https://arxiv.org/pdf/2504.08324v2**

These results suggest the use of relatively small values forK, but do not provide more specific guidance. Velez (2024) provides a higher-order analysis within a restricted class of nuisance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational resources. When the sample size is very small, larger values ofK may be desirable, and if resources permit, sensitivity analysis toK is worthwhile.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q15

- **Type:** answerable
- **Question:** What identification problem does DML not solve for a researcher?
- **Gold / expected behavior (post-run audit only):** It does not choose interesting target parameters or identify them; careful substantive reasoning is still required.
- **Agent status:** `answered`
- **Agent answer:** DML does not tell the researcher which target parameter is interesting or how to identify it; those require separate substantive reasoning. [e3bf4a09dd39a55429ff8f1a23d1db6d | page 40]
- **Citation IDs:** `e3bf4a09dd39a55429ff8f1a23d1db6d`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1162, output=94, total=1256
- **Latency / estimated cost:** 3498.762 ms / $0.0001632
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:15`

### Cited passages

**`e3bf4a09dd39a55429ff8f1a23d1db6d` · rank 1 · page 40 · https://arxiv.org/pdf/2504.08324v2**

While DML provides robustness to the estimation of nuisance parameters, it is not a panacea. It does not tell the researcher what interesting target parameters are or how to identify them. Rather, it complements careful reasoning about objects of interest and their identification. Implementation Guidance. When implementing DML, researchers face several design choices. One key decision is how to partition the data. With independent observations, forming folds at random provides a natural default. More generally, researchers should aim to form approximately independent folds by using partitions that respect any underlying dependence structure in the data, as noted in Remark 1. Researchers also need to select the number of foldsK. Standard asymptotic results apply for any fixedK; see, e.g., Chernozhukov et al. (2018).

### Final context

**Rank 1 · `e3bf4a09dd39a55429ff8f1a23d1db6d` · page 40 · https://arxiv.org/pdf/2504.08324v2**

While DML provides robustness to the estimation of nuisance parameters, it is not a panacea. It does not tell the researcher what interesting target parameters are or how to identify them. Rather, it complements careful reasoning about objects of interest and their identification. Implementation Guidance. When implementing DML, researchers face several design choices. One key decision is how to partition the data. With independent observations, forming folds at random provides a natural default. More generally, researchers should aim to form approximately independent folds by using partitions that respect any underlying dependence structure in the data, as noted in Remark 1. Researchers also need to select the number of foldsK. Standard asymptotic results apply for any fixedK; see, e.g., Chernozhukov et al. (2018).

**Rank 2 · `7ce34352406f03c7e28872629980203f` · page 36 · https://arxiv.org/pdf/2504.08324v2**

2021; Langella and Manning, 2021). This example is useful for at least two reasons. First, it illustrates how DML can incorporate complex, non-tabular data, such as text or images, which are increasingly common in empirical economics (e.g., Ash and Hansen, 2023). Second, it provides an interesting setting for discussing the choice of ML method for nuisance estimation. In particular, it highlights the importance of selecting learners and tuning parameters to support credible inference. We use this example to discuss methods for evaluating such choices. Dube et al. (2020) consider multiple identification strategies and datasets for studying monopsony power. We focus here on their analysis of a cross-sectional sample compiled by Ipeirotis (2010). The parameter of interest is the partially linear regression coefficientθ0 introduced in Example 2.

**Rank 3 · `b33db9d0a6fdb603d4f9d315278d9f97` · page 3 · https://arxiv.org/pdf/2504.08324v2**

Even a single continuous covariate may create a high-dimensional problem—for example, when identification relies on rainfall instruments that can be nonlinearly related to an endogenous regressor (e.g., Hidalgo et al., 2010; Gilchrist and Sands, 2016; Dustmann, Fasani, and Speciale, 2017). As rich data become more common in applied research, there is growing appreciation that traditional functional form assumptions are often difficult to justify, motivating the use of more flexible tools for estimating nuisance parameters. As a result, there is increasing interest in using machine learning (ML) methods, which provide flexible tools for estimating high-dimensional nuisance parameters. A natural use of ML would then be to obtain nuisance parameter estimates,ˆη, and use these in place ofη0 in (1).

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q21

- **Type:** insufficient evidence
- **Question:** What numerical effect does the paper report for DML on Vietnam's GDP growth in 2025?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1186, output=89, total=1275
- **Latency / estimated cost:** 3151.927 ms / $0.0001631
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:16`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `af20f85a1b72cbacbd98cf5922abc6b9` · page 33 · https://arxiv.org/pdf/2504.08324v2**

Relative to the size of the standard errors, the median-aggregated DML estimates (in Column 6) and the AIPW DiD estimates (Column 8) are qualitatively similar. The most notable exception is group 9’s treatment effect in Wave 10. The parametric estimate is 2534 (s.e. = 422) and thus substantially larger than the DML estimate of 937 (s.e. = 434). Further, group 10’s pre-treatment effect in Wave 7 is negative under DML (−1492, s.e. = 2223) but positive under the parametric estimator (1222, s.e. = 1127), though both are imprecisely estimated due to the small cohort size. While the true effects are unknown, the discrepancy highlights the potential for results to strongly differ based on nuisance function specification. We return to this issue in Section 6.

**Rank 2 · `cc7f74b55c93016a267c008dd5f8cf3c` · page 34 · https://arxiv.org/pdf/2504.08324v2**

Figure 3 displays the estimated dynamic effects of hospitalization obtained from the different GT-ATT estimators considered previously. Across methods, we find no statistically significant effects in the pre-treatment period and a large, significant increase in out-of-pocket medical spending immediately following hospitalization. DML estimates and the parametric AIPW alternative are quantitatively similar overall, and the variation in DML across different cross-fitting splits is quite small. One notable difference is at event time−3: the DML estimate is substantially less precise than the parametric alternative. Because only group 10 has outcomes observed three periods before hospitalization, this dynamic effect corresponds exactly to group 10’s pre-treatment effect in Wave 7, which we discussed in the preceding section.

**Rank 3 · `2e0ba1f6ad4b9f8fd5583b237eada3b9` · page 5 · https://arxiv.org/pdf/2504.08324v2**

Furthermore, DML is easy to implement, applicable to a wide range of econometric settings, and readily available in existing software packages, including Stata, R, and Python (e.g., Bach et al., 2021; Bach et al., 2022; Ahrens et al., 2024; Wiemann et al., 2023). DML thus has the potential to enhance the credibility of research findings in a broad spectrum of settings, either when used as a complementary robustness check or when the application necessitates the use of flexible estimation methods for nuisance objects. While DML offers a framework for combining flexible nuisance estimation with valid asymptotic inference, its implementation raises important challenges. Available theoretical results assume the nuisance functions are estimated with sufficiently high accuracy.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## dev/hybrid · q22

- **Type:** insufficient evidence
- **Question:** Which GPU model and training duration were used to train the DML method described in the paper?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1082, output=103, total=1185
- **Latency / estimated cost:** 3600.332 ms / $0.0001597
- **Original trace:** `results/agent/dev/hybrid_traces.jsonl:17`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `f2869c7fd423240ca03dadc998b37a2d` · page 36 · https://arxiv.org/pdf/2504.08324v2**

We use fine-tuning to adapt the pre-trained parameters to our setting, thereby improving predictive performance.18 Fine-tuning is performed separately for the outcome and treatment models in each cross-fitting iteration, alleviating concerns about inducing over-fitting bias. We consider 12 candidate learners that are trained on hand-coded controls and finetuned embeddings: OLS as a simple unregularized baseline, cross-validated lasso and ridge as regularized linear methods, and, to allow for nonlinearities, three implementations of 18We implement fine-tuning using Low-Rank Adaptation (LoRA; Hu et al., 2021). Rather than fully retraining all parameters, LoRA optimizes a low-rank decomposition of the parameters updates, effectively modifying the model within a regularized subspace. 36

**Rank 2 · `f5e5d52f9eacf43471c6e02cf8baaefa` · page 37 · https://arxiv.org/pdf/2504.08324v2**

DML estimation uses theR package ddml (Wiemann et al., 2023). The nuisance estimators were implemented with glmnet (Friedman, Hastie, and Tibshirani, 2010),ranger (Wright and Ziegler, 2017),XGBoost (Chen and Guestrin, 2016), and keras (Kalinowski, Allaire, and Chollet, 2025). Standard errors are clustered at the recruiter level. random forests, three implementations of gradient boosting (XGBoost), and three feedforward neural network architectures. The tuning parameters are reported in Table 5. We set the number of folds toK = 3, repeat cross-fittingS = 5 times, and report the median aggregate estimates.

**Rank 3 · `6256216ecb525c820b3a2bde062da672` · page 1 · https://arxiv.org/pdf/2504.08324v2**

Consequently, DML allows the use of flexible methods, including machine learning tools, for estimating nuisance functions, reducing the dependence on auxiliary functional form assumptions and enabling the use of complex non-tabular data, such as text or images. We illustrate the application of DML through simulations and empirical examples. We conclude with a discussion of recommended practices. A companion website includes additional examples with code and references to other resources.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q16

- **Type:** answerable
- **Question:** In Section 7, what conventional values of K are reported to work well in many simulation settings?
- **Gold / expected behavior (post-run audit only):** Five or ten folds.
- **Agent status:** `answered`
- **Agent answer:** Section 7 reports that conventional choices of \(K=5\) or \(K=10\) work well in many simulation settings. [ce0411f70dd2ee464ccbf2358eddf7ab | page 40]
- **Citation IDs:** `ce0411f70dd2ee464ccbf2358eddf7ab`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=905, output=95, total=1000
- **Latency / estimated cost:** 3547.661 ms / $0.0001380
- **Original trace:** `results/agent/test/dense_traces.jsonl:1`

### Cited passages

**`ce0411f70dd2ee464ccbf2358eddf7ab` · rank 2 · page 40 · https://arxiv.org/pdf/2504.08324v2**

These results suggest the use of relatively small values forK, but do not provide more specific guidance. Velez (2024) provides a higher-order analysis within a restricted class of nuisance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational resources. When the sample size is very small, larger values ofK may be desirable, and if resources permit, sensitivity analysis toK is worthwhile.

### Final context

**Rank 1 · `bf3801aa568c095b969cec06d59b4053` · page 29 · https://arxiv.org/pdf/2504.08324v2**

For the remaining estimators, intervals are computed using the infeasible simulation standard deviation. Results are based on 10000 simulation replications. on combining Neyman orthogonality with cross-fitting.

**Rank 2 · `ce0411f70dd2ee464ccbf2358eddf7ab` · page 40 · https://arxiv.org/pdf/2504.08324v2**

These results suggest the use of relatively small values forK, but do not provide more specific guidance. Velez (2024) provides a higher-order analysis within a restricted class of nuisance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational resources. When the sample size is very small, larger values ofK may be desirable, and if resources permit, sensitivity analysis toK is worthwhile.

**Rank 3 · `5ac06bfcf639759067e75417d127d083` · page 26 · https://arxiv.org/pdf/2504.08324v2**

4.2 Average Treatment Effect Estimation

This section uses a calibrated simulation to illustrate the importance of Neyman orthogonality for valid inference. We focus on estimation of the average treatment effect (ATE) 26

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q17

- **Type:** answerable
- **Question:** When the best nuisance learner is unknown in advance, what candidate-method strategy is recommended?
- **Gold / expected behavior (post-run audit only):** Consider a diverse set including parametric benchmarks, regularized regression, tree-based models, and neural networks.
- **Agent status:** `answered`
- **Agent answer:** Use a candidate pool rather than committing to one learner in advance. Evaluate nuisance learners separately for each nuisance function, since the best learner may differ across functions; then select or combine suitable candidates. One option is stacking/model averaging, which weights learners to minimize out-of-sample prediction error. [cfe19ed7d9241560249490980c989653 | page 39] [f43dcecc0ef3d9c930d0ea9cbeb4c998 | page 38]
- **Citation IDs:** `cfe19ed7d9241560249490980c989653`, `f43dcecc0ef3d9c930d0ea9cbeb4c998`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1170, output=273, total=1443
- **Latency / estimated cost:** 4388.360 ms / $0.0002535
- **Original trace:** `results/agent/test/dense_traces.jsonl:2`

### Cited passages

**`cfe19ed7d9241560249490980c989653` · rank 2 · page 39 · https://arxiv.org/pdf/2504.08324v2**

equation, or by assigning equal weights to all learnersforwhichtheCVC p-valuesarelargerthan0.2. Weuse K = 3 cross-fittingfolds, implementedbyrandomlyassigning recruiters to folds, and report median aggregated estimates obtained usingS = 5 cross-fitting repetitions. Standard errors are clustered at the recruiter level. The results in this application highlight that DML estimates can be sensitive to the choiceofnuisanceestimator. ThissensitivityisconsistentwithconditionsinexistingDML theory, which indicate that poorly tuned or ill-suited learners can yield misleading results. We emphasize that the choice of which learner to use for a particular nuisance function and data set is rarely, if ever, knownex ante. Further, there is no reason to assume that the same learner is best for every nuisance function, although this is implicitly imposed by many common estimation strategies.

**`f43dcecc0ef3d9c930d0ea9cbeb4c998` · rank 3 · page 38 · https://arxiv.org/pdf/2504.08324v2**

Rather than selecting thebest-performing nuisanceestimators based ontheR2 score or the CVC test, we can also combine them through stacking or model averaging approaches (Wolpert, 1996; Breiman, 1996; van der Laan, Polley, and Hubbard, 2007). Stacking constructs a “super learner” as a weighted average of candidate learners, where the weights are chosen to minimize out-of-sample prediction error. Within the DML framework, the stacking weights can be re-estimated at each step of the cross-fitting procedure, or estimated once using the full sample by regressing the outcome on the learners’ cross-fitted predicted values (see Ahrens et al. 2025 for a discussion of various options).

### Final context

**Rank 1 · `9fca0d4987e8fb014d55889b7dfdfd13` · page 35 · https://arxiv.org/pdf/2504.08324v2**

For example, using random forests with higher regularization (minimum node size of 100) yields a first-period treatment effect estimate of 2903 (s.e. = 497), while lower regularization (minimum node size of 1) yields 2666 (s.e. = 571). Pre-treatment effects remain statistically insignificant at the 5% level across all learner and tuning parameter choices considered. The robustness to learner choice is quite different in the example we consider in next section. There we revisit the study on monopsony power of Dube et al. (2020) and illustratethattheselectionandtuningofnuisanceestimatorscanbeempiricallyconsequential. We use this application to demonstrate diagnostic analyses that can assist in evaluating and selecting nuisance estimators.

**Rank 2 · `cfe19ed7d9241560249490980c989653` · page 39 · https://arxiv.org/pdf/2504.08324v2**

equation, or by assigning equal weights to all learnersforwhichtheCVC p-valuesarelargerthan0.2. Weuse K = 3 cross-fittingfolds, implementedbyrandomlyassigning recruiters to folds, and report median aggregated estimates obtained usingS = 5 cross-fitting repetitions. Standard errors are clustered at the recruiter level. The results in this application highlight that DML estimates can be sensitive to the choiceofnuisanceestimator. ThissensitivityisconsistentwithconditionsinexistingDML theory, which indicate that poorly tuned or ill-suited learners can yield misleading results. We emphasize that the choice of which learner to use for a particular nuisance function and data set is rarely, if ever, knownex ante. Further, there is no reason to assume that the same learner is best for every nuisance function, although this is implicitly imposed by many common estimation strategies.

**Rank 3 · `f43dcecc0ef3d9c930d0ea9cbeb4c998` · page 38 · https://arxiv.org/pdf/2504.08324v2**

Rather than selecting thebest-performing nuisanceestimators based ontheR2 score or the CVC test, we can also combine them through stacking or model averaging approaches (Wolpert, 1996; Breiman, 1996; van der Laan, Polley, and Hubbard, 2007). Stacking constructs a “super learner” as a weighted average of candidate learners, where the weights are chosen to minimize out-of-sample prediction error. Within the DML framework, the stacking weights can be re-estimated at each step of the cross-fitting procedure, or estimated once using the full sample by regressing the outcome on the learners’ cross-fitted predicted values (see Ahrens et al. 2025 for a discussion of various options).

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q18

- **Type:** answerable
- **Question:** In Section 2.3.2, why is a fold-specific nuisance estimate independent of observations in the held-out fold?
- **Gold / expected behavior (post-run audit only):** Because it is trained only on observations outside that fold.
- **Agent status:** `answered`
- **Agent answer:** A fold-specific nuisance estimate is fit using a different fold from the one held out for evaluating the score. Since the observations are independent, the training-fold data used to construct the estimate are independent of the held-out observations; sample splitting therefore mimics estimating the nuisance function on one independent dataset and evaluating it on another. [46b3d3c66f0f888a2ab9bfced5cddb51 | page 20]
- **Citation IDs:** `46b3d3c66f0f888a2ab9bfced5cddb51`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1216, output=139, total=1355
- **Latency / estimated cost:** 3202.115 ms / $0.0001911
- **Original trace:** `results/agent/test/dense_traces.jsonl:3`

### Cited passages

**`46b3d3c66f0f888a2ab9bfced5cddb51` · rank 1 · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

### Final context

**Rank 1 · `46b3d3c66f0f888a2ab9bfced5cddb51` · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

**Rank 2 · `e3bf4a09dd39a55429ff8f1a23d1db6d` · page 40 · https://arxiv.org/pdf/2504.08324v2**

While DML provides robustness to the estimation of nuisance parameters, it is not a panacea. It does not tell the researcher what interesting target parameters are or how to identify them. Rather, it complements careful reasoning about objects of interest and their identification. Implementation Guidance. When implementing DML, researchers face several design choices. One key decision is how to partition the data. With independent observations, forming folds at random provides a natural default. More generally, researchers should aim to form approximately independent folds by using partitions that respect any underlying dependence structure in the data, as noted in Remark 1. Researchers also need to select the number of foldsK. Standard asymptotic results apply for any fixedK; see, e.g., Chernozhukov et al. (2018).

**Rank 3 · `acdd8fc9e3a5cd0ea3fab7d797f387e0` · page 15 · https://arxiv.org/pdf/2504.08324v2**

Our usage emphasizes that overfitting in nuisance estimation can lead to bias in target parameter estimation, because it inflates the dependence between nuisance estimation error and the data. The second key ingredient of DML—cross-fitting, also discussed in Section 2.3— addresses overfitting bias by using sample splitting to ensure (approximate) independence between the estimation error in the nuisance function and the observations used in the sample moment condition. This independence implies that the product in the numerator of (⋆) is mean zero whenever either term is mean zero. The two main ingredients of DML, discussed in Section 2.3, are meant to alleviate the first-order impact of nuisance estimation. Estimation of nuisance parameters also generally affects the target parameter through the “higher order terms” in (14).

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q19

- **Type:** answerable
- **Question:** What convergence caveat is reported for deep regression trees in the DML discussion?
- **Gold / expected behavior (post-run audit only):** They may fail to be pointwise consistent.
- **Agent status:** `answered`
- **Agent answer:** The cited caveat is that deep regression trees may fail to be pointwise consistent, so their nuisance estimates may not converge quickly enough for DML’s asymptotic inference guarantees. [3b58ae351244c5e0cf3afdcc0da7a3b2 | page 41]
- **Citation IDs:** `3b58ae351244c5e0cf3afdcc0da7a3b2`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1221, output=103, total=1324
- **Latency / estimated cost:** 3744.673 ms / $0.0001736
- **Original trace:** `results/agent/test/dense_traces.jsonl:4`

### Cited passages

**`3b58ae351244c5e0cf3afdcc0da7a3b2` · rank 1 · page 41 · https://arxiv.org/pdf/2504.08324v2**

From a theoretical standpoint, part of DML’s appeal is that it delivers asymptotically normal inference even when flexible methods are used to estimate nuisance functions. Crucially, provided the nuisance estimator converges sufficiently quickly, the limiting distribution does not depend on the specific choice of nuisance estimator. Of course, it is unrealistic to expect all nuisance estimators to yield sufficiently accurate estimates in all settings. Many modern algorithms do not have theory establishing sufficiently fast rates without strong assumptions. For example, the results in Chi et al. (2022) suggest that random forests, when applied to high-dimensional data with tuning similar to common defaults, may fail to converge quickly enough for DML, and results in Cattaneo, Klusowski, and Yu (2025) establish that deep regression trees may fail to be pointwise consistent.

### Final context

**Rank 1 · `3b58ae351244c5e0cf3afdcc0da7a3b2` · page 41 · https://arxiv.org/pdf/2504.08324v2**

From a theoretical standpoint, part of DML’s appeal is that it delivers asymptotically normal inference even when flexible methods are used to estimate nuisance functions. Crucially, provided the nuisance estimator converges sufficiently quickly, the limiting distribution does not depend on the specific choice of nuisance estimator. Of course, it is unrealistic to expect all nuisance estimators to yield sufficiently accurate estimates in all settings. Many modern algorithms do not have theory establishing sufficiently fast rates without strong assumptions. For example, the results in Chi et al. (2022) suggest that random forests, when applied to high-dimensional data with tuning similar to common defaults, may fail to converge quickly enough for DML, and results in Cattaneo, Klusowski, and Yu (2025) establish that deep regression trees may fail to be pointwise consistent.

**Rank 2 · `f5e5d52f9eacf43471c6e02cf8baaefa` · page 37 · https://arxiv.org/pdf/2504.08324v2**

DML estimation uses theR package ddml (Wiemann et al., 2023). The nuisance estimators were implemented with glmnet (Friedman, Hastie, and Tibshirani, 2010),ranger (Wright and Ziegler, 2017),XGBoost (Chen and Guestrin, 2016), and keras (Kalinowski, Allaire, and Chollet, 2025). Standard errors are clustered at the recruiter level. random forests, three implementations of gradient boosting (XGBoost), and three feedforward neural network architectures. The tuning parameters are reported in Table 5. We set the number of folds toK = 3, repeat cross-fittingS = 5 times, and report the median aggregate estimates.

**Rank 3 · `16bca5d466604199aade410e3aafcbf0` · page 25 · https://arxiv.org/pdf/2504.08324v2**

While one should consider alternative learner choices in practice, we focus on gradient boosted trees with a maximum tree depth of four, a learning rate of 0.1, and early stopping based on a 20% validation set. We use 5-fold cross-fitting for SSIV and DML with gradient boosted trees. We report results in Figure 1 and Table 2. As expected and predicted by the theory, the methods that do not use cross-fitting—2SLS and Boosted Trees—perform poorly. Although the distributions of estimates are tightly concentrated, they are centered far from the truth, yielding average biases an order of magnitude larger than estimators 11Specifically, we generateZ∼ N(0p,. 4Ip +.6ιpι′p) and (ε,ν )′ = N(02, Σ) with Σ11 = Σ 22 = 1 and Σ21 = Σ21 =.6. We use0p and ιp to denote ap× 1 vector of zeros and ones, respectively;Ip denotes a p×p identity matrix.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q20

- **Type:** answerable
- **Question:** In the IV simulation, why are the five estimators described as isolating the impact of cross-fitting?
- **Gold / expected behavior (post-run audit only):** All five use Neyman orthogonal scores, so the design focuses on cross-fitting's effect on overfitting during nuisance estimation.
- **Agent status:** `answered`
- **Agent answer:** Because the IV estimators all use Neyman-orthogonal scores, differences in their performance can be attributed to whether cross-fitting reduces overfitting bias, rather than to differences in score orthogonality. [4196f4c01d9f15d9a55e56eb873f055f | page 24]
- **Citation IDs:** `4196f4c01d9f15d9a55e56eb873f055f`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1169, output=270, total=1439
- **Latency / estimated cost:** 3830.044 ms / $0.0002519
- **Original trace:** `results/agent/test/dense_traces.jsonl:5`

### Cited passages

**`4196f4c01d9f15d9a55e56eb873f055f` · rank 3 · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

### Final context

**Rank 1 · `716c1388156f01f96544338c5d9cac9c` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4 Two Simulation Illustrations

This section employs two simulation exercises to illustrate the consequences of relying on non-Neyman orthogonal scores and of failing to perform cross-fitting when using flexible nuisance estimators such as ML methods. We discuss two simulations to underscore that bias dominates in some contexts, while regularization bias prevails in others The first simulation focuses on the role of cross-fitting in the linear IV setting with many instruments. This problem has been thoroughly studied since the mid-1990s (e.g., Bekker, 1994). One of the recommendations to emerge from this literature is to use sample-splitting to reduce overfitting bias (often termed “many instruments bias” in this context). Our simulation revisits this classical many instrument setup by comparing linear IV estimation with ML-based IV estimation.

**Rank 2 · `6ea26237b7c6d8e36399908d23308cd7` · page 26 · https://arxiv.org/pdf/2504.08324v2**

Figure 1: Histograms of IV Coefficient Estimates Notes. Each panel compares simulation performance of a feasible IV estimator (orange) to the infeasible oracle IV estimator (blue). relying on cross-fitting. As a result, their 95% confidence intervals exhibit zero coverage acrossthe1000simulationreplications. Incontrast, theestimatorswithcross-fitting, SSIV and DML with Boosted Trees, perform substantially better. They have relatively small bias and produce coverage near the nominal 95% level. Compared to the infeasible oracle IV, they exhibit a visually larger spread, but are also approximately centered around zero. Importantly, we observe a meaningful difference between the two cross-fitted estimators. DML with Boosted Trees outperforms SSIV, reflecting the advantage of using a more flexible and regularized first-stage learner in this context.

**Rank 3 · `4196f4c01d9f15d9a55e56eb873f055f` · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q23

- **Type:** insufficient evidence
- **Question:** What acceptance rate at NeurIPS 2025 does the paper report for this work?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1262, output=85, total=1347
- **Latency / estimated cost:** 3183.584 ms / $0.0001687
- **Original trace:** `results/agent/test/dense_traces.jsonl:6`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `4b9d087ebacbb35e56c86a71b5c45ac7` · page 38 · https://arxiv.org/pdf/2504.08324v2**

Angrist and Frandsen (2022), and Bach et al. (2024) for related discussions. A convenient byproduct of cross-fitting is evidence about the out-of-sample performance of nuisance estimators. To provide guidance on the choice of nuisance estimator, we first consider the estimated out-of-sampleR2 values calculated using the cross-fitted predicted values and provided in the same table. These values indicate substantial variation across learner specifications.XGBoost (columns 7-9) achievesR2 scores of around 85% and 74% for predicting outcome and treatment, respectively, whereas other learners perform markedly worse. The XGBoost-based estimates imply a labor supply elasticity between 0.040 and 0.061 (s.e.≈ 0.022). By contrast, the neural networks achieve outcome R2 values below 4% and treatmentR2 values below 22%, and their corresponding point estimates display considerable instability.

**Rank 2 · `c0a7fc53d8f2355e14250c156f3c994b` · page 2 · https://arxiv.org/pdf/2504.08324v2**

Their target parameter is the regression coefficient θ0, which they interpret as a measure of the negative labor supply elasticity. In this example,g0(·) is a nuisance function. We are not primarily interested in how task features, outside of reward, relate to the outcome. However, Dube et al. (2020) emphasize that task heterogeneity needs to be accounted for to meaningfully interpretθ0. If g0(·) were known, estimation ofθ0 could proceed by regressingY−g0(X) onto D, which is equivalent to estimation based on the moment condition E[m(W ;θ0,g 0)] = E[(Y−g0(X)−Dθ0)D] = 0 whereW = (Y,D,X )denoteobservedrandom variables. Ofcourse, g0(·)willtypicallynot be known. A common strategy to simplify the problem is toassume that g0(X) = X′β0 with unknown coefficientβ0, in which case the model reduces to the familiar multiple regression model.

**Rank 3 · `046f7963dd755241cec1598e4ef6bd7c` · page 27 · https://arxiv.org/pdf/2504.08324v2**

The most striking 13Specifically, we estimate the probability of 401(k) eligibility given covariates,r0(X) = P(D = 1|X), andtheconditionalmeanoffinancialassetsgiventreatmentandcovariates, l0(D,X ) = E[Y |D,X ], using randomforeststrainedonthefullsample(1,000treesandminimumnodesize10). Weestimatetreatmentspecific residual variances,σ2d, as the sample variance ofyi−ˆl(di,xi) within treatment groups. In each simulation replication, we drawdi,s∼ Bernoulli(ˆr(xi)) and generate outcomes asyi,s =ˆl(di,s,xi) +εi,s, where εi,s∼N(0,ˆσ2di,s). 27

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/dense · q24

- **Type:** insufficient evidence
- **Question:** Which exact Python package version do the authors require to reproduce every experiment?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1138, output=46, total=1184
- **Latency / estimated cost:** 5626.228 ms / $0.0001368
- **Original trace:** `results/agent/test/dense_traces.jsonl:7`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `d6621fc9e296e91428122e40a45fae83` · page 41 · https://arxiv.org/pdf/2504.08324v2**

learners. We encourage researchers to report their candidate learners, tuning procedures, and diagnostic metrics to promote transparency and replicability. Challenges and Caveats While DML is conceptually straightforward, its practical implementation can be challenging, and results can be highly sensitive to implementation choices. Decisions such as how nuisance functions are estimated, how many folds are used, how often cross-fitting is repeated, and how tuning parameters are selected can materially affect empirical results. Developing a deeper understanding of the finite-sample behavior of DML—including tradeoffs in learner complexity, computational complexity, fold count, and cross-fitting repetition—would be valuable not just for refining our theoretical knowledge but for guiding applied practice.

**Rank 2 · `51890e944df34dd372bb088a6dcf6c19` · page 41 · https://arxiv.org/pdf/2504.08324v2**

Further work establishing combinations of data-generating processes, learners, and tuning strategies that provide rates of convergence compatible with the sufficient conditions for DML is important for clarifying when, where, and how different learners should be used. Convergence rate conditions may also fail in settings where nuisance functions are highly complex or non-smooth. Extending DML to better handle such settings is an important direction in current research; see, for example, Robins et al. (2017), Bradic et al. (2022), and Zheng, Bonvini, and Guo (2025). Relatedly, the literature on sensitivity analysis in DML settings (e.g., Chernozhukov et al., 2024) develops tools that, while motivated by concerns about unobserved confounding, are applicable more broadly.

**Rank 3 · `55b82572cbcd719c0d3c6928ea2a1539` · page 16 · https://arxiv.org/pdf/2504.08324v2**

particular, many theoretical guarantees do not apply to off-the-shelf implementations with default tuning choices. For tree-based methods, available analyses show that, absent specific tree depth and subsampling choices, pointwise polynomial convergence rates may fail or that estimators may even be pointwise inconsistent, with only slowL2 consistency established in high-dimensional settings (e.g., Chi et al., 2022; Cattaneo, Klusowski, and Yu, 2025). More broadly, if the nuisance functionη0 is fully nonparametric and highdimensional without additional simplifying structure, no known method is able to attain the n−1/4 rate required for standard DML asymptotics. In applications, it is often unclear which assumptions are credible and which estimator is appropriate, making it difficult to judge whether the required convergence conditions plausibly hold.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q16

- **Type:** answerable
- **Question:** In Section 7, what conventional values of K are reported to work well in many simulation settings?
- **Gold / expected behavior (post-run audit only):** Five or ten folds.
- **Agent status:** `answered`
- **Agent answer:** Section 7 reports that conventional choices of \(K=5\) or \(K=10\) work well in many simulation settings. [ce0411f70dd2ee464ccbf2358eddf7ab | page 40]
- **Citation IDs:** `ce0411f70dd2ee464ccbf2358eddf7ab`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1279, output=96, total=1375
- **Latency / estimated cost:** 3612.173 ms / $0.0001759
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:1`

### Cited passages

**`ce0411f70dd2ee464ccbf2358eddf7ab` · rank 1 · page 40 · https://arxiv.org/pdf/2504.08324v2**

These results suggest the use of relatively small values forK, but do not provide more specific guidance. Velez (2024) provides a higher-order analysis within a restricted class of nuisance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational resources. When the sample size is very small, larger values ofK may be desirable, and if resources permit, sensitivity analysis toK is worthwhile.

### Final context

**Rank 1 · `ce0411f70dd2ee464ccbf2358eddf7ab` · page 40 · https://arxiv.org/pdf/2504.08324v2**

These results suggest the use of relatively small values forK, but do not provide more specific guidance. Velez (2024) provides a higher-order analysis within a restricted class of nuisance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational resources. When the sample size is very small, larger values ofK may be desirable, and if resources permit, sensitivity analysis toK is worthwhile.

**Rank 2 · `00179456a14aa5a51f9f6f107ae6ec73` · page 22 · https://arxiv.org/pdf/2504.08324v2**

(2018) provide conditions that allow researchers to make valid inferential statements aboutθ0 using the DML estimatorˆθDML. These conditions involve conventional sampling and regularity conditions along with the assumption that the nuisance parameter estimator,ˆη, converges sufficiently quickly, as discussed in Section 2.2. Under these assumptions, the DML estimator is asymptotically normal: √nˆΣ−1/2(ˆθDML−θ0) d→N (0, I), where ˆΣ =ˆJ−1   1 n K∑ k=1 ∑ i∈Ik m(Wi;ˆθDML,ˆη−k)m(Wi;ˆθDML,ˆη−k)⊤   ˆJ−1⊤, ˆJ = 1n K∑k=1∑i∈Ik ∂∂θ{m(Wi;θ,ˆη−k)}⏐⏐⏐θ=ˆθDM L. (19) Standard errors forˆθ are thus given by square-roots of the diagonal values ofˆΣ/n. A key practical implication of using both Neyman orthogonal scores and cross-fitting is that standard errors for ˆθDML can be computed as if the nuisance functions were known.

**Rank 3 · `716c1388156f01f96544338c5d9cac9c` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4 Two Simulation Illustrations

This section employs two simulation exercises to illustrate the consequences of relying on non-Neyman orthogonal scores and of failing to perform cross-fitting when using flexible nuisance estimators such as ML methods. We discuss two simulations to underscore that bias dominates in some contexts, while regularization bias prevails in others The first simulation focuses on the role of cross-fitting in the linear IV setting with many instruments. This problem has been thoroughly studied since the mid-1990s (e.g., Bekker, 1994). One of the recommendations to emerge from this literature is to use sample-splitting to reduce overfitting bias (often termed “many instruments bias” in this context). Our simulation revisits this classical many instrument setup by comparing linear IV estimation with ML-based IV estimation.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q17

- **Type:** answerable
- **Question:** When the best nuisance learner is unknown in advance, what candidate-method strategy is recommended?
- **Gold / expected behavior (post-run audit only):** Consider a diverse set including parametric benchmarks, regularized regression, tree-based models, and neural networks.
- **Agent status:** `answered`
- **Agent answer:** Use a diverse set of candidate nuisance learners rather than assuming one will be best: include parametric benchmarks (such as linear or logistic regression), regularized regression, tree-based models, and neural networks. If they yield similar estimates, that supports confidence; substantial differences call for caution and further investigation. [e71da72d3dc715d32a990782360e3dd3 | page 40]
- **Citation IDs:** `e71da72d3dc715d32a990782360e3dd3`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1133, output=127, total=1260
- **Latency / estimated cost:** 4158.968 ms / $0.0001768
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:2`

### Cited passages

**`e71da72d3dc715d32a990782360e3dd3` · rank 1 · page 40 · https://arxiv.org/pdf/2504.08324v2**

Because it is rarely clearex antewhich learner will perform best in a given application, we recommend considering a diverse set of candidate methods, including parametric benchmarks (e.g., linear or logistic regression), regularized regression, tree-based models, and neural networks. From a practical perspective, greater confidence in DML results is warranted when different learners deliver similar estimates, while substantial divergence across learners should be viewed as a warning sign that calls for caution and further investigation. We illustrated how predictive diagnostics, which are a natural byproduct of cross-fitting, can help identify potentially problematic 40

### Final context

**Rank 1 · `e71da72d3dc715d32a990782360e3dd3` · page 40 · https://arxiv.org/pdf/2504.08324v2**

Because it is rarely clearex antewhich learner will perform best in a given application, we recommend considering a diverse set of candidate methods, including parametric benchmarks (e.g., linear or logistic regression), regularized regression, tree-based models, and neural networks. From a practical perspective, greater confidence in DML results is warranted when different learners deliver similar estimates, while substantial divergence across learners should be viewed as a warning sign that calls for caution and further investigation. We illustrated how predictive diagnostics, which are a natural byproduct of cross-fitting, can help identify potentially problematic 40

**Rank 2 · `cfe19ed7d9241560249490980c989653` · page 39 · https://arxiv.org/pdf/2504.08324v2**

equation, or by assigning equal weights to all learnersforwhichtheCVC p-valuesarelargerthan0.2. Weuse K = 3 cross-fittingfolds, implementedbyrandomlyassigning recruiters to folds, and report median aggregated estimates obtained usingS = 5 cross-fitting repetitions. Standard errors are clustered at the recruiter level. The results in this application highlight that DML estimates can be sensitive to the choiceofnuisanceestimator. ThissensitivityisconsistentwithconditionsinexistingDML theory, which indicate that poorly tuned or ill-suited learners can yield misleading results. We emphasize that the choice of which learner to use for a particular nuisance function and data set is rarely, if ever, knownex ante. Further, there is no reason to assume that the same learner is best for every nuisance function, although this is implicitly imposed by many common estimation strategies.

**Rank 3 · `9fca0d4987e8fb014d55889b7dfdfd13` · page 35 · https://arxiv.org/pdf/2504.08324v2**

For example, using random forests with higher regularization (minimum node size of 100) yields a first-period treatment effect estimate of 2903 (s.e. = 497), while lower regularization (minimum node size of 1) yields 2666 (s.e. = 571). Pre-treatment effects remain statistically insignificant at the 5% level across all learner and tuning parameter choices considered. The robustness to learner choice is quite different in the example we consider in next section. There we revisit the study on monopsony power of Dube et al. (2020) and illustratethattheselectionandtuningofnuisanceestimatorscanbeempiricallyconsequential. We use this application to demonstrate diagnostic analyses that can assist in evaluating and selecting nuisance estimators.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q18

- **Type:** answerable
- **Question:** In Section 2.3.2, why is a fold-specific nuisance estimate independent of observations in the held-out fold?
- **Gold / expected behavior (post-run audit only):** Because it is trained only on observations outside that fold.
- **Agent status:** `answered`
- **Agent answer:** Because the sample consists of independent observations and cross-fitting splits it into separate folds: the nuisance estimate is fitted using one fold, while the held-out fold is used to evaluate the score. Since the held-out observations were not used to fit that estimate, the estimate is independent of them under the sample-independence assumption. [46b3d3c66f0f888a2ab9bfced5cddb51 | page 20]
- **Citation IDs:** `46b3d3c66f0f888a2ab9bfced5cddb51`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1234, output=208, total=1442
- **Latency / estimated cost:** 3720.545 ms / $0.0002274
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:3`

### Cited passages

**`46b3d3c66f0f888a2ab9bfced5cddb51` · rank 1 · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

### Final context

**Rank 1 · `46b3d3c66f0f888a2ab9bfced5cddb51` · page 20 · https://arxiv.org/pdf/2504.08324v2**

To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, independence betweenˆη−η0 and ∂∂ηm(Wi;θ0,η 0) would follow by construction. With a single sample of independent observations, we can mimic this logic by randomly splitting the sample into two partitions, or “folds,” using one fold to estimateˆη and the other to evaluate the score function and estimateθ0. Of course, such an approach inefficiently uses the available data because bothη0 and θ0 are estimated using only subsets of the data.

**Rank 2 · `acdd8fc9e3a5cd0ea3fab7d797f387e0` · page 15 · https://arxiv.org/pdf/2504.08324v2**

Our usage emphasizes that overfitting in nuisance estimation can lead to bias in target parameter estimation, because it inflates the dependence between nuisance estimation error and the data. The second key ingredient of DML—cross-fitting, also discussed in Section 2.3— addresses overfitting bias by using sample splitting to ensure (approximate) independence between the estimation error in the nuisance function and the observations used in the sample moment condition. This independence implies that the product in the numerator of (⋆) is mean zero whenever either term is mean zero. The two main ingredients of DML, discussed in Section 2.3, are meant to alleviate the first-order impact of nuisance estimation. Estimation of nuisance parameters also generally affects the target parameter through the “higher order terms” in (14).

**Rank 3 · `38c4fae73d63d31b8ef6bb74f20aea60` · page 20 · https://arxiv.org/pdf/2504.08324v2**

2.3.2 Cross-fitting

Overfitting bias arises due to statistical dependence between the error in the nuisance parameter estimator and the data used in constructing the plug-in estimator. As discussed above, ignoring the first-step estimation of ˆη is justified only if the term (⋆) in (14) is asymptotically negligible. In the previous section, we outlined an argument for this term vanishing that depends on Neyman orthogonalityand independence between the estimation error in the nuisance function,ˆη−η0, and the data used to construct the sample moment condition{Wi}ni=1. If ˆη is constructed using these same observations, the independence assumption will be violated. More generally, Neyman orthogonality alone is not sufficient to guarantee that first-step estimation of nuisance parameters can be ignored in inference about low-dimensional target parameters.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q19

- **Type:** answerable
- **Question:** What convergence caveat is reported for deep regression trees in the DML discussion?
- **Gold / expected behavior (post-run audit only):** They may fail to be pointwise consistent.
- **Agent status:** `answered`
- **Agent answer:** The DML discussion notes that deep regression trees may fail to be pointwise consistent, so they may not achieve the convergence needed for DML inference. [3b58ae351244c5e0cf3afdcc0da7a3b2 | page 41]
- **Citation IDs:** `3b58ae351244c5e0cf3afdcc0da7a3b2`
- **Context contains strict gold evidence:** `True` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1180, output=100, total=1280
- **Latency / estimated cost:** 3814.538 ms / $0.0001680
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:4`

### Cited passages

**`3b58ae351244c5e0cf3afdcc0da7a3b2` · rank 2 · page 41 · https://arxiv.org/pdf/2504.08324v2**

From a theoretical standpoint, part of DML’s appeal is that it delivers asymptotically normal inference even when flexible methods are used to estimate nuisance functions. Crucially, provided the nuisance estimator converges sufficiently quickly, the limiting distribution does not depend on the specific choice of nuisance estimator. Of course, it is unrealistic to expect all nuisance estimators to yield sufficiently accurate estimates in all settings. Many modern algorithms do not have theory establishing sufficiently fast rates without strong assumptions. For example, the results in Chi et al. (2022) suggest that random forests, when applied to high-dimensional data with tuning similar to common defaults, may fail to converge quickly enough for DML, and results in Cattaneo, Klusowski, and Yu (2025) establish that deep regression trees may fail to be pointwise consistent.

### Final context

**Rank 1 · `51890e944df34dd372bb088a6dcf6c19` · page 41 · https://arxiv.org/pdf/2504.08324v2**

Further work establishing combinations of data-generating processes, learners, and tuning strategies that provide rates of convergence compatible with the sufficient conditions for DML is important for clarifying when, where, and how different learners should be used. Convergence rate conditions may also fail in settings where nuisance functions are highly complex or non-smooth. Extending DML to better handle such settings is an important direction in current research; see, for example, Robins et al. (2017), Bradic et al. (2022), and Zheng, Bonvini, and Guo (2025). Relatedly, the literature on sensitivity analysis in DML settings (e.g., Chernozhukov et al., 2024) develops tools that, while motivated by concerns about unobserved confounding, are applicable more broadly.

**Rank 2 · `3b58ae351244c5e0cf3afdcc0da7a3b2` · page 41 · https://arxiv.org/pdf/2504.08324v2**

From a theoretical standpoint, part of DML’s appeal is that it delivers asymptotically normal inference even when flexible methods are used to estimate nuisance functions. Crucially, provided the nuisance estimator converges sufficiently quickly, the limiting distribution does not depend on the specific choice of nuisance estimator. Of course, it is unrealistic to expect all nuisance estimators to yield sufficiently accurate estimates in all settings. Many modern algorithms do not have theory establishing sufficiently fast rates without strong assumptions. For example, the results in Chi et al. (2022) suggest that random forests, when applied to high-dimensional data with tuning similar to common defaults, may fail to converge quickly enough for DML, and results in Cattaneo, Klusowski, and Yu (2025) establish that deep regression trees may fail to be pointwise consistent.

**Rank 3 · `55b82572cbcd719c0d3c6928ea2a1539` · page 16 · https://arxiv.org/pdf/2504.08324v2**

particular, many theoretical guarantees do not apply to off-the-shelf implementations with default tuning choices. For tree-based methods, available analyses show that, absent specific tree depth and subsampling choices, pointwise polynomial convergence rates may fail or that estimators may even be pointwise inconsistent, with only slowL2 consistency established in high-dimensional settings (e.g., Chi et al., 2022; Cattaneo, Klusowski, and Yu, 2025). More broadly, if the nuisance functionη0 is fully nonparametric and highdimensional without additional simplifying structure, no known method is able to attain the n−1/4 rate required for standard DML asymptotics. In applications, it is often unclear which assumptions are credible and which estimator is appropriate, making it difficult to judge whether the required convergence conditions plausibly hold.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q20

- **Type:** answerable
- **Question:** In the IV simulation, why are the five estimators described as isolating the impact of cross-fitting?
- **Gold / expected behavior (post-run audit only):** All five use Neyman orthogonal scores, so the design focuses on cross-fitting's effect on overfitting during nuisance estimation.
- **Agent status:** `answered`
- **Agent answer:** Because all five estimators use Neyman-orthogonal scores, the comparison holds orthogonality constant and focuses on the effect of cross-fitting—specifically, whether it reduces overfitting bias. [4196f4c01d9f15d9a55e56eb873f055f | page 24]
- **Citation IDs:** `4196f4c01d9f15d9a55e56eb873f055f`
- **Context contains strict gold evidence:** `False` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `False`
- **Tool-call count:** 1
- **Usage:** input=1171, output=253, total=1424
- **Latency / estimated cost:** 3761.821 ms / $0.0002436
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:5`

### Cited passages

**`4196f4c01d9f15d9a55e56eb873f055f` · rank 2 · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

### Final context

**Rank 1 · `716c1388156f01f96544338c5d9cac9c` · page 24 · https://arxiv.org/pdf/2504.08324v2**

4 Two Simulation Illustrations

This section employs two simulation exercises to illustrate the consequences of relying on non-Neyman orthogonal scores and of failing to perform cross-fitting when using flexible nuisance estimators such as ML methods. We discuss two simulations to underscore that bias dominates in some contexts, while regularization bias prevails in others The first simulation focuses on the role of cross-fitting in the linear IV setting with many instruments. This problem has been thoroughly studied since the mid-1990s (e.g., Bekker, 1994). One of the recommendations to emerge from this literature is to use sample-splitting to reduce overfitting bias (often termed “many instruments bias” in this context). Our simulation revisits this classical many instrument setup by comparing linear IV estimation with ML-based IV estimation.

**Rank 2 · `4196f4c01d9f15d9a55e56eb873f055f` · page 24 · https://arxiv.org/pdf/2504.08324v2**

As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimation of average treatment effects, where we emphasize the role of Neyman orthogonality in delivering valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

**Rank 3 · `6ea26237b7c6d8e36399908d23308cd7` · page 26 · https://arxiv.org/pdf/2504.08324v2**

Figure 1: Histograms of IV Coefficient Estimates Notes. Each panel compares simulation performance of a feasible IV estimator (orange) to the infeasible oracle IV estimator (blue). relying on cross-fitting. As a result, their 95% confidence intervals exhibit zero coverage acrossthe1000simulationreplications. Incontrast, theestimatorswithcross-fitting, SSIV and DML with Boosted Trees, perform substantially better. They have relatively small bias and produce coverage near the nominal 95% level. Compared to the infeasible oracle IV, they exhibit a visually larger spread, but are also approximately centered around zero. Importantly, we observe a meaningful difference between the two cross-fitted estimators. DML with Boosted Trees outperforms SSIV, reflecting the advantage of using a more flexible and regularized first-stage learner in this context.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q23

- **Type:** insufficient evidence
- **Question:** What acceptance rate at NeurIPS 2025 does the paper report for this work?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1217, output=58, total=1275
- **Latency / estimated cost:** 4513.009 ms / $0.0001507
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:6`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `4b9d087ebacbb35e56c86a71b5c45ac7` · page 38 · https://arxiv.org/pdf/2504.08324v2**

Angrist and Frandsen (2022), and Bach et al. (2024) for related discussions. A convenient byproduct of cross-fitting is evidence about the out-of-sample performance of nuisance estimators. To provide guidance on the choice of nuisance estimator, we first consider the estimated out-of-sampleR2 values calculated using the cross-fitted predicted values and provided in the same table. These values indicate substantial variation across learner specifications.XGBoost (columns 7-9) achievesR2 scores of around 85% and 74% for predicting outcome and treatment, respectively, whereas other learners perform markedly worse. The XGBoost-based estimates imply a labor supply elasticity between 0.040 and 0.061 (s.e.≈ 0.022). By contrast, the neural networks achieve outcome R2 values below 4% and treatmentR2 values below 22%, and their corresponding point estimates display considerable instability.

**Rank 2 · `51890e944df34dd372bb088a6dcf6c19` · page 41 · https://arxiv.org/pdf/2504.08324v2**

Further work establishing combinations of data-generating processes, learners, and tuning strategies that provide rates of convergence compatible with the sufficient conditions for DML is important for clarifying when, where, and how different learners should be used. Convergence rate conditions may also fail in settings where nuisance functions are highly complex or non-smooth. Extending DML to better handle such settings is an important direction in current research; see, for example, Robins et al. (2017), Bradic et al. (2022), and Zheng, Bonvini, and Guo (2025). Relatedly, the literature on sensitivity analysis in DML settings (e.g., Chernozhukov et al., 2024) develops tools that, while motivated by concerns about unobserved confounding, are applicable more broadly.

**Rank 3 · `5b78c9908c7c853931d8c6ec67e2e6db` · page 42 · https://arxiv.org/pdf/2504.08324v2**

data in economic applications, further development of practical diagnostics and implementation guidance tailored to this setting would be a welcome addition to the literature. Functional Restrictions. A recent proposal for improving performance involves empirical calibration of nuisance function estimates, as developed by van der Laan, Luedtke, and Carone (2025). Their approach adapts ideas from predictive modeling, requiring that estimated nuisance functions satisfy known properties. For example, if the nuisance function isη0(X) = E[Y|X], we should not be able to improve mean squared prediction error by transformingη0(X). van der Laan, Luedtke, and Carone (2025) propose methods to enforce such calibration and show that, for a broad class of target parameters, DML estimators remain asymptotically normal even if only one nuisance estimator satisfies the usual convergence rate.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

## test/hybrid · q24

- **Type:** insufficient evidence
- **Question:** Which exact Python package version do the authors require to reproduce every experiment?
- **Gold / expected behavior (post-run audit only):** Search and abstain if evidence is insufficient.
- **Agent status:** `abstain`
- **Agent answer:** The available evidence is insufficient to answer this question.
- **Citation IDs:** none
- **Context contains strict gold evidence:** `None` (mechanical retrieval check)
- **Citation syntax/in-context check:** `True`
- **Raw abstention detected:** `True`
- **Tool-call count:** 1
- **Usage:** input=1206, output=47, total=1253
- **Latency / estimated cost:** 3078.568 ms / $0.0001441
- **Original trace:** `results/agent/test/hybrid_traces.jsonl:7`

### Cited passages

No citations emitted.

### Final context

**Rank 1 · `55b82572cbcd719c0d3c6928ea2a1539` · page 16 · https://arxiv.org/pdf/2504.08324v2**

particular, many theoretical guarantees do not apply to off-the-shelf implementations with default tuning choices. For tree-based methods, available analyses show that, absent specific tree depth and subsampling choices, pointwise polynomial convergence rates may fail or that estimators may even be pointwise inconsistent, with only slowL2 consistency established in high-dimensional settings (e.g., Chi et al., 2022; Cattaneo, Klusowski, and Yu, 2025). More broadly, if the nuisance functionη0 is fully nonparametric and highdimensional without additional simplifying structure, no known method is able to attain the n−1/4 rate required for standard DML asymptotics. In applications, it is often unclear which assumptions are credible and which estimator is appropriate, making it difficult to judge whether the required convergence conditions plausibly hold.

**Rank 2 · `cfe19ed7d9241560249490980c989653` · page 39 · https://arxiv.org/pdf/2504.08324v2**

equation, or by assigning equal weights to all learnersforwhichtheCVC p-valuesarelargerthan0.2. Weuse K = 3 cross-fittingfolds, implementedbyrandomlyassigning recruiters to folds, and report median aggregated estimates obtained usingS = 5 cross-fitting repetitions. Standard errors are clustered at the recruiter level. The results in this application highlight that DML estimates can be sensitive to the choiceofnuisanceestimator. ThissensitivityisconsistentwithconditionsinexistingDML theory, which indicate that poorly tuned or ill-suited learners can yield misleading results. We emphasize that the choice of which learner to use for a particular nuisance function and data set is rarely, if ever, knownex ante. Further, there is no reason to assume that the same learner is best for every nuisance function, although this is implicitly imposed by many common estimation strategies.

**Rank 3 · `a1b3a5c7ca75cea978cdfddf08d10a18` · page 20 · https://arxiv.org/pdf/2504.08324v2**

Cross-fitting restores asymptotic efficiency by rotating which folds are used for each task, so all observations contribute to both steps. The cross-fit version of the plug-in estimator with a generic score defined in (13) is ˆθ×-fit : 1n K∑k=1∑i∈Ikm(Wi;ˆθ×-fit,ˆη−k) = 0. (17) Here,{Ik}Kk=1 is a random partition of the sample of units{1,...,n } intoK subsamples of approximately equal size, and ˆη−k denotes a first-step nuisance parameter estimate constructed using only observationsexcluding those in the subsampleIk. Because ˆη−k uses only observationsnot in subsamplek, the estimation error inˆη−k is independent of observations in subsamplek, which alleviates overfitting bias.

### Student fields

- `answer_grade_0_1_2: ____`
- `citation_semantic_support: ____`
- `abstention_correct: ____`
- `reviewer_reason: ____`

