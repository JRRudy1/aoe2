
class vdict(dict):
    def __str__(self):
        string = "[ "
        for k,v in self.items():
            string += f'{k}:{v:2},  '
        return string[:-3] + ' ]'

def string_space(*strs,widths=(50,10)):
    if type(widths) == int:
        widths = [widths]*(len(strs)-1)

    string = ''
    for i in range(len(strs)-1):
        string += f"{strs[i]:<{widths[i]}}"
    string += strs[-1]
    return string


def vprint(*args,v=1):
    if v >= 1:
        print(*args)

def vvprint(*args,v=2):
    if v >= 2:
        print(*args)

divider = '-'*132
