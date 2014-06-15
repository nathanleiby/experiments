"""
Fetches all of yours tasks.

Usage:

- triage
- a wunderlist username/password combo

"""
import datetime
from wunderpy import Wunderlist
import argparse
import sys
from pprint import pprint
import json
from collections import OrderedDict

def get_args():
  """ Returns (username, password) tuple """
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('--username', dest='username')
  parser.add_argument('--password', dest='password')

  args = parser.parse_args()
  return (args.username, args.password)

def connect_to_wunderlist(username, password):
  """ Returns a Wunderlist connection
  param: username - WL username
  param: password - WL password
  """
  print "Connecting to Wunderlist..."
  wunderlist = Wunderlist()
  wunderlist.login(username, password)
  wunderlist.update_lists()  # you have to run this first, before you do anything else
  return wunderlist

def today(): return (datetime.date.today()).isoformat()
def tomorrow(): return (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
def inOneWeek(): return (datetime.date.today() + datetime.timedelta(days=7)).isoformat()
def inOneMonth(): return (datetime.date.today() + datetime.timedelta(days=30)).isoformat()

def main():
  """
    Usage: python triage.py --username=x --password=y
  """
  due_date_options = OrderedDict()
  due_date_options['Today'] = today
  due_date_options['Tomorrow'] = tomorrow
  due_date_options['In a Week'] = inOneWeek
  due_date_options['In a Month'] = inOneMonth

  print today()
  print tomorrow()
  print inOneMonth()

  username, password = get_args()
  wunderlist = connect_to_wunderlist(username, password)
  print "Getting all tasks"
  for l in wunderlist.lists:
    for task in l.tasks:
      print("")
      pprint(task)
      print("Due when?")
      # Tell user the options
      for idx, value in enumerate(due_date_options.keys()):
        print( "{}. {}".format(str(idx+1), value) )
      user_text = raw_input()

      # Process the users input.
      if user_text == '':
        print "Skipping..."
      else:
        # If matches a due date option, update the due date
        due_date_was_updated = False
        for idx, value in enumerate(due_date_options.keys()):
          if user_text == str(idx+1):
            due_date_iso = due_date_options[value]()
            # def update_task_due_date(self, task_title, due_date, recurrence_count=1, list_title="inbox"):
            wunderlist.update_task_due_date(task.info['title'], due_date_iso, recurrence_count=1, list_title='inbox')
            print "Due {}".format(value)
            due_date_was_updated = True
            break

        # Otherwise, rename task per user input
        if not due_date_was_updated:
          new_title = user_text
          print "Updating title to '{}'".format(new_title)
          are_you_sure = None
          while are_you_sure not in ['y', 'n']:
            are_you_sure = raw_input("Are you sure? [y/n]")

          if are_you_sure == 'y':
            # update_task_title(self, task_title, new_title, list_title="inbox"):
            wunderlist.update_task_title(task.info['title'], new_title, list_title='inbox')
          else:
            print "(Skipping title change)"



if __name__ == "__main__":
  main()
