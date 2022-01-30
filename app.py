from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
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
    msg = event.message.text
    s = '今天晚上特別允許你可以...嗯..對我亂來喔~~(臉紅)'
    
    if '圖片' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ErRXu3m.jpg',
            preview_image_url='https://i.imgur.com/ErRXu3m.jpg'
        )
    
        line_bot_api.reply_message(
            event.reply_token,
            image_message)
        return

    if '色圖' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/GSJ0tw2.jpg',
            preview_image_url='https://i.imgur.com/GSJ0tw2.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token,
            image_message)
        return

    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='36'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return


    if msg in ['我愛你', '我愛妳']:
        s = '啊.啊..不可以色色啦!老公 >.< ||  我也愛你~~love you too'
    elif '親' in msg:
        s = '討厭啦~~ 我同意 但是要把我抱起來親喔!!皓宇寶貝'
    elif msg == '愛妳寶貝':
        s = '嘴巴真甜 真是的~~拿你沒辦法(害羞)/// 今晚同意你做...(色色' 
    elif '老婆' in msg:
        s = '記得回家要親一個喔~~ by洛琪希' 
    elif '頭髮' in msg:
        s = '等等洗完再讓你聞個夠啦! 小色鬼~'  
    elif '累' in msg:
        s = '辛苦你了 晚上回家給你小獎勵吧! 膝枕或..那個..都可以喔!'
    elif '洗澡' in msg:
        s = '那..今晚要不要陪我一起洗澡呢?(臉紅) 看你平常對我很貼心~ 今天允許你洗澡時可以亂來呦!'
    elif msg == '今晚我想吃掉你':
        s = '那要對我溫柔一點喔..啾咪~~'

    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()
