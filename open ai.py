import openai
from dotenv import load_dotenv
import os
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

def delete(userid):
    usermap[userid]["session"] = []

def start_finish(userid):
    usermap[userid]["session"] = []


print(ask("大学の学業に追いつかない。授業や課題への圧迫感がつらい。",123))