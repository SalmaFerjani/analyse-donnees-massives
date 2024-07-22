# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:38:29 2023

@author: Salma
"""

import numpy as np
def mad(M, axis=None):
    median_M = np.median(M, axis=axis)
    abs_diff = np.abs(M - median_M)
    mad_value = np.median(abs_diff, axis=axis)
    return mad_value

