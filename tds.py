from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import os
# import random
import json

class TraoDoiSub():
	def __init__(self):
		self.ses = requests.session()

	# Lấy thông tin acc
	def get_profile(self, token):
		url = f'https://traodoisub.com/api/?fields=profile&access_token={token}'
		res = self.ses.get(url)
		data = res.json()
		return data

	# Dat nick cau hinh
	def cau_hinh(self, token, idfb):
		url = f"https://traodoisub.com/api/?fields=run&id={idfb}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	# Lấy danh sách nhiệm vụ
	def get_job_follow(self, token):
		url = f"https://traodoisub.com/api/?fields=follow&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_like(self, token):
		url = f"https://traodoisub.com/api/?fields=like&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_reaction(self, token):
		url = f"https://traodoisub.com/api/?fields=reaction&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_comment(self, token):
		url = f"https://traodoisub.com/api/?fields=comment&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_share(self, token):
		url = f"https://traodoisub.com/api/?fields=share&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_reactcmt(self, token):
		url = f"https://traodoisub.com/api/?fields=reactcmt&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_group(self, token):
		url = f"https://traodoisub.com/api/?fields=group&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def get_job_page(self, token):
		url = f"https://traodoisub.com/api/?fields=page&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data
	# Nhận tiền
	def rec_job_follow(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=FOLLOW&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_like(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=LIKE&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_reaction(self, token, idjob, reaction):
		url = f"https://traodoisub.com/api/coin/?type={reaction}&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_reactcmt(self, token, idjob, reaction):
		url = f"https://traodoisub.com/api/coin/?type={reaction}&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_comment(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=COMMENT&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_share(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=SHARE&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_group(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=GROUP&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data

	def rec_job_page(self, token, idjob):
		url = f"https://traodoisub.com/api/coin/?type=PAGE&id={idjob}&access_token={token}"
		res = self.ses.get(url)
		data = res.json()
		return data


def  main():
	token = "TDSQfikjclZXZzJiOiIXZ2V2ciwiIyATMiV3c5VHaiojIyV2c1Jye"
	idfb = "100075907172959"
	TDS = TraoDoiSub()
	# TDS.cau_hinh(token, idfb)
	# get_profile(self, token)
	
	print(TDS.get_job_follow(token))
	# print("================")
	# TDS.get_job_like(token)
	# print("================")
	# print(TDS.get_job_reaction(token))
	# print("================")
	# print(TDS.get_job_comment(token))
	# print("================")
	# print(TDS.get_job_share(token))
	# print("================")
	# TDS.get_job_group(token)
	# print("================")
	# TDS.get_job_page(token)
	# print("================")


	# TDS.get_job_reactcmt(token)
	# idjob = '453725923091183'
	# rec_job_comment(self, token, idjob)
	idjob = "248398010752893"
	reaction = "LOVE"
	# TDS.rec_job_reaction(token, idjob, reaction)
	# TDS.rec_job_share(token, idjob)
	# TDS.get_job_group(token)
	# TDS.rec_job_group(token, idjob)
	# TDS.get_job_comment(token)
	# TDS.rec_job_comment(token, idjob)
	# TDS.rec_job_share(token, idjob)

if __name__ == '__main__':
	main()