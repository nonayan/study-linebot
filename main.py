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
    num = count - 1

    rand = random.randint(0, 4)
    
    String_1 = ["は", "？", "ま", "ギ", "ャ"]
    String_2 = ["なに", "ガチ", "KP", "なえ", "りょ"]
    String_3 = ["だまれ", "ボケー", "ズッ友", "最&高", "バおわ"]
    String_4 = ["キャパい", "アセアセ", "イケてる", "ギャルべ", "あげぽよ"]
    String_5 = ["やりらフィ", "こみこみで", "時差グラム", "生きるww", "大丈夫そ?"]
    String_6 = ["初心LOVE", "タンバルモリ", "ギャルピース", "片思いハート", "ちゅきちゅき"]
    String_7 = ["わかりみが深い", "パワー!ヤー!", "ルーズソックス", "ガチおわなんよ", "ふざけんなよ!"]
    String_8 = ["フレンチガーリー", "超ちるなラッパー", "どうかしてるぜっ", "あげていこうぜ!", "コーヒー無糖で。"]
    String_9 =  ["イーアールサンスー", "アーニャピーナッツ", "人生詰んだじゃんw", "元カレがさ~クズ!", "ウチ辛いのマヂ無理"]
    String_10 = ["ギャルちょーかわいー", "ひよってるやついる?", "パーティーしちゃう?", "ちょーかわいーじゃん", "キュンさせてもろて。"]

    if num == 0:
        reply_message = String_1[rand]
    elif num == 1:
        reply_message = String_2[rand]
    elif num == 2:
        reply_message = String_3[rand]
    elif num == 3:
        reply_message = String_4[rand]
    elif num == 4:
        reply_message = String_5[rand]
    elif num == 5:
        reply_message = String_6[rand]
    elif num == 6:
        reply_message = String_7[rand]
    elif num == 7:
        reply_message = String_8[rand]
    elif num == 8:
        reply_message = String_9[rand]
    elif num == 9:
        reply_message = String_10[rand]
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