import unittest
import pytest

from rotate_matrix.rotate import rotate


class RotateMatrix(unittest.TestCase):

    def test_rotate_matrix_2x2(self):
        matrix = [[1, 2], [3, 4]]
        expected_matrix = [[2, 4], [1, 3]]
        rotated_matrix = rotate(matrix)
        self.assertEquals(expected_matrix, rotated_matrix)

    def test_rotate_4x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected_matrix = [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
        rotated_matrix = rotate(matrix)
        self.assertEquals(expected_matrix, rotated_matrix)

    @pytest.mark.skip(reason="Doesn't works for non-square matrix")
    def test_rotate_2x3(self):
        matrix = [[1, 2, 3], [5, 6, 7]]
        expected_matrix = [[3, 5], [2, 6], [1, 7]]
        rotated_matrix = rotate(matrix)
        self.assertEquals(expected_matrix, rotated_matrix)
