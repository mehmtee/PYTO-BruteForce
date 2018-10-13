#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:08:38 2018

@author: root1
"""

from bruteforce import Brute

print("""
      

 _______          _________ _______ 
(  ____ )|\     /|\__   __/(  ___  )
| (    )|( \   / )   ) (   | (   ) |
| (____)| \ (_) /    | |   | |   | |
|  _____)  \   /     | |   | |   | |
| (         ) (      | |   | |   | |
| )         | |      | |   | (___) |
|/          \_/      )_(   (_______)
                                    
                                                        


C0ded by mehmtee
""")


user = input('Username.txt dosyasının adını giriniz ')
passs = input('Password.txt dosyasının adını giriniz ')
url = input('Url adresini giriniz')

brute = Brute(user,passs,url)


brute.Start()


print(brute.u_name)
print(brute.p_name)
