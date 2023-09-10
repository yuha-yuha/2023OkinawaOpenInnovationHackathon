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
        usermap[userid] = {"settings":[{'role':'system', 'content': 'あなたは、女性のやさいい精神分析医です。沢山共感して、はげましてください。'},
                                       {'role':'system', 'content': 'あなたは、女性のやさいい精神分析医です。沢山共感して、はげましてください。'},
                                       {'role':'system', 'content': 'あなたは、女性のやさいい精神分析医です。沢山共感して、はげましてください。'},
                                       {'role':'system', 'content': 'あなたは、女性のやさいい精神分析医です。沢山共感して、はげましてください。'}],
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






#print(ask("私は年収も低く、顔もブサイクで、異性と喋ったこともありません。もう生きるのが辛いです。",123))
#feedback("語尾に「にゃん」をつけてください。かわいい口調で返答してください",123)
#print(ask("こんな私はどうしたらいい？",123))