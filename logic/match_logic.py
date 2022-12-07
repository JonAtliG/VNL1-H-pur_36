from model.match import Match

class Match_Logic():
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def __get_int_list_of_all_ids(self):
        return [int(id) for id in self.data_wrapper.get_all_match_ids()]
    
    def __create_unique_id(self):
        currentids = self.__get_int_list_of_all_ids()
        if len(currentids) > 0:
            new_id = {max(currentids) + 1}
        else:
            new_id = 1
        return new_id
    
    def give_match_list_ids(self, matches: list) -> list:
        id = self.__create_unique_id()
        matches_with_ids = []
        for match in matches:
            match.ID = id
            matches_with_ids.append(match)
            id += 1
        return matches_with_ids

    def give_match_id(self, match: Match) -> Match:
        id = self.__create_unique_id()
        match.ID = id
        return match