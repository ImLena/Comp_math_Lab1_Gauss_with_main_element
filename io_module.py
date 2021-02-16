import random

def input_parameters(A):
        print("Необходимо определить размерность (<= 20).\n" +
              "Чтобы задать с клавиатуры введите 'k'\n" +
              "Чтобы задать из файла введите 'f'")
        answer = input().strip()
        if answer == "k":
          n = input_n_from_console(A)
          return n
        elif answer == "f":
            n = input_parameters_from_file(A)
            return n
        else:
            print("Неверные данные")
            input_parameters(A)

def input_matrix(n, A):
    print("Если хотите ввести матрицу с консоли, введите 'k',\n" +
             "если хотите сгенерировать матрицу рандомно, введите 'r'")
    case = input().strip()
    if case == "k":
        print("Вводите коэффициенты матрицы построчно, разделяя значения пробелами.\n" +
                  "Число строк и столбцов должно быть одинаковым (не считая столбца свободных членов)")
        for i in range(n):
            current_line = input().split()
            if (len(current_line) != n+1):
                print ("Неверное число элементов")
                input_n_from_console(A)
            A.append(current_line)
    elif case == "r":
            random_parameter(n, A)
    else:
           print("Неверные данные")
           input_matrix(n, A)
           
def input_n_from_console(A):
   try:
     n = int(input("Введите n от 1 до 20:\n").strip())
     if n < 1 | n > 20:
       print("Ошибка!")
       input_n_from_console(A)
     else:
       input_matrix(n, A)
     return n
   except ValueError:
     print("Неверные данные")
     input_n_from_console(A)


def input_parameters_from_file(A):
    try:
        n = 0
        path = input("Введите имя файла\n")
        with open(path, 'r', encoding='utf-8') as file:
          while n == 0:
            line = file.readline()
            if line != "\n" and line != " ":
                n = line.split()
                n = int(n[0])
          #while line:
           #   line = file.readline()
                read_lines = 0
                while read_lines < n:
                  line = file.readline()
                  current_line = line.split()
                  A.append(current_line)
                  read_lines += 1
        file.close()
        return n
    except FileNotFoundError:
        print("Файл " + path + " не найден")
        input_parameters(A)
    except ValueError:
        print("Неверные данные")
        input_parameters(A)

def random_parameter(n, A):
    try:
      for i in range(n):
          current_line = []
          for j in range(n + 1):
              current_line.append(round(float(random.uniform(1, 100)), 3))
          A.append(current_line)
      print("Полученная матрица:\n")
      print_matrix(n, A)
      print("\n")
    except ValueError:
        print("Неверные данные")

def print_x(x, n):
    x.reverse()
    for i in range(n):
        print("x" + str(i+1) + " = " + "%.3f" % float(x[i]) + "; ")

def print_matrix(n, A):
    for i in range(n):
        for j in range(n):
            if float(A[i][j]) < 0:
                if abs(float(A[i][j])) >= 10:
                    print("%.3f" % float(A[i][j]) + " ", end='')
                else:
                    print(" " + "%.3f" % float(A[i][j]) + " ", end='')

            else:
                if abs(float(A[i][j])) >= 10:
                    print(" " + "%.3f" % float(A[i][j]) + " ", end='')
                else:
                    print(" "*2 + "%.3f" % float(A[i][j]) + " ", end='')
        print("| " + str(A[i][n]) + "\n")

def print_residual(i, residual):
    print("Невязка в строке " + str(i+1) + " равна " + "%.6f" % float(residual))

