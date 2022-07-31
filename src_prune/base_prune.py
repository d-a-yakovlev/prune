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
        fh = open(self.case_data_name, "w")
        fh.close()

        fh = open(self.case_data_name, "a")
        for data in data_arr:
            fh.write(data)
        
        fh.close()

        brute_ans = os.popen(f"python {self.brute_solution} < {self.case_data_name}").readlines()
        opt_ans = os.popen(f"python {self.opt_solution} < {self.case_data_name}").readlines()

        if brute_ans == opt_ans:
            print (f"Test {test_count} : OK")
        else:
            print (f"Test {test_count} : Not OK \n  {data_arr}")
