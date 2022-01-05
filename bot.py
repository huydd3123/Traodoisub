from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import os
import random
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fb import FaceBook as FB
from tds import TraoDoiSub as TDS

# Khoi dong trinh duyet

def initOptions():
	options = Options()

	options.add_argument(f'user-data-dir={os.getcwd()}\\profile')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox')
	options.add_argument('--log-level 3')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	options.add_argument("--window-size=400,500")
	options.add_argument('--app=https://mbasic.facebook.com/')

	return options

def initDriver(options):
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)
	return driver

def addCookie(driver, cookie):
	driver.delete_all_cookies()
	cookieList = [
		{"name": "c_user", "value": re.findall(r'c_user=(.*?);', cookie)[0]},
		{"name": "xs", "value": re.findall(r'xs=(.*?);', cookie)[0]}
	]
	for ck in cookieList:
		driver.add_cookie(ck)
	return driver

# làm nhiem vu
def make_job_follow(driver, token, idfb):
	list_job = TDS().get_job_follow(token)
	# print(list_job)
	if len(list_job) == 0: return 1
	count = 0
	max_make = random.randint(2, 4)
	for job in list_job:
		idjob = job['id']
		# print(idjob)
		res = FB().follow_user(driver, idfb, idjob)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block FOLLOW")
			return 2
		else:
			res = TDS().rec_job_follow(token, idjob)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1

def make_job_like(driver, token, idfb):
	list_job = TDS().get_job_like(token)
	# print(list_job)
	if len(list_job) == 0: return 1
	count = 0
	max_make = random.randint(2, 4)
	count_error = 0
	for job in list_job:
		idjob = job['id']
		# print(idjob)
		res = FB().like_post(driver, idfb, idjob)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block LIKE")
			return 2
		else:
			res = TDS().rec_job_like(token, idjob)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1

def make_job_reaction(driver, token, idfb):
	list_job = TDS().get_job_reaction(token)
	if len(list_job) == 0: return 1
	# print(list_job)
	count = 0
	max_make = random.randint(2, 4)
	for job in list_job:
		idjob = job['id']
		reaction = job['type']
		res = FB().reaction_post(driver, idfb, idjob, reaction)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block REACTION")
			return 2
		else:
			res = TDS().rec_job_reaction(token, idjob, reaction)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1

def make_job_comment(driver, token, idfb):
	list_job = TDS().get_job_comment(token)
	if len(list_job) == 0: return 1
	# print(list_job)
	count = 0
	max_make = random.randint(2, 4)
	for job in list_job:
		idjob = job['id']
		content = job['msg']
		res = FB().comment_post(driver, idfb, idjob, content)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block COMMENT")
			return 2
		else:
			res = TDS().rec_job_comment(token, idjob)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				with open(f'Log/{idfb}.txt', 'a', encoding='utf8') as f:
					f.write(content + '\n')
					f.close
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1

def make_job_share(driver, token, idfb):
	list_job = TDS().get_job_share(token)
	if len(list_job) == 0: return 1
	# print(list_job)
	count = 0
	max_make = random.randint(2, 4)
	for job in list_job:
		idjob = job['id']
		res = FB().share_post(driver, idfb, idjob)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block SHARE")
			return 2
		else:
			res = TDS().rec_job_share(token, idjob)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1

def make_job_group(driver, token, idfb):
	list_job = TDS().get_job_group(token)
	if len(list_job) == 0: return 1
	# print(list_job)
	count = 0
	max_make = random.randint(2, 4)
	for job in list_job:
		idjob = job['id']
		res = FB().join_group(driver, idfb, idjob)
		if res == 3:
			print("COOKIE DIE")
			return 3
		elif res == 2:
			print("block GROUP")
			return 2
		else:
			res = TDS().rec_job_group(token, idjob)
			if "error" in res:
				print(f"\t>[error: {idjob}]<")
				continue
			else:
				xu = res['data']['xu']
				msg = res['data']['msg']
				print(f'\t[success: {idjob}|{msg}|{xu}] <<wait 5s>>')
				count += 1
				if count >= max_make: break
				sleep(5)
	return 1


def main():
	options = initOptions()
	driver = initDriver(options)
	# driver.get("https://mbasic.facebook.com/home.php")

	token = "TDSQfikjclZXZzJiOiIXZ2V2ciwiIyATMiV3c5VHaiojIyV2c1Jye"

	list_acc_make = {}
	while True:
		for fn in os.listdir('cookie'):
			fpath = f'cookie/{fn}'
			cookie = open(fpath, 'r').read()
			idfb = fn.split('.')[0]
			# print(idfb)

			acc = f"acc_{idfb}"
			# print(acc)
			if acc not in list_acc_make:
				list_acc_make[acc] = ["FOLLOW", "LIKE", "REACTION", "COMMENT", "SHARE", "GROUP"]

			addCookie(driver, cookie)
			res = TDS().cau_hinh(token, idfb)
			print(f"[[[[[ Cau hinh thanh cong: {res['data']['id']} ]]]]]")
			# print(res)
			if 'FOLLOW' in list_acc_make[acc]:
				print("\t [FOLLOW]")
				res = make_job_follow(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('FOLLOW')

			if 'LIKE' in list_acc_make[acc]:
				print("\t [LIKE]")
				res = make_job_like(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('LIKE')

			if 'REACTION' in list_acc_make[acc]:	
				print("\t [REACTION]")
				res = make_job_reaction(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('REACTION')

			if 'COMMENT' in list_acc_make[acc]:	
				print("\t [COMMENT]")
				res = make_job_comment(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('COMMENT')

			if 'SHARE' in list_acc_make[acc]:
				print("\t [SHARE]")
				res = make_job_share(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('SHARE')

			if 'GROUP' in list_acc_make[acc]:
				print("\t [GROUP]")
				res = make_job_group(driver, token, idfb)
				if res == 2 or res == 3:
					list_acc_make[acc].remove('GROUP')
			print("Chuyen nick sau 10s")
			sleep(10)


	
if __name__ == '__main__':
	main()