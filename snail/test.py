import unittest
import copy
from snail import Snail


# Python3.8 tested
class SnailTest(unittest.TestCase):
    def test_solution_1_matrix_size_1(self):
        in_matrix = [[0]]
        snail = Snail()
        self.assertEqual(in_matrix, snail.solution_1(in_matrix))

    def test_solution_1_matrix_size_2(self):
        in_matrix = [
            [0, 1],
            [0, 1]
        ]
        out_matrix = [
            [0, 2],
            [0, 3]
        ]
        snail = Snail()
        self.assertEqual(out_matrix, snail.solution_1(in_matrix))

    def test_solution_1_matrix_size_3(self):
        in_matrix = [[x for x in range(0, 3)] for _ in range(3)]
        out_matrix = [
            [0, 2, 6],
            [0, 9, 8],
            [0, 6, 10]
        ]
        snail = Snail()
        self.assertEqual(out_matrix, snail.solution_1(in_matrix), f'in_matrix:{in_matrix}')

    def test_get_submatrix_without_perimeter_size_3(self):
        in_matrix = [[x for x in range(0, 3)] for _ in range(3)]
        out_matrix = [[1]]
        snail = Snail()
        self.assertEqual(out_matrix, snail._get_submatrix_without_perimeter(in_matrix))

    def test_update_submatrix_in_matrix_size_3_and_submatrix_size_1(self):
        out_matrix = [
            [0, 2, 6],
            [0, 9, 8],
            [0, 6, 10]
        ]
        in_matrix = copy.deepcopy(out_matrix)
        in_matrix[1][1] = 1
        in_submatrix = [[9]]
        snail = Snail()
        self.assertEqual(out_matrix, snail._update_submatrix_in_matrix(in_matrix, in_submatrix))


    def test_update_perimetr_with_matrix_size_1(self):
        in_matrix = [[1]]
        start_multiply = 2
        out_result = ([[2]], 3)
        snail = Snail()
        self.assertEqual(out_result, snail._update_perimeter(in_matrix, start_multiply))


if __name__ == '__main__':
    unittest.main()
