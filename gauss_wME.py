from io_module import input_parameters, print_x, print_matrix, print_residual

def determinant(A, permutations, n):
    det = (-1)**permutations
    for i in range(n):
        det *= float(A[i][i])
    print(det)
    return det

def gauss(n, A, x):
    try:
        permutations = 0
        for j in range(n):
            line_to_swap = find_max_el(j, n, A)
            if line_to_swap != j:
                swap_lines(line_to_swap, j, A, permutations)
            for i in range(j+1, n):
                coef = calculate_coef(A[j][j], A[i][j])
                elem_transform(i, coef, j, n, A)
        if determinant(A, permutations, n) == 0:
            print("Решений нет")
        else:
            solve_system(n, A, x)
    except ValueError:
        print("Неверные данные")
        math()
  

def find_max_el(j, n, A):
  max_el = abs(float(A[j][j]))
  max_line = j
  for i in range(j+1, n):
    if abs(float(A[i][j])) > max_el:
      max_el = abs(float(A[i][j]))
      max_line = i
  return max_line

def swap_lines(line_to_swap, current_line, A, permutations):
    permutations += 1
    current_column = current_line
    A[current_line], A[line_to_swap] = A[line_to_swap], A[current_line]

def calculate_coef(max_elem, current_elem):
  return -(float(current_elem)/float(max_elem))

def elem_transform(current_line, coef, main_line, n, A):
  for i in range(main_line, n+1):
      A[current_line][i] = round((float(A[current_line][i]) +
                                 float(A[main_line][i]) * coef), 3)

def solve_system(n, A, x):
  if float(A[n-1][n-1]) == 0:
      x.append(0)
  else:
      x.append(float(A[n-1][-1]) / float(A[n-1][n-1]))
  for i in range(n-2, -1, -1):
    current_position = n - 1
    b = float(A[i][-1])
    while current_position > i:
      b -= float(x[n - 1 - current_position]) * float(A[i][current_position])
      current_position -= 1
    if float(A[i][i]) == 0:
        x.append(0)
    else:
        x.append(b/float(A[i][i]))

def find_residuals(n, A, x):
    for i in range(n):
        residual = 0
        for j in range(n):
            residual += float(A[i][j]) * float(x[j])
        residual -= float(A[i][-1])
        print_residual(i, abs(residual))
        
def math():
    A = []
    x = []
    n = input_parameters(A)
    gauss(n, A, x)
    print_matrix(n, A)
    print_x(x, n)
    find_residuals(n, A, x)

math()
