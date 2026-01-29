#============= matrix insert =============
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


mat2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

mat3 = []


print("\n\n\n\n\n")


#============= matrix addition =============

def matadds():
    if len(mat1) == len(mat2):

        for m1 in range(len(mat1)):
            mat3.append([])

            for m1in in range(len(mat1[m1])):
                res=mat1[m1][m1in] + mat2[m1][m1in]
                mat3[m1].append(res)

        for i in range(len(mat3)):
            print(mat3[i])

    else:
        print("undefined")




#============= matrix multiplication =============
def matmult():
    if len(mat1[0]) == len(mat2):

        for ml1 in range(len(mat1)):
            mat3.append([])

            for ml1in in range(len(mat2[0])):
                res=0

                for ml1inin in range(len(mat2)):
                    res += mat1[ml1][ml1inin] * mat2[ml1inin][ml1in]
                mat3[ml1].append(res)
    else:
        print("Error: Incompatible dimensions!")

    for i in range(len(mat3)):
        print(mat3[i])





wtd = int(input("what do u wish to do ? \n 1 : for addiction \n 2 : for mult \n -- :"))

if wtd == 1:
    matadds()
elif wtd == 2:
    matmult()