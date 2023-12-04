#!/usr/bin/python3
""" This module contains ``matrix_mul`` function """


def matrix_mul(m_a, m_b):
    out = []
    product = 0

    # [1, 2]
    # [3, 4]
           # [1, 2]
           # [3, 4]
    for r in range(len(m_a)):
        for e in range(len(m_a[r])):
            product += m_a[r][e] * m_b[e][r]
        out.append([product])
        product = 0
    return out
