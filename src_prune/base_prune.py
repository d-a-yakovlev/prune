import os

'''
Класс как пространство имён
статичных методов для валидации
'''


class Prune:


    '''
    Конструктор
    Принимает:
    - directory - имя директории, в которой хранятся файлы
    - task - ммя задачи
    '''

    def __init__(self, directory, task):
        self.directory = directory
        self.task = task
        self.task_data_name = directory + "/" + task + "_data.txt"
        self.brute_solution = directory + "/" + task + "_brute.py"
        self.opt_solution = directory + "/" + task + "_opt.py"
    '''
    Классический подход
    Принимает:
    - data_arr - данные для одного тестового случая
    - test_count - номер теста
    '''
    def classic_check(self, data_arr, test_count):

        data_str = '\n'.join(data_arr)
        brute_ans = os.popen(f"echo {data_str} | python3 {self.brute_solution}").readlines()
        opt_ans = os.popen(f"echo {data_str} | python3 {self.opt_solution}").readlines()

        if brute_ans == opt_ans:
            print (f"Test {test_count} : OK")
        else:
            f = open(f'{self.directory}/wrong.txt', 'a')
            print (f"Test {test_count} : Not OK \n  "
                   f"{data_arr}\n "
                   f"correct answer: {brute_ans}\n "
                   f"wrong answer:{opt_ans}\n", file=f)
            f.close()

    def check_with_solution(self,  data_arr, test_count):

        data_str = '\n'.join(data_arr)
        opt_ans = os.popen(f"echo {data_str} | python3 {self.opt_solution}").readlines()

        if brute_ans == opt_ans:
            print(f"Test {test_count} : OK")
        else:
            print(f"Test {test_count} : Not OK \n  {data_arr}")

