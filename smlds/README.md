# SMLDS – Dataset-wise runnable scripts

Each folder = one dataset. Each .py = the complete code of one experiment on that dataset (no cells, run top to bottom).

## Setup
```
pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels
```
Open a file in VS Code -> Run Python File. Plot windows open one at a time; close each to continue.
Iris/Titanic (seaborn) and California Housing need internet on first run.

## breast_cancer
- `breast_cancer/central_limit_theorem.py` – Central Limit Theorem
- `breast_cancer/classification_models.py` – Classification Models
- `breast_cancer/data_preprocessing.py` – Data Preprocessing
- `breast_cancer/decision_tree_random_forest.py` – Decision Tree & Random Forest
- `breast_cancer/exploratory_data_analysis.py` – Exploratory Data Analysis
- `breast_cancer/hypothesis_testing.py` – Hypothesis Testing (t-test, Chi-square, ANOVA)

## california_housing
- `california_housing/bootstrap_confidence.py` – Bootstrap Confidence Intervals & Permutation Test
- `california_housing/classification_models.py` – Classification Models
- `california_housing/linear_regression_diagnostics.py` – Linear Regression & Diagnostics
- `california_housing/mle_estimation.py` – Maximum Likelihood Estimation (MLE)
- `california_housing/ridge_lasso_elastic.py` – Ridge, Lasso & Elastic Net Regression

## iris
- `iris/bootstrap_confidence.py` – Bootstrap Confidence Intervals & Permutation Test
- `iris/central_limit_theorem.py` – Central Limit Theorem
- `iris/classification_models.py` – Classification Models
- `iris/decision_tree_random_forest.py` – Decision Tree & Random Forest
- `iris/hypothesis_testing.py` – Hypothesis Testing (t-test, Chi-square, ANOVA)
- `iris/linear_regression_diagnostics.py` – Linear Regression & Diagnostics
- `iris/mle_estimation.py` – Maximum Likelihood Estimation (MLE)
- `iris/pca_clustering.py` – PCA + Clustering
- `iris/ridge_lasso_elastic.py` – Ridge, Lasso & Elastic Net Regression
- `iris/sampling_methods.py` – Sampling Methods

## titanic
- `titanic/bootstrap_confidence.py` – Bootstrap Confidence Intervals & Permutation Test
- `titanic/decision_tree_random_forest.py` – Decision Tree & Random Forest
- `titanic/linear_regression_diagnostics.py` – Linear Regression & Diagnostics
- `titanic/mle_estimation.py` – Maximum Likelihood Estimation (MLE)
- `titanic/ridge_lasso_elastic.py` – Ridge, Lasso & Elastic Net Regression

