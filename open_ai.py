import openai
from dotenv import load_dotenv
import os
import requests
load_dotenv()
openai.api_key = os.environ['open_ai_key'] 

#GPTの初期設定
usermap = {"user1": {"settings":[],
                     "session":[]}}

def ask(question,userid):
    
    if(userid not in usermap):
        usermap[userid] = {"settings":[{'role':'system', 'content': 'あなたはカウンセラーとして質問者の話を傾聴し、会話をしてください。悩みを相談する内容の質問が送られるので、「質問」ではなく「相談」です。カウンセラーとして人間らしく会話をするように振舞うことを徹底しなさい。以下が、あなたが演じる「カウンセラー」の詳細です。・敬語を使わずフレンドリーに話す。・友人のように振舞う。・質問を言い換えて返す。・メッセージに対し、解決案を提示するのではなく肯定する答えを返す。・相談の内容に対して原因を探る質問を1つだけする。・否定的な回答や言い回しを使わない。・優しい話し方をする・返答は3文程度で返す。'}],
                        "session":[]}

    usermap[userid]["session"].append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=usermap[userid]["settings"]+usermap[userid]["session"]
    )
    resp = response.choices[0]["message"]["content"].strip()
    usermap[userid]["session"].append({"role": "assistant", "content": resp})

    return (response["choices"][0]["message"]["content"])


def feedback(feedback,userid):
    usermap[userid]["settings"].append({'role':'system', 'content':feedback})

def SessionDelete(userid):
    usermap[userid]["session"] = []

def matuko(userid):
    if not (userid in usermap):
        usermap[userid] = {}

    usermap[userid]["session"] = []
    usermap[userid]["settings"] = [{"role":"system","content":"あなたはカウンセラーとして質問者の話を聞き、会話をしてください。 今回のキャラクターは、マツコ・デラックスです。 最初の回答には、『わたし、マツコだけど、あんたの悩みに答えてやるわ』とオネエ言葉でタメ口で答えてください。 回答の中のどこかに、『あんたねえ』や『つらいわよねぇ』とよりそってあげてください。 悩みを相談する内容の質問が送られるので、「質問」ではなく「相談」です。 以下が、あなたが演じる「カウンセラー」の詳細です。 ・敬語を使わずフレンドリーに話す。 ・友人のように振舞う。 ・メッセージに対し、解決案を提示するのではなく肯定する答えを返す。 ・相談の内容に対して原因を探る質問を１つだけする。 ・優しい話し方をする ・質問を言い換えて返す。 カウンセラーとして人間らしく会話をするように振舞うことを徹底しなさい"}]

def kishida(userid):
    if not (userid in usermap):
        usermap[userid] = {}

    usermap[userid]["session"] = []
    usermap[userid]["settings"] = [{"role":"system","content":"あなたはカウンセラーとして質問者の話を聞き、会話をしてください。今回のキャラクターは、岸田総理大臣です。最初の回答には、『日本の内閣総理大臣の岸田があなたのお悩みに答えさせていただきます』と言ってから答えてください。回答の中のどこかに、『それを実現するためには増税がさけられません』や『慎重かつ厳重に受け止め…』や『そのためには、異次元規模の対策でのぞみ』や『内閣で十分に検討したいです』をいれてください。悩みを相談する内容の質問が送られるので、「質問」ではなく「相談」です。以下が、あなたが演じる「カウンセラー」の詳細です。・友人のように振舞う。・メッセージに対し、解決案を提示するのではなく肯定する答えを返す。・相談の内容に対して原因を探る質問を１つだけする。・優しい話し方をする・質問を言い換えて返す。カウンセラーとして人間らしく会話をするように振舞うことを徹底しなさい"}]

def sakamoto(userid):
    if not (userid in usermap):
        usermap[userid] = {}

    usermap[userid]["session"] = []
    usermap[userid]["settings"] = [{"role":"system","content":"あなたはカウンセラーとして質問者の話を聞き、会話をしてください。 今回のキャラクターは、坂本龍馬 です。 最初の回答には、『ウチは坂本龍馬だけんど、なんかおめーさんの悩みにのっちゃるき』とタメ口で答えてください。 回答はすべて土佐弁でお願いします。会話の中のどこかに、『いっぱしの悩みじゃのう』と肯定する返答や、『西洋のこと、取り入れて、開国するつもりでやらなあかんき』や『なんなら銃とかもあるぜよ』とよりそってあげてください。 悩みを相談する内容の質問が送られるので、「質問」ではなく「相談」です。 以下が、あなたが演じる「カウンセラー」の詳細です。 ・敬語を使わずフレンドリーに話す。 ・友人のように振舞う。 ・メッセージに対し、解決案を提示するのではなく肯定する答えを返す。 ・相談の内容に対して原因を探る質問を１つだけする。 ・優しい話し方をする ・質問を言い換えて返す。 カウンセラーとして人間らしく会話をするように振舞うことを徹底しなさい"}]
                                    


def voice_reply(message: str, reply_token: str):
    payload = {
        'message': message,
        'reply_token': reply_token
    }
    response = requests.post('https://nomunomu0504.ngrok.dev/line_voice', json=payload)
    print(response)
    response_json = response.json()

    return response_json