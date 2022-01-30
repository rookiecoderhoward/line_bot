from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('mD0QwtD3X5zwWKmKU/VKvfCFYftYym8heb9lB64vJXIS8cQqT0whg/okx5SLzIgG+Hg4sPkZ8LlwWP71/pe7u0fl95Jh+H8sndI1+cX8K70jrMvHujNOBP7Su3Hm0w/CLiBfOa8K+BmZwf0tbUMiWQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bb118b2fb70a5df58e63ef58018679cc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
