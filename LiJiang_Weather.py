#coding:utf-8
import os
import urllib.request
import re
import time
import pygame
import datetime
import threading

def getHtml(url):
    page = urllib.request.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()                  # read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。
    return html

def getdata(html):
    html = html.decode('utf-8')         #html内容编码
    reg =r'(湿度:)[\S\s]{43}([\d]*)[\S\s]{44}(%)[\S\s]*(云量:)[\S\s]{43}([\d]*)'
    datre = re.compile(reg)             #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)   #读取html中包含正则表达式的数据。
    return datlist
    #for dat in datlist:
    #    dat = str(dat)
    #    in_file.write(dat + "\n")       #每个list元素一行保存。


in_file=open('C:\\Monitor_Weather\\LiJiang_Weather\\WeaInf.txt','w+')
urlstr='http://weather.gmg.org.cn:9000/latest_gmg.php'
pygame.mixer.init()
pygame.mixer.music.load('C:\\Monitor_Weather\\sound.mp3')
while 1:
    in_file = open('C:\\Monitor_Weather\\LiJiang_Weather\\WeaInf.txt', 'a')
    html = getHtml(urlstr)
    data=getdata(html)
    nowtime = datetime.datetime.now()
    shijian = nowtime.strftime('%H:%M:%S')
    in_file.write(shijian + str(data) + '\n')
    humidity=float(list(data[0])[1])
    cloudage=float(list(data[0])[4])
    print (u'时间:',shijian,'   ',u'湿度:',humidity,'   ',u'云量:',cloudage)
    if humidity >= 70 or cloudage >= 7:
        if pygame.mixer.music.get_busy():
            x=1
        else:
            pygame.mixer.music.play(loops=10)
    else:
        if  pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    in_file.close()
    time.sleep(60)

