from msilib.schema import Property
import time

class Prune:
    def __init__(self, directory_name, task_name):
        self.directory_name = directory_name
        self.task_name = task_name

        self._task_data_name = self.directory_name + "/" + self.task_name + "_data.txt"
        self.opt_solution = self.directory_name + "/" + self.task_name + "_opt.py"
        self.log_name = self.directory_name + "/" + self.task_name + "_log_" + time.asctime() + ".txt"

    @Property
    def task_data_name(self):
        return self._task_data_name
    
    def check(self):
        pass