#coding:utf-8
from dingtalkchatbot.chatbot import DingtalkChatbot
from ConfigParser import ConfigParser
from Stock import Stock
from Warning import Warning

class Dingding():
    def __init__(self,webhook,message):
        self.webhook = webhook
        self.message = message
    def send_dingding(self):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg = self.message)


