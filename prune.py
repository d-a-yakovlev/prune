import sys
import os

'''
-d параметр для католога dir (e.g -d contest1)
-t параметр для задачи task (e.g -t A)

Запуск будет следующий python prune.py -d contest1 -t A
'''

def ans_check (data_arr, test_count):
    fh = open(case_data_name, "w")
    fh.close()

    fh = open(case_data_name, "a")
    for data in data_arr:
        fh.write(data)
    
    fh.close()

    brute_ans = os.popen(f"python {brute_solution} < {case_data_name}").readlines()
    opt_ans   = os.popen(f"python {opt_solution} < {case_data_name}").readlines()

    if brute_ans == opt_ans:
        print (f"Test {test_count} : OK")
    else:
        print (f"Test {test_count} : Not OK \n  {data_arr}")




_, f_d, dir_name, f_t, task_name = sys.argv

task_data_name = dir_name + "/" + task_name + "_data.txt"
brute_solution = dir_name + "/" + task_name + "_brute.py"
opt_solution   = dir_name + "/" + task_name + "_opt.py"

data_sep = "/* end */"
case_data_name = dir_name + "/" + task_name + "_case_data.txt"

# Читать из task_data_name до разделителя, потом передать эти данные в решения
data_file = open(task_data_name, "r")
input_data = []
test_count = 1

for line in data_file:
    line = line.strip()
    if line != data_sep:
        input_data.append(line)
    else:
        ans_check(input_data, test_count)
        test_count += 1
        input_data.clear()

data_file.close()




