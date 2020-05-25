import numpy as np

def anti_diagonal(a: np.ndarray) -> int:
    a1 = a[:, ::-1].diagonal()
    return a[a > a1[a1 > 0].mean()].size
