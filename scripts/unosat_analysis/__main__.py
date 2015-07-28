#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from export import WriteOutput
from config.load import LoadConfig
from process import DownloadAndProcess
from utilities.prompt_format import item


def Main():
  '''Program wrapper.'''
  
  #
  # Fetch resource list.
  # And conduct analysis.
  # param: delete_files will delete each file after download.
  # param: test will the whole analysis on a single dataset
  #
  resource_list = DownloadAndProcess(delete_files=True, test=False)
  if resource_list == False:
  	print '%s Analysis failed.' % item('prompt_error')
  	return False

  #
  # Write output to disk.
  #
  if WriteOutput(data=resource_list, write_json=True, write_csv=True) == False:
  	print '%s Analysis failed.' % item('prompt_error')
  	return False


  print '%s Analysis finished successfully.' % item('prompt_success')
  return True


if __name__ == '__main__':
  Main()