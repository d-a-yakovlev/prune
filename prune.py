import argparse
from src_prune.base_prune import Prune

'''
1) параметр для католога dir (e.g contest1)
2) параметр для задачи task (e.g A)

Запуск будет следующий python prune.py contest1 A
'''
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='', required=True)
parser.add_argument('-f', '--file', help='', required=True)
parser.add_argument('-s', '--solution', help='', action='store_true')
args = parser.parse_args()

task_data_name = dir_name + "/" + task_name + "_data.txt"
brute_solution = dir_name + "/" + task_name + "_brute.py"
opt_solution   = dir_name + "/" + task_name + "_opt.py"

data_sep = "/* end */"
case_data_name = dir_name + "/" + task_name + "/"+_case_data.txt"

tester = Prune(case_data_name, brute_solution, opt_solution)

# Читать из task_data_name до разделителя, потом передать эти данные в решения
data_file = open(task_data_name, "r")
input_data = []
test_count = 1

for line in data_file:
    line = line.strip()
    if line != data_sep:
        input_data.append(line)
    else:
        tester.classic_check(input_data, test_count)
        test_count += 1
        input_data.clear()

data_file.close()




