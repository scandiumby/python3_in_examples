import inspect


class Snail:
    def solution_1(self, matrix: list, start_multiply: int = 1) -> list:
        matrix, _ = self._update_perimeter(matrix, start_multiply)
        return matrix

    def _update_perimeter(self, matrix: list, start_multiply: int) -> tuple:
        matrix_size = len(matrix)
        if matrix_size == 1:
            return [[matrix[0][0] * start_multiply]], start_multiply + 1
        else:
            for i in range(matrix_size - 1):
                matrix[0][i] *= (start_multiply + i)  # update top matrix side
                matrix[i][-1] *= (start_multiply + matrix_size - 1 + i)  # update right matrix side
                matrix[-1][-1-i] *= (start_multiply + (matrix_size - 1) * 2 + i)  # update bottom matrix side
                matrix[i][0] *= (start_multiply + (matrix_size - 1) * 3 + i)  # update left matrix side
            submatrix = self._get_submatrix_without_perimeter(matrix)
            if submatrix:
                next_multiply = start_multiply + (matrix_size - 1) * 4
                updated_submatrix, _ = self._update_perimeter(submatrix, next_multiply)
                updated_matrix = self._update_submatrix_in_matrix(matrix, updated_submatrix)
                return updated_matrix, next_multiply
            else:
                return matrix, start_multiply

    @staticmethod
    def _get_submatrix_without_perimeter(in_matrix: list) -> list:
        if len(in_matrix) == 1:
            raise ValueError(f"Error in {inspect.stack()[0][3]}: No submatrix")
        else:
            submatrix = [row[1:-1] for row in in_matrix[1:-1]]
            if len(submatrix) == 1 and len(submatrix[0]) == 1:
                return [submatrix[0]]
            else:
                return [row[1:-1] for row in in_matrix[1:-1]]

    @staticmethod
    def _update_submatrix_in_matrix(matrix: list, submatrix: list) -> list:
        len_matrix = len(matrix)
        if len_matrix <= 2 and submatrix:
            raise ValueError("The matrix size 2 doesn't contain a submatrix!")
        elif len_matrix > 2 and submatrix:
            for row_index in range(1, len_matrix-1):
                submatrix_slice = submatrix[row_index-1][:]
                matrix[row_index][1: -1] = submatrix_slice
            return matrix
        else:
            return matrix
