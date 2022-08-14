from src_prune import Prune, PruneClassic, PruneSolution 

import argparse

def get_prune_tester(args):
    tester = Prune(args.directory, args.task)
    if args.solution:
        tester = PruneSolution(tester)
    else:
        tester = PruneClassic(tester)
    
    return tester

def start(args, tester):
    data_sep = args.data_sep or "/* end */"

    # Читать из task_data_name до разделителя, потом передать эти данные в решения
    with open(tester.task_data_name, "r") as data_file:
        test_count = 1
        input_data = []
        for line in data_file:
            line = line.strip()
            if line != data_sep:
                input_data.append(line)
            else:
                tester.check(input_data, test_count)
                test_count += 1
                input_data.clear()

'''
<Main thread of execution here>
Запуск будет следующий:
- python prune.py -d contest1 -t A
- python prune.py -d contest1 -t A -s
- python prune.py -d contest1 -t A -s --data_sep "< end >"
'''
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', dest="directory", help='The name of the directory where the files are stored', required=True)
parser.add_argument('-t', '--task', dest="task", help='prefix task name before required _brute.py and _opt.py (you have for example A_opt.py and A_brute.py so you write -t A)', required=True)
parser.add_argument('-s', '--solution', dest="solution", help='Set the -s flag if there ' +
                                             'is no native solution, but there is an output file.', action='store_true')
parser.add_argument("--data_sep", dest="data_sep", help="custom data separator in <task>_data.txt file")
args = parser.parse_args()

tester = get_prune_tester(args)
start(args, tester) 