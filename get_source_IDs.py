from selenium import webdriver
import requests
import json
from open_chrome_driver import open_chrome_driver
from login_COOL import login_COOL
from copy_cookies import copy_cookies
import time, getpass

def get_course_video_IDs(driver, session, course_id):
    manage_url = "https://cool.ntu.edu.tw/courses/" + str(course_id) + "/external_tools/29"
    video_list_url = "https://cool-video.dlc.ntu.edu.tw/api/courses/" + str(course_id) + "/videos"
    driver.get(manage_url)
    driver.get(video_list_url)
    session = copy_cookies(session, driver)
    videos_json = json.loads( session.get(video_list_url).text )

    videos = []
    for video in videos_json:
        videos.append({"title": video["title"], "ID": video["id"]})
    sorted_videos = sorted(videos, key=lambda x: x["title"])
    return sorted_videos


def get_course_slides_IDs(driver, session, course_id):
    print('get_course_slides_IDs')
    manage_url = "https://cool.ntu.edu.tw/courses/" + str(course_id) + "/external_tools/124"
    slides_list_url = "https://symphony.dlc.ntu.edu.tw/api/v1/courses/" + str(course_id) + "/documents"
    driver.get(manage_url)
    driver.get(slides_list_url)
    session = copy_cookies(session, driver)
    slides_json = json.loads( session.get(slides_list_url).text )

    slides_list = []
    for slides in slides_json:
        slides_list.append({"display_name": slides["display_name"], "ID": slides["id"]})
    sorted_slides_list = sorted(slides_list, key=lambda x: x["display_name"])
    return sorted_slides_list


if __name__ == '__main__':
    course_id = 23970
    driver = open_chrome_driver()
    login_COOL(driver)
    session = requests.session()
    sorted_videos = get_course_video_IDs(driver, session, course_id)
    print(sorted_videos)
    sorted_slides_list = get_course_slides_IDs(driver, session, course_id)
    print(sorted_slides_list)
