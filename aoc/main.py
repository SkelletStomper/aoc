import util

class Runner:
    def __init__(self, year, day, task):
        self.year = year
        self.day = day
        self.task = task
        self.run()
    
    def run(self):
        import importlib.util # cheers https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
        import sys
        spec = importlib.util.spec_from_file_location("module.name", f"./y{self.year}/day{self.day}.py")
        day = importlib.util.module_from_spec(spec)
        sys.modules["module.name"] = day
        spec.loader.exec_module(day)

        util.FileProvider.set_year(self.year)
        if self.task == 1:
            day.run1()
        else:
            day.run2()



Runner(
    year=2023,
    day=7,
    task=2
    )



