def swap(mat, i, r):
    temp = mat[r]
    mat[r] = mat[i]
    mat[i] = temp
    return mat


def cleanRREF(rref):
    for i in range(len(rref)):
        for j in range(len(rref[0])):
            rref[i][j] = round(rref[i][j], 10)
    return rref


def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=' ')


def find_pivot_positions(matrix):
    m, n = len(matrix), len(matrix[0])
    pivot_positions = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                pivot_positions.append((i, j))
                break
    return pivot_positions


def findRREF(mat):

    first_ele = 0

    no_of_rows = len(mat)
    no_of_cols = len(mat[0])

    for r in range(no_of_rows):
        if no_of_cols <= first_ele:

            return mat

        i = r
        while mat[i][first_ele] == 0:
            i = i + 1
            if no_of_rows == i:
                i = r
                first_ele = first_ele + 1
                if no_of_cols == first_ele:
                    return mat

        if i != r:
            mat = swap(mat, i, r)

        mat[r] = [mat[r][k]/mat[r][first_ele] for k in range(len(mat[r]))]

        for j in range(no_of_rows):
            if j != r:
                mat[j] = [mat[j][k] - mat[j][first_ele]*mat[r][k]
                          for k in range(len(mat[j]))]

        first_ele = first_ele + 1
    return mat


f = open("./input.txt", 'r').read()
inp = f.split("\n")
i_ctr = 0
no_of_rows = int(inp[i_ctr])
i_ctr += 1
no_of_cols = int(inp[i_ctr])
i_ctr += 1
mat = []
for i in range(no_of_rows):
    temp = list(map(int, inp[i_ctr].split()))
    i_ctr += 1
    mat.append(temp)


RREF = cleanRREF(findRREF(mat))

print("PIVOT POSITIONS: ")
pivots = find_pivot_positions(RREF)
n_pivots = len(pivots)
n_free = no_of_cols-n_pivots
print(pivots)
pivot_cols = [i[1] for i in pivots]
non_pivot_cols = [i for i in range(no_of_cols) if i not in pivot_cols]

print("RREF : ")
print_matrix(RREF)
print("SOLUTION: ")
if(n_free == 0):
    print([0 for i in range(no_of_cols)])
    print("Only Trivial Solution exists")
else:
    ans_mat = [[0 for i in range(no_of_cols)] for j in range(n_free+1)]

    for i in range(no_of_rows):
        pivot = -1
        for j in range(no_of_cols):
            if(RREF[i][j] == 1):
                pivot = j
            if(pivot != -1 and pivot != j and RREF[i][j] != 0):
                ind = non_pivot_cols.index(j)+1

                ans_mat[ind][pivot] -= RREF[i][j]

    for i in non_pivot_cols:
        ind = non_pivot_cols.index(i)+1
        ans_mat[ind][i] = 1
    ctr = 0
    for i in range(len(ans_mat)):
        if(i != 0):
            print(f'x_{non_pivot_cols[i-1]}*{ans_mat[i]}+', end=" ")
        else:
            print(f'{ans_mat[i]} + ', end="")



# used for reference: wikipedia of row echelon form , link- https://en.wikipedia.org/wiki/Row_echelon_form
