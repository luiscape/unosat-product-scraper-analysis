#!/usr/bin/python
# -*- coding: utf-8 -*-

# system
import os
import sys
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(os.path.join(dir, 'scripts'))

# testing
import mock
import unittest
from mock import patch

# program
import unosat_analysis.process as Process
import unosat_analysis.download as Download


class CheckQueryFunctions(unittest.TestCase):
  '''Unit tests checking if the collector is working as expected.'''

  #
  # Organization queries.
  #
  def test_query_hdx(self):
    assert Download.FetchPackageList('foo') == False
    assert Download.FetchPackageList('hdx') != False

  def test_json_processing(self):
    d = Download.FetchPackageList('hdx')
    assert type(d) == list

  #
  # Package queries.
  #
  def test_query_hdx(self):
    assert Download.FetchResourceInfo('foo') == False

  def test_package_query(self):
    i = 'geodata-of-damage-assessment-of-sanaa-city-sanaa-governorate-yemen-june-03-2015'
    d = Download.FetchResourceInfo(i)
    assert type(d) == list


class CheckProcessFunctions(unittest.TestCase):
  '''Tests to check if the whole download program works.'''

  def test_download_wrapper(self):
    l = ['foo', 'bar']
    assert Process.DownloadAndProcess(l) != False
