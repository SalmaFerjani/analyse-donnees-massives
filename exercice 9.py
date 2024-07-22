# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:31:07 2023

@author: Salma
"""

import numpy as np
def random_mat(N):
    X = np.random.normal(5, 5, N)
    Y = 2 * X
    M = np.column_stack((X, Y))
    return M
def build_m(M, N, n=20):
    for _ in range(n):
        i = np.random.randint(N)
        j = np.random.randint(N)
        if i < N and j < M.shape[1]:
           M[i, j] = np.nan
    return M


