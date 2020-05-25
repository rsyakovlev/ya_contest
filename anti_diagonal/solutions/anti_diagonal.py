import numpy as np

def anti_diagonal(a: np.ndarray) -> int:
    a1 = a[:, ::-1].diagonal()
    a2 = a1[a1 > 0].mean()
    return a[a > a2].size
