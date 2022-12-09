import re
import datetime

class Input_Validator:
    def date(self, inp, low, high):
        if ";" in inp or "," in inp:
            return False
        target = re.search("(\d{2}).(\d{2}).(\d{4})", inp)
        if target == None:
            return False
        if int(target.group(1)) > 31 or int(target.group(1)) < 1:
            return False
        if int(target.group(2)) > 12 or int(target.group(2)) < 1:
            return False
        if int(target.group(3)) < 2022 or int(target.group(3)) > 2050:
            return False
        checks = [True, True]
        if not low is None:
            checks[0] = datetime.datetime.strptime(inp, "%d.%m.%Y") >= datetime.datetime.strptime(low, "%d.%m.%Y")
        if not high is None:
            checks[1] = datetime.datetime.strptime(inp, "%d.%m.%Y") <= datetime.datetime.strptime(high, "%d.%m.%Y")
        return checks[0] and checks[1]
        
    def name(self, inp):
        if ";" in inp or "," in inp:
            return False
        if len(inp) < 2 or len(inp) > 50:
            return False
        return True

    def nid(self, inp):
        if ";" in inp or "," in inp:
            return False
        if len(inp) != 10:
            return False
        if not inp.isdigit():
            return False
        return True
    
    def number(self, inp, high):
        if ";" in inp or "," in inp:
            return False
        if not inp.isdigit():
            return False
        if int(inp) >= high or int(inp) < 1:
            return False
        return True


    def mail(self, inp):
        if ";" in inp or "," in inp:
            return False
        if len(inp) < 5 or len(inp) > 50:
            return False
        if "@" not in inp:
            return False
        return True
    
    def phone(self, inp):
        if ";" in inp or "," in inp:
            return False
        if len(inp) != 7:
            return False
        if not inp.isdigit():
            return False
        return True
    
    def birthday(self, inp):
        if ";" in inp or "," in inp:
            return False
        target = re.search("(\d{2}).(\d{2}).(\d{4})", inp)
        if target == None:
            return False
        if int(target.group(1)) > 31 or int(target.group(1)) < 1:
            return False
        if int(target.group(2)) > 12 or int(target.group(2)) < 1:
            return False
        if int(target.group(3)) < 1900 or int(target.group(3)) > 2021:
            return False
        return True