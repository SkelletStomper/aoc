

class FileProvider:
    _singleton: None = None
    _created: int = 0
    @staticmethod
    def create() -> "FileProvider":
        if FileProvider._singleton == None:
            FileProvider._created = 1
            FileProvider._singleton = FileProvider() # type: ignore
            FileProvider._created = 2
        return FileProvider._singleton
    
    def __init__(self):
        if FileProvider._created != 1:
            raise Exception("Instantiate Singletons over the Create method!")
        self.year = 2017
        
    @staticmethod
    def set_year(year: int) -> None:
        FileProvider.create().year = year
    
    @staticmethod
    def get_path(filename: str) -> str:
        return f"./y{FileProvider.create().year}/data/{filename}"




def linewise(filename: str, strip_newlines = False):
    path = FileProvider.get_path(filename)
    with open(path, "r") as f:
        for line in f.readlines():
            if strip_newlines:
                yield line.replace("\n", "")
            else:
                yield line

def file_string(filename):
    return "".join([line for line in linewise(filename)])

def one_and_next(x, space= 1):
    for n in range(len(x)-space):
        yield x[n], x[n+space]



def replace_dict(string: str, repDic: dict[str, str]) -> str:
    for key, value in repDic.items():
        string = string.replace(key, value)
    return string


class inf:
    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False
    
    def __eq__(self, other):
        return isinstance(other, inf)
        
    