from src_prune import Prune
import os

class PruneSolution(Prune):

    def __init__(self, directory_name, task_name):
        super().__init__(directory_name=directory_name, task_name=task_name)

    # def check(self,  data_arr, test_count):

    #     data_str = '\n'.join(data_arr)
    #     opt_ans = os.popen(f"echo {data_str} | python3 {self.opt_solution}").readlines()

    #     if brute_ans == opt_ans:
    #         print(f"Test {test_count} : OK")
    #     else:
    #         print(f"Test {test_count} : Not OK \n  {data_arr}")