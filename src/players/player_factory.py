from players.player import HumanPlayer, ComputerPlayer

class PlayerFactory:
    @staticmethod
    def create_player(name):
        player = None
        if name.lower().startswith("computer"):
            difficulty = "medium"  # Default difficulty
            if "(" in name and ")" in name:
                difficulty = name[name.find("(") + 1:name.find(")")]
            player = ComputerPlayer(name.split("(")[0].strip(), difficulty)
        else:
            player = HumanPlayer(name)
            
        return player