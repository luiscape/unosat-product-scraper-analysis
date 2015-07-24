#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item
from unosat_analysis.download import FetchPackageList
from unosat_analysis.download import FetchResourceInfo


def DownloadAndProcess(verbose=True, **kwargs):
  '''Download and process the packages from UNOSAT.'''

  #
  # Assemble resource data from HDX.
  #
  try:
    package_list = FetchPackageList('un-operational-satellite-appplications-programme-unosat')

    package_data = []
    for package in package_list:
      if verbose:
        print '%s Fetching data for: %s' % (item('prompt_bullet'), package)
      package_data.append(FetchResourceInfo(package))
      if kwargs.get('test'):
        break

    return package_data

  except Exception as e:
    print e
    return False


if __name__ == '__main__':
  d = DownloadAndProcess(test=True)
  print d
