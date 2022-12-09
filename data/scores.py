class Scores:
    def __init__(self):
        '''Constructor for Scores class.'''
        self.file_name = "files/scores.csv"


    def get_scores(self):
        '''Returns a list of all the scores in the file.'''
        games = []
        with open(self.file_name, "r") as csv:
            c = 0
            for i in csv:
                if "Date:" in i:
                    games_on_date = [i.strip("Date: ").strip("\n")]
                elif "Game" in i:
                    matches = [i.strip("Game:").strip()]
                    c = 12
                elif c > 0:
                    matches.append(i.strip("\n").split(";"))
                    c -= 1
                    if c == 0:
                        games_on_date.append(matches)
                elif i == "\n":
                    try:
                        games.append(games_on_date)
                    except:
                        pass
            games.append(games_on_date)
        return games


    def add_score(self, game):
        '''Adds a score to the file.'''
        with open(self.file_name, "a") as csv:
            csv.write("\nDate: " + game[0] + "\n")
            csv.write("Game: " + game[1] + "\n")
            for i in game[2]:
                csv.write(";".join(i) + "\n")