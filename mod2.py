from  scipy.stats import norm

distr = norm(1000, 5)
d = distr.cdf(1070) - distr.cdf(1005)
print(f'доля промаха {d}')