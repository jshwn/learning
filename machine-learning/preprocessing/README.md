#   Data Preprocessing

##  Problems with Data and Solutions
*   Incomplete: missing values
    *   Removing features(colums) or instances(rows) which miss values
    *   Imputation
        *   for univariate features
            *   mean imputation
            *   median imputation
            *   most frequent imputation
        *   for multivariate features
            *   get function from other features to target feature (maybe with regression)
*   Noisy: containing errors or outliers
*   Inconsistent: containing discrepancies

##  Estimator
여기서는 sklearn을 전제한다.

*   Transformer
    *   `.fit()`: 
    *   `.transform()`
*   Predictor

##  Handling categorical data
*   nomial feature
    *   one-hot encoding
        *   Multicollinearity Issue
        *   feature의 종류가 4개면, 종류별 column을 3개만 쓰는 것.
*   ordinal feature
*   class label

##  Feature Scaling
Scale Invariant한 학습 알고리즘(Decision Tree, Random Forest)에서는 불필요

*   Scaling
    *   min-max
    *   max-abs
    *   robust
*   Standardization
*   Normalization
    *   L1 Norm
    *   L2 Norm

##  Discretization
생략