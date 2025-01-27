from itertools import permutations
number_of_variables = int(input("Enter the number of variables: "))
number_of_equations = int(input("Enter the number of equations: "))
matrix = [[] for i in range(number_of_equations)]
for i in range(number_of_equations):
    for j in range(number_of_variables):
        matrix[i].append(int(input(f"Enter the value of {j + 1} variable in equation {i+1}: ")))
    matrix[i].append(int(input(f"Enter the constant value of equation {i+1}: ")))
flag = True
a = matrix.copy()
check = []
answer = 0
for case in permutations(a):
    for i in range(number_of_equations - 1):
        for j in range(i + 1, number_of_equations):
            if case[i][i] == 0:
                break
            subtraction = case[j][i] / case[i][i]
            for z in range(number_of_variables + 1):
                case[j][z] = case[j][z] - subtraction * case[i][z]
    rank_of_coefficients = number_of_equations
    rank_of_matrix = number_of_equations
    for i in range(number_of_equations):
        for j in range(number_of_variables):
            if case[i][j] != 0:
                break
        else:
            rank_of_coefficients -= 1
            if case[i][-1] == 0:
                rank_of_matrix -= 1
    if (rank_of_coefficients != rank_of_matrix):
        print("The system of equations does not has solutions.")
        answer = 1
        break
    if (rank_of_coefficients > number_of_equations):
        print("The system of equations does not have solutions.")
        answer = 1
        break
    else:
        if rank_of_coefficients < number_of_variables:
            print("The system of equations has infinity solutions.")
            answer = 1
            break
    for i in range(number_of_variables):
        if case[i][i] == 0:
            check.append(0)
            flag = False
            break
    if flag == False:
        continue
    solution = [0 for i in range(number_of_variables)]
    for i in range(number_of_variables - 1, -1, -1):
        solution[i] = (case[i][-1] - sum([solution[j] * case[i][j] for j in range(number_of_variables - 1, i, -1)])) / case[i][i]
    check.append(1)
    break
if 1 in check:
    print("The solution for system of equation is : ")
    for i in range(len(solution)):
        print(f"{i + 1}: {round(solution[i], 4)}")
else:
    if answer == 0:
        print("The system of equations has infinity solutions.")