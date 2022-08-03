import os

'''
Класс как пространство имён
статичных методов для валидации
'''


class Prune:

    '''
    Конструктор
    Принимает:
    - case_data_name - имя файла для буфера
    - brute_solution - имя файла не оптимального решения
    - opt_solution - имя файла оптимального решения
    '''
    def __init__(self, case_data_name, brute_solution, opt_solution):
        self.case_data_name = case_data_name
        self.brute_solution = brute_solution
        self.opt_solution = opt_solution
    '''
    Классический подход
    Принимает:
    - data_arr - данные для одного тестового случая
    - test_count - номер теста
    '''
    def classic_check (self, data_arr, test_count):

        with open(self.case_data_name, 'w') as fh:
            for data in data_arr:
                fh.write(data)

        brute_ans = os.popen(f"python3 {self.brute_solution} < {self.case_data_name}").readlines()
        opt_ans = os.popen(f"python3 {self.opt_solution} < {self.case_data_name}").readlines()

        if brute_ans == opt_ans:
            print (f"Test {test_count} : OK")
        else:
            f = open(wrong.txt, 'a')
            print (f"Test {test_count} : Not OK \n  "
                   f"{data_arr}\n "
                   f"correct answer: {brute_ans}\n "
                   f"wrong answer:{opt_ans}\n", file=f)
            f.close()

    def check_with_solution(self,  data_arr, test_count):
        with open(self.case_data_name, 'w') as fh:
            for data in data_arr:
                fh.write(data)

        opt_ans = os.popen(f"python3 {self.opt_solution} < {self.case_data_name}").readlines()

        if brute_ans == opt_ans:
            print(f"Test {test_count} : OK")
        else:
            print(f"Test {test_count} : Not OK \n  {data_arr}")

