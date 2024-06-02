import requests

class TelegramMessenger:
    def __init__(self, bot_token):
        self.token = bot_token

    def SendMessage(self, msg, chat_id):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={msg}&parse_mode=HTML"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return
            else:
                raise Exception("Error Sending Message: ", response.json()["description"])
        except Exception as e:
            print("Error: ", e)
