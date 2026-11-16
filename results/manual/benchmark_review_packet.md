# Manual benchmark review packet

> All automatic checks are mechanical. Every checkbox below is intentionally blank and requires student review.

## q01 — dev — answerable

- **Question:** In Section 2, what two essential components define Double/Debiased Machine Learning?
- **Gold answer:** Neyman orthogonality and cross-fitting.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 9
- **Gold chunk ID:** `19cea224507fdb1853fa43fc456ece5c`
- **Gold evidence:** This section describes the two essential components that define DML: Neyman orthogonality and cross-fitting.
- **Evidence context:**

> 2 Key Ingredients of DML  This section describes the two essential components that define DML: Neyman orthogonality and cross-fitting. Together, they help control the sensitivity of the target estimator to nuisance estimation, which can substantially improve both the reliability of point estimates and the quality…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q02 — dev — answerable

- **Question:** Within the semiparametric framework, what kind of object is the target parameter theta-zero?
- **Gold answer:** It is a low-dimensional parameter, such as an average treatment effect or a fixed vector of regression coefficients.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 9
- **Gold chunk ID:** `3fc918bfa4346bbf4d5a72f77e0f146a`
- **Gold evidence:** First, we have a target parameter of interest, θ0, which is low-dimensional; e.g.,θ0 may be an average treatment effect or a fixed vector of regression coefficients.
- **Evidence context:**

> 2.1 A Semiparametric Framework for DML  We frame our discussion of DML within a relatively general semiparametric framework. There are two key elements of the framework. First, we have a target parameter of interest, θ0, which is low-dimensional; e.g.,θ0 may be an average treatment effect or a fixed vector of regression coefficients. Second, we have a nuisance parameterη0 which may be high-dimensional and potentially complex. In many examples, η0 is a vector of conditional expectation functions, such as outcom…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q03 — dev — answerable

- **Question:** According to Section 2.3.1, how does Neyman orthogonality change sensitivity to small nuisance-parameter errors?
- **Gold answer:** Small nuisance perturbations do not create first-order changes in the moment function, reducing regularization bias.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 16
- **Gold chunk ID:** `90c3b5213c632d1e7a0b1b069959fc95`
- **Gold evidence:** small perturbations of the nuisance parameter away from the true value do not create first-order changes in the moment function.
- **Evidence context:**

> … localdeviationawayfromthetrue η0. Intuitively, (15)requiresthat, whenwemakeasmall move away fromη0 in any directionη−η0, the moment condition remains unchanged.10 In other words, small perturbations of the nuisance parameter away from the true value do not create first-order changes in the moment function.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q04 — dev — answerable

- **Question:** In Section 2.3.2, what is cross-fitting intended to reduce?
- **Gold answer:** It reduces dependence between first-step nuisance-estimation error and the data used to estimate the target parameter.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 20
- **Gold chunk ID:** `46b3d3c66f0f888a2ab9bfced5cddb51`
- **Gold evidence:** Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter.
- **Evidence context:**

> To address this issue, DML relies on a second key ingredient: cross-fitting. Cross-fitting is a form of repeated sample splitting intended to reduce the dependence between first-step estimation error and the data used to estimate the target parameter. Intuitively, if two independent datasets were available, one could be used to estimate the nuisance function ˆη and the other to estimateθ0 by plugging in ˆη. In that case, indepe…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q05 — dev — answerable

- **Question:** Why does rotating folds in cross-fitting avoid the efficiency loss of a simple one-time sample split?
- **Gold answer:** Rotation lets every observation contribute to nuisance estimation and target estimation across folds.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 20
- **Gold chunk ID:** `a1b3a5c7ca75cea978cdfddf08d10a18`
- **Gold evidence:** Cross-fitting restores asymptotic efficiency by rotating which folds are used for each task, so all observations contribute to both steps.
- **Evidence context:**

> Cross-fitting restores asymptotic efficiency by rotating which folds are used for each task, so all observations contribute to both steps. The cross-fit version of the plug-in estimator with a generic score defined in (13) is ˆθ×-fit : 1n K∑k=1∑i∈Ikm(Wi;ˆθ×-fit,ˆη−k) = 0. (17) Here,{Ik}Kk=1 is a random partition of t…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q06 — dev — answerable

- **Question:** What two ingredients are combined by the DML estimator defined in the estimation and inference section?
- **Gold answer:** Neyman orthogonal scores and cross-fitting.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 22
- **Gold chunk ID:** `0394cbc044adaf0319490b78f7cfa5e6`
- **Gold evidence:** a DML estimator is a plug-in estimator that combines both Neyman orthogonal scores and cross-fitting.
- **Evidence context:**

