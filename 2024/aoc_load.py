import requests
import os

from dotenv import load_dotenv

load_dotenv()

class aoc_input:
	def __init__(self, day_nr):
		self.name = "AoC Loader"
		self.session = os.getenv("session_cookie")
		self.day = day_nr
		self.year = 2024
	
	def loader(self):
		url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
		cookie = {"session": self.session}
		response = requests.get(url, cookies=cookie)

		if response.status_code == 200:
			return response.text
		else:
			raise ConnectionError	
