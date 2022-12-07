class Match_Logic():
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
    
    def __get_unique_id(self):
        currentids = [int(id) for id in self.data_wrapper.get_all_match_ids()]
        if len(currentids) > 0:
            new_id = f"{max(currentids) + 1}"
        else:
            new_id = "1"
        return new_id