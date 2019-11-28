# !/usr/bin/python3
# -*-coding: utf-8-*-
#nom autor: Miguel Amorós Moret
#isx: 46410800

# Duplicates pam_permit.c
#
import pam
DEFAULT_USER = "nobody"

def pam_sm_authenticate(pamh, flags, argv):
	try:
		user = pamh.get_user(None)
	except pamh.exception, e:
		return e.pam_result
	if user == None:
	pamh.user = DEFAULT_USER
		return pamh.PAM_SUCCESS
		
def pam_sm_setcred(pamh, flags, argv):
	return pamh.PAM_SUCCESS
	
def pam_sm_acct_mgmt(pamh, flags, argv):
	return pamh.PAM_SUCCESS
	
def pam_sm_open_session(pamh, flags, argv):
	return pamh.PAM_SUCCESS
	
def pam_sm_close_session(pamh, flags, argv):
	return pamh.PAM_SUCCESS
	
def pam_sm_chauthtok(pamh, flags, argv):
	return pamh.PAM_SUCCESS
