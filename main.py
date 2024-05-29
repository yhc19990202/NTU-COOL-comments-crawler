from selenium import webdriver
import requests
import json
from open_chrome_driver import open_chrome_driver
from login_COOL import login_COOL
from get_students_info import get_students_info
from get_source_IDs import get_course_video_IDs, get_course_slides_IDs
from get_comments import get_video_comments, get_slides_comments
from write_comments_csv import write_comments_csv

course_id = input("Please input the course_id: ")
driver = open_chrome_driver()
login_COOL(driver)

session = requests.session()
ID_students, students_name = get_students_info(driver, session, course_id)
print(ID_students)
print(students_name)

unit_list = []
student_ID_list = []
time_list = []
comment_list = []

comment_type = input("Videos / Slides? (v/s): ")
if comment_type == "v":
    sorted_videos = get_course_video_IDs(driver, session, course_id)
    for video in sorted_videos:
        comments = get_video_comments(driver, session, course_id, video["ID"])
        for comment in comments:
            student_ID = []
            try:
                student_ID = ID_students[comment["user"]]
            except:
                continue
            unit_list.append(video["title"])
            student_ID_list.append(student_ID)
            time_list.append(comment["time"])
            comment_list.append(comment["content"])
    write_comments_csv(unit_list, student_ID_list, time_list, comment_list, "video_comments")
if comment_type == "s":
    sorted_slides_list = get_course_slides_IDs(driver, session, course_id)
    for slides in sorted_slides_list:
        comments = get_slides_comments(driver, session, course_id, slides["ID"])
        for comment in comments:
            student_ID = []
            try:
                student_ID = ID_students[comment["user"]]
            except:
                continue
            unit_list.append(slides["display_name"])
            student_ID_list.append(student_ID)
            time_list.append(comment["time"])
            comment_list.append(comment["content"])
    write_comments_csv(unit_list, student_ID_list, time_list, comment_list, "slides_comments")
