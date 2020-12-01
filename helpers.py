import numpy as np 

def bootstrap(x, n_iterations = 10000, gamma = 0.95):
    """ Return a 'gamma' confidence interval for the mean of x by resampling it n_iterations times.
    
    Parameters
    ----------
		x: 1D array
			sequences of values to boostrap on
		n_iterations: int, optional
			number of bootstrapping iterations
		gamma: float in (0, 1), optional
			confidence level (e.g. 0.95 gives a 95% CI)
			
	Returns
	-------
		CI_low: float
			lower quantile of the CI
		CI_high: float
			upper quantile of the CI
    """
    
    x = np.array(x)
    N = len(x)
    q_high = (1+gamma)/2
    q_low = (1-gamma)/2
    
    sample_mean = np.empty(n_iterations)
    for i in range(n_iterations):
        sample = np.random.choice(x, N, replace = True)
        sample_mean[i] = np.mean(sample)
    
    CI_low, CI_high = np.quantile(sample_mean, [q_low, q_high])   
        
    return CI_low, CI_high

def mae(target, pred, start = None):
    if start is not None:
        target = target[start:]
        pred = pred[start:]
       
    return np.abs(target-pred).mean()