from selenium import webdriver
import requests
import json
from open_chrome_driver import open_chrome_driver
from login_COOL import login_COOL
from copy_cookies import copy_cookies
from get_source_IDs import get_course_video_IDs
from bs4 import BeautifulSoup
import time, getpass
import re


def get_students_info(driver, session, course_id):
    manage_url = "https://cool.ntu.edu.tw/courses/" + str(course_id) + "/external_tools/29"
    user_url = "https://cool-video.dlc.ntu.edu.tw/api/courses/" + str(course_id) + "/users"
    driver.get(manage_url)
    driver.get(user_url)

    session = copy_cookies(session, driver)
    students_json = json.loads( session.get(user_url).text )
    print(students_json)
    time.sleep(1)
    ID_students = dict()
    students_name = dict()
    for student in students_json:
        student_ID = re.search('.*@', student["loginId"]).group()[:-1]
        ID = student["id"]
        name = student["name"]
        ID_students[ID] = student_ID
        students_name[student_ID] = name
    return ID_students, students_name

if __name__ == '__main__':
    course_id = 23970
    driver = open_chrome_driver()
    login_COOL(driver)
    session = requests.session()
    ID_students, students_name = get_students_info(driver, session, course_id)
    print(ID_students)
    print(students_name)
