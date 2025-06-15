class Game:
    def __init__(self):
        self.history = []

    def play_move(self, move):
        response = f"You chose: {move}"
        self.history.append(response)
        return "\n".join(self.history)