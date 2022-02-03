import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# print(yes_hd, no_hd)

chol_hd = yes_hd.chol

mean_chol_hd = np.mean(chol_hd)
# mean chol from ppl with hd = ~251
print(mean_chol_hd)
# null hypothesis: People with hd have an avg chol = 240
# alt hypothesis: People with hd have avg chol > 240
tstat, pvalue = ttest_1samp(chol_hd, 240, alternative='greater')
# p-value of .00354 - reject null hypothesis
print(tstat, pvalue)

# hypothesis test for patients not diagnosed with hd
# null hyp: People w/o hd have avg chol = 240
# alt hyp: avg chol > 240
chol_no_hd = no_hd.chol
# pvalue = .26, do not reject null hypothesis
tstat, pvalue = ttest_1samp(chol_no_hd, 240, alternative='greater')
print(tstat, pvalue)