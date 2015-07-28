#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from config.load import LoadConfig
from utilities.prompt_format import item

def FetchPackageList(organization_id, verbose=False, **kwargs):
  '''Query HDX for a list of datasets that belong to an organization.'''

  #
  # Fetch configuration.
  #
  if kwargs.get('config_file') is not None:
    config = LoadConfig(kwargs.get('config_file'))
  else:
    config = LoadConfig()  # default: dev.json

  header = { 'X-CKAN-API-Key': config['hdx_key'] , 'content-type': 'application/json' }
  u = config['hdx_site'] + '/api/action/organization_show?id=' + organization_id

  try:

    #
    # If not production, we need to
    # add simple HTTP authorization.
    #
    if config['production']:
      r = requests.get(u, verify=True)  # turns off SSL certificate verification.

    else:
      r = requests.get(u, auth=(config['auth'][0], config['auth'][1]), verify=True)

  except Exception as e:
    print '%s There was a connection error. Host %s is now known.' % (item('prompt_error'), u)
    return False

  if r.status_code != 200:
    print '%s HDX query returned an error: "%s"' % (item('prompt_error'), r.json()['error']['message'])
    return False

  else:

    #
    # Assembling a list of packages
    # and returning.
    #
    data = r.json()
    dataset_array = [ name['name'] for name in data['result']['packages'] ]
    return dataset_array



def FetchResourceInfo(package_id, preferred_format='ZIPPED SHAPEFILE', verbose=False, **kwargs):
  '''Query HDX for a list of datasets that belong to an organization.
     Only fetches resources that match a preferred file format.'''

  #
  # Fetch configuration.
  #
  if kwargs.get('config_file') is not None:
    config = LoadConfig(kwargs.get('config_file'))
  else:
    config = LoadConfig()  # default: dev.json

  header = { 'X-CKAN-API-Key': config['hdx_key'] , 'content-type': 'application/json' }
  u = config['hdx_site'] + '/api/action/package_show?id=' + package_id

  try:

    #
    # If not production, we need to
    # add simple HTTP authorization.
    #
    if config['production']:
      r = requests.get(u, verify=True)  # turns-off SSL certificate verification

    else:
      r = requests.get(u, auth=(config['auth'][0], config['auth'][1]), verify=True)

  except Exception as e:
    print '%s There was a connection error. Host %s is now known.' % (item('prompt_error'), u)
    return False

  if r.status_code != 200:
    print '%s HDX query returned an error: "%s"' % (item('prompt_error'), r.json()['error']['message'])
    return False

  else:

    #
    # Fetching URL information
    # from all organization packages.
    #
    data = r.json()
    package_array = []
    for resource in data['result']['resources']:
      if resource['format'] == preferred_format:
        d = { 'resource_id': resource['id'], 'dataset_id': package_id, 'resource_url': resource['url'] }
        package_array.append(d)

    return package_array




if __name__ == '__main__':
  print 'nothing'
