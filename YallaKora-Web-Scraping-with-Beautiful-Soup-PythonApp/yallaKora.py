import requests
from bs4 import BeautifulSoup
import csv

date = input('please enter the date in the follwing format MM/DD/YYYY: ')
page =requests.get(f'https://www.yallakora.com/match-center/?date={date}')

soup = BeautifulSoup(page.content, 'html.parser')