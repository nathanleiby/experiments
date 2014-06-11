"""
given

- an input .py file from https://code.google.com/p/tasks-backup/
- a wunderlist username/password combo

"""
from datetime import datetime
from wunderpy import Wunderlist
import argparse
import sys
from pprint import pprint
import json

import data # expects local file `data.py` with backed up gtasks data
mapping = json.load(open('mappings.json')) # expects local file mappings.json

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
  w = Wunderlist()
  w.login(username, password)
  w.update_lists()  # you have to run this first, before you do anything else
  return w

def filter_gtasks(tasklists):
  print "Converting gtask tasklist into Wunderlist formatted tasks..."
  tasks_grouped_by_tasklist = {}
  for tasklist in tasklists:
    tasklist_title = rename_key(tasklist['title'])
    tasks = [
      {
        'title': remove_non_ascii(t['title']),
        'notes': remove_non_ascii(t['notes']) if 'notes' in t else '',
        'status': remove_non_ascii(t['status']),
        'tag': tasklist_title,
        'link': "Email: {} - {}".format(remove_non_ascii(t['links'][0]['description']), t['links'][0]['link']) if 'links' in t else ''
      }
      for t in tasklist['tasks'] if t['status'] == 'needsAction'
    ]
    tasks_grouped_by_tasklist[tasklist_title] = tasks
  return tasks_grouped_by_tasklist

def remove_non_ascii(s): return "".join(i for i in s if ord(i)<128)

def create_task(wunderlist, task):
  print "Creating task..."
  pprint(task)

  title = "{} {}".format(task['tag'], task['title'])
  notes = task['notes']
  if task['link'] != '':
    # only add a line break if some notes text already present
    if notes != '':
      notes += "\n"
    notes += task['link']

  wunderlist.add_task(title, note=notes)

def rename_key(key):
  """
  expects local file mappings.json
  """
  return mapping[key] if key in mapping else key

def main():
  """
    Usage: python export.py --username=x --password=y

    Expects:
      - data.py
      - mappings.json (if you want to rename between existing task list and tag names in wunderlist)
  """

  username, password = get_args()
  wunderlist = connect_to_wunderlist(username, password)
  task_groups = filter_gtasks(data.tasklists)
  for k in task_groups.keys():
    print k
    for idx, task in enumerate(task_groups[k]):
      print idx,
      create_task(wunderlist, task)
    print ""

if __name__ == "__main__":
  main()