> …ensional target parameter θ0, which is defined by moment conditions (2) and depends on an unknown (potentially high-dimensional) nuisance parameterη0. Within this general setting, a DML estimator is a plug-in estimator that combines both Neyman orthogonal scores and cross-fitting. The DML estimator ofθ0 is then ˆθDML : 1n K∑k=1∑i∈Ikm(Wi;ˆθDML,ˆη−k) = 0, (18) where m is a Neyman orthogonal score (i.e., a score that satisfies (2) and (15)),{Ik}Kk=1 is a rando…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q07 — dev — answerable

- **Question:** In Section 3, what practical simplification applies when computing standard errors for the DML estimator?
- **Gold answer:** They can be computed as if the nuisance functions were known.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 22
- **Gold chunk ID:** `00179456a14aa5a51f9f6f107ae6ec73`
- **Gold evidence:** standard errors for ˆθDML can be computed as if the nuisance functions were known.
- **Evidence context:**

> …9) Standard errors forˆθ are thus given by square-roots of the diagonal values ofˆΣ/n. A key practical implication of using both Neyman orthogonal scores and cross-fitting is that standard errors for ˆθDML can be computed as if the nuisance functions were known.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q08 — dev — answerable

- **Question:** Why does the many-instrument IV simulation isolate overfitting rather than regularization bias?
- **Gold answer:** All compared IV approaches use Neyman orthogonal scores, leaving cross-fitting as the relevant difference.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 24
- **Gold chunk ID:** `4196f4c01d9f15d9a55e56eb873f055f`
- **Gold evidence:** As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting.
- **Evidence context:**

> As each of these approaches relies on Neyman orthogonal scores (see Example 3), the IV setting isolates the impact of overfitting. We show that cross-fitting alleviates overfitting bias and that using first stage estimators other than OLS can lead to efficiency gains. Our second example turns to the estimatio…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q09 — dev — answerable

- **Question:** How many instruments are generated in the paper's many-instrument simulation?
- **Gold answer:** Two hundred simulated instruments.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 24
- **Gold chunk ID:** `15a078cdc96d38c502da20e2aac41eac`
- **Gold evidence:** HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution.
- **Evidence context:**

> …s  We present simulation results from the canonical many-instrument linear IV model (see Example 3). We generate data asi.i.d. realizations from Y =θ0D +ε, D =g0(Z) +ν, (ε,ν )′⊥Z. HereZ arep = 200 simulated instruments,θ0 = 0 is the parameter of interest, and(ε,ν )′ are correlated error terms drawn from the normal distribution. We define the nuisance functionas g0(Z) =Z′π0, wherethefirstsixelementsof π0 aresetto0.1andtheremaining entries are set to 0. That is, only the first six instruments carry any sig…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q10 — dev — answerable

- **Question:** What combination produced reliable sampling behavior in the calibrated average-treatment-effect simulation?
- **Gold answer:** The combination of Neyman orthogonality and cross-fitting.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 24
- **Gold chunk ID:** `4196f4c01d9f15d9a55e56eb873f055f`
- **Gold evidence:** only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior
- **Evidence context:**

> …ing valid inference. Using a calibrated simulation, we compare estimators based on orthogonal and non-orthogonal scores, with and without cross-fitting. The results highlight that only the combination of orthogonality and cross-fitting yields estimators with reliable sampling behavior, thereby illustrating why these two ingredients are central to the DML framework.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q11 — dev — answerable

- **Question:** What was the size and wave range of the balanced HRS panel used in the hospitalization application?
- **Gold answer:** 656 households observed over waves 7 through 11.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 29
- **Gold chunk ID:** `aba1a68f17ebf1eebfedd4c86eaff838`
- **Gold evidence:** a balanced panel of 656 households observed over waves 7 through 11 of the HRS.
- **Evidence context:**

