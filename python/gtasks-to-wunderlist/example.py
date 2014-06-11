from datetime import datetime
from wunderpy import Wunderlist
import argparse
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--username', dest='username')
parser.add_argument('--password', dest='password')

args = parser.parse_args()
username = args.username
password = args.password

w = Wunderlist()
w.login(username, password)
w.update_lists()  # you have to run this first, before you do anything else

# print w
print w.__dict__

raw_input("About to create list 'test'...")
w.add_list("test")  # make a new list called "test"
raw_input("About to add task 'test wunderpy'...")
due = datetime.now().isoformat()
w.add_task("test wunderpy", list_title="test", note="a note",
           due_date=due, starred=True)  # add a task to it
raw_input("About to complete task 'test wunderpy'...")
w.complete_task("test wunderpy", "test")  # complete it
raw_input("About to delete task 'test wunderpy'...")
w.delete_task("test wunderpy", "test")  # and delete it
raw_input("About to delete list 'test'...")
w.delete_list("test")  # and delete the list
print "Done!"