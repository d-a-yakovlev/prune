import argparse
from src_prune.base_prune import Prune

'''
1) параметр для католога dir (e.g contest1)
2) параметр для задачи task (e.g A)
3) 

Запуск будет следующий python prune.py contest1 A
'''
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='The name of the directory where the files are stored', required=True)
parser.add_argument('-t', '--task', help='task name', required=True)
parser.add_argument('-s', '--solution', help='Set the -s flag if there '
                                             'is no native solution, but there is an output file.', action='store_true')
args = parser.parse_args()

tester = Prune(directory, task)

data_sep = "/* end */"
# Читать из task_data_name до разделителя, потом передать эти данные в решения
with open(task_data_name, "r") as data_file:
    test_count = 1
    input_data = []
    for line in data_file:
        line = line.strip()
        if line != data_sep:
            input_data.append(line)
        else:
            if solution:
                tester.check_with_solution(input_data, test_count)
            else:
                tester.classic_check(input_data, test_count)
            test_count += 1
            input_data.clear()
