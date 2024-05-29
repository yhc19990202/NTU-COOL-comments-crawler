from selenium import webdriver
import requests
import json
from open_chrome_driver import open_chrome_driver
from login_COOL import login_COOL
from copy_cookies import copy_cookies
from get_source_IDs import get_course_slides_IDs, get_course_video_IDs
from bs4 import BeautifulSoup
import time, getpass
import re


def get_slides_comments(driver, session, course_id, slides_id):
    manage_url = "https://cool.ntu.edu.tw/courses/" + str(course_id) + "/external_tools/124"
    # video_url = "https://symphony.dlc.ntu.edu.tw/api/v1/courses/23970/documents/2202/annotations"
    comments_url = "https://symphony.dlc.ntu.edu.tw/api/v1/courses/" + str(course_id) + "/documents/" + str(slides_id) + "/annotations"
    driver.get(manage_url)
    # driver.get(video_url)
    driver.get(comments_url)
    session = copy_cookies(session, driver)
    comments_json = json.loads( session.get(comments_url).text )
    comments_json = comments_json["annotations"]

    comments = []
    for comment in comments_json:
        if comment["deleted"] is False:
            # print(comment)
            content = BeautifulSoup(comment["content"]).get_text()
            user = comment["user_id"]
            time = re.search('.*T', comment["created_at"]).group()[:-1]
            comments.append({"time": time, "user": user, "content": content})
            for c in comment["comments"]:                
                content = BeautifulSoup(c["content"]).get_text()
                user = c["user_id"]
                time = re.search('.*T', c["created_at"]).group()[:-1]
                comments.append({"time": time, "user": user, "content": content})
    return comments


def get_video_comments(driver, session, course_id, video_id):
    manage_url = "https://cool.ntu.edu.tw/courses/" + str(course_id) + "/external_tools/29"
    video_url = "https://cool-video.dlc.ntu.edu.tw/api/courses/" + str(course_id) + "/videos/" + str(video_id) + "/view"
    comments_url = "https://cool-video.dlc.ntu.edu.tw/api/course-videos/" + str(video_id) + "/comments"
    driver.get(manage_url)
    driver.get(video_url)
    driver.get(comments_url)
    session = copy_cookies(session, driver)
    comments_json = json.loads( session.get(comments_url).text )

    comments = []
    for comment in comments_json:
        if comment["isDeleted"] is False:
            content = BeautifulSoup(comment["content"]).get_text()
            user = comment["creatorId"]
            time = re.search('.*T', comment["createdAt"]).group()[:-1]
            comments.append({"time": time, "user": user, "content": content})
    return comments


if __name__ == '__main__':
    course_id = 23970
    driver = open_chrome_driver()
    login_COOL(driver)
    session = requests.session()
    sorted_slides_list = get_course_slides_IDs(driver, session, course_id)
    for slides in sorted_slides_list:
        comments = get_slides_comments(driver, session, course_id, slides["ID"])
        print(slides["display_name"])
        print(comments)
        break

    sorted_videos = get_course_video_IDs(driver, session, course_id)
    for video in sorted_videos:
        comments = get_video_comments(driver, session, course_id, video["ID"])
        print(video["title"])
        print(comments)
        break
