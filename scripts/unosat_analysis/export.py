#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import json
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item


def WriteOutput(data=None, directory='output', write_json=False, write_csv=False, write_db=False, verbose=True):
  '''Writting the output of the collection function.'''

  if data == None:
    print '%s Provide data.' % item('promp_error')
    return False
   
  if write_json:
    try:
	  print '%s Writting JSON file.' % item('prompt_bullet')
	  p = os.path.join(directory, 'analysis.json')
	  with open(p, 'wb') as f:
	    json.dump(data, f)

    except Exception as e:
      print '%s Failed to write JSON.' % item('prompt_error')
      print e
      return False

  if write_csv:
    try:
      print '%s Writting CSV file.' % item('prompt_bullet')
      p = os.path.join(directory, 'analysis.csv')
      with open(p,'wb') as f:
        writter = csv.writer(f, delimiter=',', quotechar='"')
     
        i = 0
        for row in data:
          if i == 0:
            writter.writerow([ k for k in row.keys() ])
          else:
            writter.writerow([ v for v in row.values() ])
            i += 1
            myfile.flush()

    except Exception as e:
      print '%s Failed to write CSV.' % item('prompt_error')
      print e
      return False