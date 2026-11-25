def create_matrix(rows,cols,value=0):
    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(value)

        matrix.append(row)

    return matrix


#--------------------
#testing
A = create_matrix(2,3)
print(A)
#--------------------


def matrix_add(A,B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            value = A[i][j] + B[i][j]
            row.append(value)

        result.append(row)

    return result


def matrix_subtract(A,B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            value = A[i][j] - B[i][j]
            row.append(value)

        result.append(row)

    return result


def matrix_multiply(A,B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Incompatible")

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0 

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = []

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(A[i][j])

        result.append(row)

    return result


def scalar_multiply(A, scalar):
    result = []

    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        row = []

        for j in range(cols):
            value = A[i][j] * scalar
            row.append(value)

        result.append(row)

    return result


def elementwise_multiply(A,B):

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Incompatible Dimensions")

    result = []

    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        row = []

        for j in range(cols):
            value = A[i][j] * B[i][j]
            row.append(value)

        result.append(row)

    return result
#--------------------
#testing
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print("Addition :", matrix_add(A,B))
print("Subtract :", matrix_subtract(A,B))
print("Multiply :", matrix_multiply(A,B))
print("Transpose :", matrix_transpose(A))
print("ElementWise Multiply :", elementwise_multiply(A,B))
#--------------------
