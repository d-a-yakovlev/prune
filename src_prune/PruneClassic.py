from src_prune import Prune
import os

'''
Класс как пространство имён
статичных методов для валидации
'''


class PruneClassic(Prune):
    '''
    Конструктор
    Принимает:
    - directory - имя директории, в которой хранятся файлы "contest1"
    - task - имя задачи "A"
    '''

    def __init__(self, directory_name, task_name):
        super().__init__(directory_name=directory_name, task_name=task_name)

        self.brute_solution = self.directory_name + "/" + self.task_name + "_brute.py"
    
    '''
    Классический подход
    Принимает:
    - data_arr - данные для одного тестового случая
    - test_count - номер теста
    '''
    def check(self, data_arr, test_count):

        data_str = '\n'.join(data_arr)
        brute_ans = os.popen(f"echo {data_str} | python3 {self.brute_solution}").readlines()
        opt_ans = os.popen(f"echo {data_str} | python3 {self.opt_solution}").readlines()

        log_file = open(self.log_name, 'a')
        if brute_ans == opt_ans:
            print (f"Test {test_count} : OK")
            print (f"Test {test_count} : OK", file=log_file)
        else:
            
            print (f"Test {test_count} : Not OK \n  "
                   f"{data_arr}\n "
                   f"correct answer: {brute_ans}\n "
                   f"wrong answer:{opt_ans}\n", file=log_file)

        log_file.close()
