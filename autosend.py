import itchat
import requests

itchat.login()
#从图灵中获取回复信息
def get_response(message):
    #请求地址
    apiUrl = "http://www.tuling123.com/openapi/api"
    #请求的数据
    data = {
        "key"    : "86504cd4f5c143c886215a81118da68d",
        "info"   : message,
        "userid" : "robot"
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        info = r["text"]
        return info
    except:
        return

#回复给微信好友,msg是好友的信息。
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultReply = "我知道了"
    #搜索微信好友
    realFriend = itchat.search_friends(name="zhangyujia")
    #得到用户名称
    realFriendsName = realFriend[0]["UserName"]
    #打印好友回复的信息
    print("message:%s"%msg["Text"])
    #调用图灵接口
    reply = get_response(msg["Text"])
    if msg["FromUserName"] == realFriendsName:
        itchat.send(reply,toUserName=realFriendsName)

itchat.run()
