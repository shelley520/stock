#coding:utf-8
from dingtalkchatbot.chatbot import DingtalkChatbot
from ConfigParser import ConfigParser
from Stock import Stock
from Warning import Warning
from Dingding import Dingding


if __name__ == '__main__':
    cp = ConfigParser()
    cp.read('config.ini')
    webhook = cp.get('dingding','webhook')
    stock_num = cp.get('stock','stock_num')
    high_price = cp.get('stock','high')
    low_price = cp.get('stock', 'low')

    message = Warning(stock_num,high_price,low_price)
    stock = Stock(stock_num)
    print stock.get_price()
    send_message = message.stock_message(stock.get_price())

    ding = Dingding(webhook,send_message)
    if  send_message> 0:
        ding.send_dingding()