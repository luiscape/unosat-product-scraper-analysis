#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from zipfile import ZipFile
from utilities.prompt_format import item
from unosat_analysis.download import FetchPackageList
from unosat_analysis.download import FetchResourceInfo


def DownloadResource(url, default_dir='data', verbose=True):
  '''Downloading a resource from HDX.'''
  
  #
  # Assemble file path.
  #
  file_name = os.path.basename(url)
  file_path = os.path.join('data', file_name)
  if verbose:
    print '%s Downloading resource %s' % (item('prompt_bullet'), file_name)
  
  #
  # Make request.
  #
  try:
    r = requests.get(url)
    if r.status_code == 200:
      with open(file_path, 'wb') as f:
        for chunk in r:
          f.write(chunk)

    if verbose:
      print '%s File %s was downloaded successfully.' % (item('prompt_bullet'), file_name)

  except Exception as e:
    if verbose:
      print e
      print '%s File %s failed to download.' % (item('prompt_error'), file_name)

    return False



def FetchZipInformation(package_dictionary, verbose=False):
  '''Collects and reports information from a ZIP package.'''

  file_path = os.path.join('data', os.path.basename(package_dictionary['resource_url']))
  print '%s Fetching ZIP package information for %s' % (item('prompt_bullet'), file_path)
  
  #
  # Collect information for a file
  # on a dictionary and return.
  #
  try:
    with ZipFile(file_path, 'r') as f:
      file_info = f.infolist()

      i = 0
      for file in file_info:
        if file.filename.endswith('shp'):
          if verbose:
            print file.filename
          i += 1


      package_dictionary['file_path'] = file_path
      package_dictionary['n_files'] = len(file_info)
      package_dictionary['n_shapefiles'] = i

  except Exception as e:
    print '%s Failed to read ZIP package %s. Skipping.' % (item('prompt_error'), file_path)

    #
    # Generating missing data.
    #
    package_dictionary['file_path'] = file_path
    package_dictionary['n_files'] = None
    package_dictionary['n_shapefiles'] = None

  
  return package_dictionary
    



def AssemblePackageData(verbose=True, **kwargs):
  '''Assembles the package data from a series of datasets.'''

  #
  # Assemble resource data from HDX.
  #
  try:
    package_list = FetchPackageList('un-operational-satellite-appplications-programme-unosat')

    package_data = []
    for package in package_list:
      if verbose:
        print '%s Fetching metadata for: %s' % (item('prompt_bullet'), package)
        d = FetchResourceInfo(package)
      package_data += d
      if kwargs.get('test'):
        break

    return package_data

  except Exception as e:
    print e
    print '%s Failed to assemble package data.' % item('prompt_error')
    return False



def DownloadAndProcess(delete_files=True, verbose=False, **kwargs):
  '''Download and process the packages from UNOSAT.'''
  
  try:
    results = []
    a = AssemblePackageData(**kwargs)
    for package in a:

      #
      # Download.
      #
      DownloadResource(package['resource_url'])
      
      #
      # Analyze.
      #
      b = FetchZipInformation(package)
      results.append(b)
      
      #
      # Clean downloaded file.
      #
      if delete_files:
        f = os.path.basename(b['resource_url'])
        os.remove(os.path.join('data', f))

    return results
  
  except Exception as e:
    print '%s Failed to download and process files.' % item('prompt_error')
    print e
    return results

    
