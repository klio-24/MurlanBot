import secrets
import boto3

class Game:
    def __init__(self):
        self.history = []
        self.session_id = secrets.token_hex(16)

    def play_move(self, move):
        response = f"You chose: {self.load_from_db()}"
        self.history.append(response)
        return "\n".join(self.history)
    
    def save_to_db(self, in_val):
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        table = dynamodb.Table('game_sessions')
        table.put_item(Item={"session_id": self.session_id, "test": in_val})

    def load_from_db(self):
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        table = dynamodb.Table('game_sessions')
        response = table.get_item(Key={"session_id": self.session_id})
        return response.get('Item')