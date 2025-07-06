import numpy as np
from scipy.stats import multivariate_normal

def bayes_classifier(x, means, covs, priors):
    posteriors = []
    for mean, cov, prior in zip(means, covs, priors):
        likelihood = multivariate_normal.pdf(x, mean=mean, cov=cov)
        posteriors.append(likelihood * prior)
    return np.argmax(posteriors)

# Example usage
means = [np.array([1, 2]), np.array([5, 6])]
covs = [np.eye(2), np.eye(2)]
priors = [0.5, 0.5]
x = np.array([3, 4])
label = bayes_classifier(x, means, covs, priors)
print("Class:", label)
