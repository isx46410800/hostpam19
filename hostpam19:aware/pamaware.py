# !/usr/bin/python
# -*-coding: utf-8-*-
import pam
p=pam.pam()
userName=input("Usuari: ")
userPasswd=input("Passwd: ")
p.authenticate(userName, userPasswd)
print('{} {}'.format(p.code,p.reason))
if p.code == 0:
	print ("Usuari UNIX valid")
else:
	print ("Error autenticacio")
