from selenium import webdriver
import requests
import json
import pandas as pd

def write_comments_csv(unit_list, student_ID_list, time_list, comment_list, filename):
	df = pd.DataFrame()
	df["unit"] = unit_list
	df["student_ID"] = student_ID_list
	df["time"] = time_list
	df["comment"] = comment_list
	df.to_csv(filename + '.csv', index=False, encoding="utf-8")
