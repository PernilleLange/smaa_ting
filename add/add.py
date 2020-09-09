
def add(*matrices):
    matrix_shapes = {tuple(len(list) for list in matrix) for matrix in matrices}
    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")
    else:
        return [[sum(values) for values in zip(*lists)] for lists in zip(*matrices)]




