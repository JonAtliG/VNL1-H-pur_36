import re
class Input_Validator:
    def __init__(self, input):
        self.input = input

    def date(self):
        if ";" in self.input or "," in self.input:
            return False
        target = re.search("(\d{2}).(\d{2}).(\d{4})", self.input)
        if target == None:
            return False
        if target.group(1) > 31 or target.group(1) < 1:
            return False
        if target.group(2) > 12 or target.group(2) < 1:
            return False
        if target.group(3) < 2022 or target.group(3) > 2050:
            return False
        return True
        
    def name(self):
        if ";" in self.input or "," in self.input:
            return False
        if len(self.input) < 2 or len(self.input) > 50:
            return False
        return True

    def nid(self):
        if ";" in self.input or "," in self.input:
            return False
        if len(self.input) != 10:
            return False
        if not self.input.isdigit():
            return False
        return True
    
    def number(self, high):
        if ";" in self.input or "," in self.input:
            return False
        if not self.input.isdigit():
            return False
        if int(self.input) > high or int(self.input) < 1:
            return False
        return True
