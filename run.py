import os
import shutil

if os.path.exists(r"C:\Users\aaron\PycharmProjects\filebeat\data\registry"):
    shutil.rmtree(r"C:\Users\aaron\PycharmProjects\filebeat\data\registry")

os.chdir(r"C:\Users\aaron\PycharmProjects\filebeat")
os.system("filebeat -e -c filebeat.yml")
