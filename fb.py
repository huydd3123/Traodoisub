import re
from time import sleep

#Facebook
# 0: loi nhiem vu
# 1: thanh cong
# 2: block
# 3: cookie die

class FaceBook():
	def like_post(self, driver, idfb, idjob):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(2)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebook.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3
				else:
					return 0
			# //////////////
		
			xpath = f'//*[@id="actions_{idjob}"]/table/tbody/tr/td[1]/a'
			driver.find_element_by_xpath(xpath).click()
			sleep(2)
			data = driver.page_source
			check = re.search('hãy cho chúng tôi biết', data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def reaction_post(self, driver, idfb, idjob, reaction):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(2)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebook.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3
				else:
					return 0
			# /////////////
		
			xpath1 = f'//*[@id="actions_{idjob}"]/table/tbody/tr/td[2]/a'
			driver.find_element_by_xpath(xpath1).click()
			sleep(1)
			lstRea = {"LOVE": 2, "HAHA": 4, "ANGRY": 7, "WOW": 5, "SAD": 6, "CARE": 3}
			xpath2 = f'//*[@id="root"]/table/tbody/tr/td/ul/li[{lstRea[reaction]}]'
			driver.find_element_by_xpath(xpath2).click()
			sleep(2)
			data = driver.page_source
			check = re.search("hãy cho chúng tôi biết", data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def follow_user(self, driver, idfb, idjob):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(1)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebook.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3 #cookie die
				else:
					return 0 #loai
			# //////////////
		
			xpath = '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/a'
			# driver.find_element_by_xpath(xpath).click()
			driver.find_element_by_link_text("Theo dõi").click()
			sleep(2)
			data = driver.page_source
			check = re.search("hãy cho chúng tôi biết", data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def join_group(self, driver, idfb, idjob):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(2)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebok.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3
				else:
					return 0
			# //////////////
		
			xpath = '//*[@id="root"]/div[1]/form/input[3]'
			driver.find_element_by_xpath(xpath).click()
			sleep(2)
			data = driver.page_source
			check = re.search('hãy cho chúng tôi biết', data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def comment_post(self, driver, idfb, idjob, content):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(2)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebok.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3
				else:
					return 0
			# //////////////
		
			xpath = '//*[@id="composerInput"]'
			driver.find_element_by_xpath(xpath).send_keys(content)
			driver.find_element_by_css_selector('input[value="Bình luận"]').click()
			sleep(2)
			data = driver.page_source
			check = re.search('hãy cho chúng tôi biết', data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def share_post(self, driver, idfb, idjob):
		url = f"https://mbasic.facebook.com/{idjob}"
		driver.get(url)
		sleep(2)
		try:
			# kiểm tra cookie sống hay không
			data = driver.page_source
			check = re.search(idfb, data)
			if check == None:
				driver.get("https://mbasic.facebok.com/")
				sleep(2)
				data = driver.page_source
				check = re.search('query', data)
				if check == None:
					return 3
				else:
					return 0
			# //////////////
		
			css_selector = f'#actions_{idjob} > table > tbody > tr > td:last-child'
			driver.find_element_by_css_selector(css_selector).click()
			# driver.find_element_by_link_text("Chia sẻ").click()
			xpath = '//*[@id="composer_form"]/input[18]'
			driver.find_element_by_xpath(xpath).click()
			sleep(2)
			data = driver.page_source
			check = re.search('hãy cho chúng tôi biết', data)
			if check != None: 
				return 2 #block
			else:
				return 1
		except:
			return 0

	def evaluate_page(self, driver, idjob):
		url = f"https://www.facebook.com/{idjob}"
		driver.get(url)

