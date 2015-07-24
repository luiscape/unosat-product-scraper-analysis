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


def DownloadAndProcess(resource_list, **kwargs):
  '''Download and process the packages from UNOSAT.'''

  print 'nothing yet.'
  return False
