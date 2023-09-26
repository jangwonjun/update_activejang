from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from env import SLACK

slack_token = SLACK.TOKEN
client = WebClient(token=slack_token)

class slack_bot : 
        
    def __init__(self):
        def mail_arrive(self):
            try:
                response = client.chat_postMessage(
                    channel=SLACK.MONITOR, #채널 id를 입력합니다.
                    text="안녕하세요~!"
                )
            except SlackApiError as e:
                assert e.response["error"]
                
    
            