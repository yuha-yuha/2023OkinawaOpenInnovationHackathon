import os
import open_ai
from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError   
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
load_dotenv()
app = Flask(__name__)

Configuration = Configuration(access_token=os.environ['access_token'])
handler = WebhookHandler(os.environ['channel_sercret'])

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.warn("Invalid Signature.")
        abort(400)
        
    return 'ok'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(Configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        match event.message.text:
            case "終了":
                open_ai.SessionDelete()
            case _:
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text=open_ai.ask(event.message.text, event.source.user_id))]
                    )
                )

    
if __name__ == "__main__":
    app.run()
