#!/usr/bin/python3

"""Module contains function that multiplies two matrices."""

import numpy


def lazy_matrix_mul(m_a, m_b):
	"""Returns multiplication of two matrices.

	Args:
	    m_a: First matrix
	    m_b: Second Matrix
	"""


	return (numpy.matmul(m_a, m_b))