> … analysis by estimating dynamic effects using more flexible methods that allow for treatment effect heterogeneity. We use the same data as Sun and Abraham (2021), which consist of a balanced panel of 656 households observed over waves 7 through 11 of the HRS.15 We proceed in two steps. In Section 5.1, we estimate the change in out-of-pocket medical spending at time periodt caused by hospitalization at timeg for all potential pairs (t,g…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q12 — dev — answerable

- **Question:** What does repeating DML estimation help assess in the hospitalization example?
- **Gold answer:** It helps assess whether conclusions are robust to particular random sample splits.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 29
- **Gold chunk ID:** `875ff9f481bc4cae91e9ab5d6af07133`
- **Gold evidence:** simply repeating the DML estimation can help us gauge the robustness of conclusions to particular sample splits.
- **Evidence context:**

> …ation of DML in a canonical panel data setting, we further use this example to discuss the additional randomness introduced in DML due to the use of sample splitting. We show that simply repeating the DML estimation can help us gauge the robustness of conclusions to particular sample splits. We then outline the median aggregation approach presented in Chernozhukov et al. (2018) as a way to summarize results across repetitions. Our example builds on Dobkin et al. (2018…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q13 — dev — answerable

- **Question:** Which online labor platform is studied in the paper's monopsony application?
- **Gold answer:** Amazon MTurk.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 35
- **Gold chunk ID:** `c7a398e572f892c424d0b76ece0ed77a`
- **Gold evidence:** We revisit the Dube et al. (2020) paper on monopsony power on Amazon MTurk, an online platform for hiring workers to perform tasks.
- **Evidence context:**

> 6 Monopsony in Online Markets  We revisit the Dube et al. (2020) paper on monopsony power on Amazon MTurk, an online platform for hiring workers to perform tasks. The research falls into the wider literature estimating the labor supply elasticity (see reviews in Sokolova and Sorensen, 35

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q14 — dev — answerable

- **Question:** Which tools do the authors recommend for evaluating choices among nuisance-function estimators?
- **Gold answer:** Cross-fitted performance metrics such as R-squared, the CVC test, and model averaging.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 39
- **Gold chunk ID:** `20bcc1b0d7906926f811987d806147ea`
- **Gold evidence:** Appropriate tools for evaluating these choices include cross-fitted performance metrics such asR2, the CVC test, and model averaging approaches.
- **Evidence context:**

> In practice, we recommend using a diverse set of nuisance function estimators to increase the credibility of DML estimates. Appropriate tools for evaluating these choices include cross-fitted performance metrics such asR2, the CVC test, and model averaging approaches.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q15 — dev — answerable

- **Question:** What identification problem does DML not solve for a researcher?
- **Gold answer:** It does not choose interesting target parameters or identify them; careful substantive reasoning is still required.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 40
- **Gold chunk ID:** `e3bf4a09dd39a55429ff8f1a23d1db6d`
- **Gold evidence:** It does not tell the researcher what interesting target parameters are or how to identify them.
- **Evidence context:**

> While DML provides robustness to the estimation of nuisance parameters, it is not a panacea. It does not tell the researcher what interesting target parameters are or how to identify them. Rather, it complements careful reasoning about objects of interest and their identification. Implementation Guidance. When implementing DML, researchers face several design choice…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [ ] Question hợp lệ.
- [ ] Gold answer / expected abstention đúng.
- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q16 — test — answerable

- **Question:** In Section 7, what conventional values of K are reported to work well in many simulation settings?
- **Gold answer:** Five or ten folds.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 40
- **Gold chunk ID:** `ce0411f70dd2ee464ccbf2358eddf7ab`
- **Gold evidence:** conventional choices like K = 5 or 10 work well in many settings.
- **Evidence context:**

> …sance estimators and finds that performance improves with more folds, peaking atK = n but with diminishing returns. Simulation evidence, including that in Section 4, suggests that conventional choices like K = 5 or 10 work well in many settings. Given this evidence and that computational complexity is often a concern in applications of DML, we recommend choosing a simple round number informed by available computational re…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [ ] Gold answer / expected abstention đúng.
- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q17 — test — answerable

- **Question:** When the best nuisance learner is unknown in advance, what candidate-method strategy is recommended?
- **Gold answer:** Consider a diverse set including parametric benchmarks, regularized regression, tree-based models, and neural networks.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 40
- **Gold chunk ID:** `e71da72d3dc715d32a990782360e3dd3`
- **Gold evidence:** we recommend considering a diverse set of candidate methods, including parametric benchmarks (e.g., linear or logistic regression), regularized regression, tree-based models, and neural networks.
- **Evidence context:**

> Because it is rarely clearex antewhich learner will perform best in a given application, we recommend considering a diverse set of candidate methods, including parametric benchmarks (e.g., linear or logistic regression), regularized regression, tree-based models, and neural networks. From a practical perspective, greater confidence in DML results is warranted when different learners deliver similar estimates, while substantial divergence across learners should…

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [ ] Gold answer / expected abstention đúng.
- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [x] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q18 — test — answerable

- **Question:** In Section 2.3.2, why is a fold-specific nuisance estimate independent of observations in the held-out fold?
- **Gold answer:** Because it is trained only on observations outside that fold.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 20
- **Gold chunk ID:** `a1b3a5c7ca75cea978cdfddf08d10a18`
- **Gold evidence:** Because ˆη−k uses only observationsnot in subsamplek, the estimation error inˆη−k is independent of observations in subsamplek
- **Evidence context:**

> …,n } intoK subsamples of approximately equal size, and ˆη−k denotes a first-step nuisance parameter estimate constructed using only observationsexcluding those in the subsampleIk. Because ˆη−k uses only observationsnot in subsamplek, the estimation error inˆη−k is independent of observations in subsamplek, which alleviates overfitting bias.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [ ] Gold answer / expected abstention đúng.
- [ ] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q19 — test — answerable

- **Question:** What convergence caveat is reported for deep regression trees in the DML discussion?
- **Gold answer:** They may fail to be pointwise consistent.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 41
- **Gold chunk ID:** `3b58ae351244c5e0cf3afdcc0da7a3b2`
- **Gold evidence:** deep regression trees may fail to be pointwise consistent.
- **Evidence context:**

> …lied to high-dimensional data with tuning similar to common defaults, may fail to converge quickly enough for DML, and results in Cattaneo, Klusowski, and Yu (2025) establish that deep regression trees may fail to be pointwise consistent.

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q20 — test — answerable

- **Question:** In the IV simulation, why are the five estimators described as isolating the impact of cross-fitting?
- **Gold answer:** All five use Neyman orthogonal scores, so the design focuses on cross-fitting's effect on overfitting during nuisance estimation.
- **Source:** arxiv_2504_08324v2
- **Physical page:** 26
- **Gold chunk ID:** `55e21584ca54114035f78fa129dbb7c2`
- **Gold evidence:** all five estimators rely on Neyman orthogonal scores.
- **Evidence context:**

> …t highlights a broader point: the choice of learner can matter substantially in practice. We return to this theme in the empirical example in Section 6. Finally, we emphasize that all five estimators rely on Neyman orthogonal scores. As such, these simulations are designed to isolate the impact of cross-fitting in reducing the impact of overfitting during nuisance parameter estimation. In the next subsection, …

- **Automatic check:** `passed` — schema=true, manual_status_pending=true, gold_fields_present=true, source_exists=true, physical_page_valid=true, gold_chunk_ids_exist=true, evidence_in_declared_chunk_page=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q21 — dev — insufficient evidence

- **Question:** What numerical effect does the paper report for DML on Vietnam's GDP growth in 2025?
- **Expected behavior:** search and abstain when evidence remains insufficient.
- **Absence rationale:** The paper discusses econometric DML methods, not Vietnam GDP estimates.
- **Corpus check procedure:** Search all normalized pages for Vietnam, GDP, and growth; inspect any matches in context.
- **Source / page / gold chunk / evidence:** N/A by benchmark design.
- **Automatic check:** `passed` — schema=true, manual_status_pending=true, no_fake_gold_fields=true, expected_abstention_present=true

Student checklist:

- [x] Question hợp lệ.
- [ ] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q22 — dev — insufficient evidence

- **Question:** Which GPU model and training duration were used to train the DML method described in the paper?
- **Expected behavior:** search and abstain when evidence remains insufficient.
- **Absence rationale:** DML is an inference framework here, not a trained foundation model with a GPU training run.
- **Corpus check procedure:** Search all normalized pages for GPU, graphics processor, and training duration.
- **Source / page / gold chunk / evidence:** N/A by benchmark design.
- **Automatic check:** `passed` — schema=true, manual_status_pending=true, no_fake_gold_fields=true, expected_abstention_present=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q23 — test — insufficient evidence

- **Question:** What acceptance rate at NeurIPS 2025 does the paper report for this work?
- **Expected behavior:** search and abstain when evidence remains insufficient.
- **Absence rationale:** The source is an economics preprint and contains no NeurIPS acceptance-rate claim.
- **Corpus check procedure:** Search all normalized pages for NeurIPS, acceptance, and conference.
- **Source / page / gold chunk / evidence:** N/A by benchmark design.
- **Automatic check:** `passed` — schema=true, manual_status_pending=true, no_fake_gold_fields=true, expected_abstention_present=true

Student checklist:

- [ ] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [x] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

## q24 — test — insufficient evidence

- **Question:** Which exact Python package version do the authors require to reproduce every experiment?
- **Expected behavior:** search and abstain when evidence remains insufficient.
- **Absence rationale:** The paper mentions a companion website but does not mandate one exact package version for all experiments.
- **Corpus check procedure:** Search all normalized pages for Python, package, version, requirements, and reproduce.
- **Source / page / gold chunk / evidence:** N/A by benchmark design.
- **Automatic check:** `passed` — schema=true, manual_status_pending=true, no_fake_gold_fields=true, expected_abstention_present=true

Student checklist:

- [x] Question hợp lệ.
- [x] Gold answer / expected abstention đúng.
- [x] Evidence thực sự hỗ trợ hoặc absence check đủ thuyết phục.
- [ ] Source/page đúng.
- [ ] Không trùng hoặc rò rỉ dev/test.
- **Ghi chú:** ________________________________________________

