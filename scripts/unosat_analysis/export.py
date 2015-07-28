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
      output_path = os.path.join(directory, 'analysis.csv')
      with open(output_path, 'wb') as f:
        writter = csv.writer(f, delimiter=',', quotechar='"')

        i = 0
        for row in data:
          if i == 0:
            writter.writerow([ k for k in row.keys() ])
            writter.writerow([ k for k in row.values() ])
            i += 1

          else:
            writter.writerow([ v for v in row.values() ])
            i += 1
            f.flush()
    
    except Exception as e:
      print '%s Could not write CSV file.' % item('prompt_error')
      print e
      return False



def WriteCSV(json_path='output/analysis.json', verbose=True):
  '''Writes a CSV output based on a JSON input.'''
  
  #
  # Configuring path.
  #
  data_dir = os.path.split(json_path)[0]
  output_path = os.path.join(data_dir, 'analysis.csv')

  #
  # Read json file. 
  #
  try:
    with open(json_path) as data_file:    
      data = json.load(data_file)

  except Exception as e:
    print '%s Could not ope JSON file.' % item('prompt_error')
    print e
    return False
  
  #
  # Writting file.
  #
  try:
    with open(output_path, 'wb') as f:
      writter = csv.writer(f, delimiter=',', quotechar='"')

      i = 0
      for row in data:
        if i == 0:
          writter.writerow([ k for k in row.keys() ])
          writter.writerow([ k for k in row.values() ])
          i += 1

        else:
          writter.writerow([ v for v in row.values() ])
          i += 1
          f.flush()
  
  except Exception as e:
    print '%s Could not write CSV file.' % item('prompt_error')
    print e
    return False

