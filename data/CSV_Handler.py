class DataNotFound(Exception):
    pass

class CSV_Handler():
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name
    
    def get_data_by_line_index(self, index: int) -> list:
        '''Returns a list of the data of the line at the index'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for i, line in enumerate(csv.readlines()):
                if i == index:
                    return line.strip("\n").split(";")
        raise DataNotFound
    
    def get_data_by_data(self, data: str, data_index: int) -> list:
        '''Returns a list of the data of the line, if the data given matches the line data at the given index'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for line in csv.readlines()[1:]:
                split_line = line.strip("\n").split(";")
                if split_line[data_index] == data:
                    return split_line
        raise DataNotFound
    
    def get_data_by_data_in_data(self, data: str, data_index: int):
        '''Returns a list of data of the line, if the data matches a data in the data of the line data at the given index'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for line in csv.readlines()[1:]:
                split_line = line.strip("\n").split(";")
                for data_in_data in split_line[data_index].split(","):
                    if data_in_data == data:
                        return split_line
        raise DataNotFound
    
    def get_line_index_by_data(self, data: str, data_index: int) -> int:
        '''Returns the index of the line if the data given matches the line data at the given index'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for i, line in enumerate(csv.readlines()[1:]):
                split_line = line.split(";")
                if split_line[data_index] == data:
                    return i+1
        raise DataNotFound
    
    def get_all_data(self) -> list:
        '''Returns a list of all the data in the file'''
        data = []
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for line in csv.readlines()[1:]:
                data.append(line.strip("\n").split(";"))
        if data:
            return data
        else:
            raise DataNotFound
    
    def get_all_data_by_column_index(self, index: int) -> list:
        '''Returns a list of all data of at the index column'''
        data = []
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            for line in csv.readlines()[1:]:
                data.append(line.split(";")[index])
        if data:
            return data
        raise DataNotFound

    def add_line(self, line: str) -> None:
        '''Adds a new line to the file'''
        with open(self.__file_name, "a", encoding="UTF-8") as csv:
            csv.write(line + "\n")

    def replace_line(self, index: int, new_line: str) -> None:
        '''Replaces the line at the index with the new line'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            lines = csv.readlines()
        with open(self.__file_name, "w", encoding="UTF-8") as csv:
            for i, line in enumerate(lines):
                if i == index:
                    csv.write(new_line + "\n")
                else:
                    csv.write(line)

    def remove_line(self, index: int) -> None:
        '''Removes the line at the index'''
        with open(self.__file_name, "r", encoding="UTF-8") as csv:
            lines = csv.readlines()
        with open(self.__file_name, "w", encoding="UTF-8") as csv:
            for i, line in enumerate(lines):
                if i != index:
                    csv.write(line)
