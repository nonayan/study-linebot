import numbers
import random
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
import os
 
app = Flask(__name__)

#環境変数取得
# LINE Developersで設定されているアクセストークンとChannel Secretを取得し、設定します。
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
 
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
 
 
## 1 ##
#Webhookからのリクエストをチェックします。
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得します。
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得します。
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
# 署名を検証し、問題なければhandleに定義されている関数を呼び出す。
    try:
        handler.handle(body, signature)
# 署名検証で失敗した場合、例外を出す。
    except InvalidSignatureError:
        abort(400)
# handleの処理を終えればOK
    return 'OK'


## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    count = 0
    count = len(event.message.text)
    num = count -1

    rand = random.randint(0, 4)
    
    String = [["ま", "!", "?", "り", "え"], ["マジ", "ガチ", "KP", "なえ", "りょ"], ["イエベ", "ブルベ", "ズッ友", "最&高", "バおわ"], ["キャパい", "アセアセ", "イケてる", "ギャルべ", "あげぽよ"], ["やりらフィ", "こみこみで", "時差グラム", "生きるww", "大丈夫そ?"], ["初心LOVE", "タンバルモリ", "ギャルピース", "片思いハート", "ちゅきちゅき"], ["わかりみが深い", "パワー!ヤー!", "ルーズソックス", "ガチおわなんよ", "ふざけんなよ!"], ["フレンチガーリー", "超ちるなラッパー", "どうかしてるぜっ", "あげていこうぜ!", "コーヒー無糖で。"], ["イーアールサンスー", "アーニャピーナッツ", "人生詰んだじゃんw", "元カレがさ~クズ!", "ウチ辛いのマヂ無理"], ["ギャルちょーかわいー", "ひよってるやついる?", "パーティーしちゃう?", "ちょーかわいーじゃん", "キュンさせてもろて。"]]
    
    if num <= 9:
        reply_message = String[num][rand]
    elif num == 10:
        reply_message = "11文字送ってくんな!!"
    else:
        reply_message = "10文字以上は無理やって!!"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)) #ここでメッセージを返します。
 
# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)