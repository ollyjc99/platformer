import numpy as np
import matplotlib.pyplot as plt


def main():
    N = 800

    mean = np.zeros(N)
    positions = np.expand_dims(np.arange(N), axis=1)
    horizontal_lengthscale, vertical_lengthscale = 50, 3
    cov_matrix = vertical_lengthscale*np.exp(-(positions.T-positions)**2/(2*horizontal_lengthscale**2))

    random_sample = np.random.multivariate_normal(mean, cov_matrix)
    print(type(random_sample))
    listl = list(random_sample)
    print(listl)
    plt.figure()
    plt.plot(random_sample)
    plt.show()


if __name__ == "__main__":
    main()
