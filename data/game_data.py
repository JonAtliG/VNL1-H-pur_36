from CSV_Handler import CSV_Handler

class Game_Data():
    def __init__(self) -> None:
        self.file_name = "data/files/game_data.csv"
        self.CSV_Handler = CSV_Handler(self.file_name)
