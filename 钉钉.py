import requests
import json




def msg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                "11111"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print(requests.post(api_url, json.dumps(json_text), headers=headers).content)


if __name__ == '__main__':

    token ="829be9b98bff04172277bba17de41c13a709c998c5e28c883d8cc1704a7983a4"
    text = 'ubuntu虚拟机'+'报警'+'abc'

    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % token
    msg(text)

