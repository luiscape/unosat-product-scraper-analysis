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
import config.load as Load


class CheckLoadFunction(unittest.TestCase):
  '''Test that the load function works as expected..'''

  def test_loading_default_config_file(self):
    assert Load.LoadConfig() != False

  def test_loading_non_existing_file(self):
    assert Load.LoadConfig('xxx.json') == False
