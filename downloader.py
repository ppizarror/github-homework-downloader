# coding=utf-8
from __future__ import print_function

"""
Main file that downloads several files using a user list.
"""

# Library import
import json

# Constants
CONFIG_FILE = 'config.json'
VERSION = '0.1'

# Load configs
with open(CONFIG_FILE) as json_data:
    cfg = json.load(json_data)

# Check if organization is not empty
if cfg['ORGANIZATION'] == '':
    raise Exception('Organization cant be empty')

# Write status on console
print('HOMEWORK DOWNLOADER v{0}'.format(VERSION))
print('\tYOUR ORGANIZATION: {0}'.format(cfg['ORGANIZATION']))
print('')

# Load user list
users = []
data = open(cfg['USER_LIST'])
lastd = 0
for line in data:
    line = line.split('\t')
    if line[1] is '':
        continue
    if line[0] is not '':
        lastd = int(line[0])
    else:
        lastd += 1
    users.append([lastd, line[1], line[2]])
data.close()

# noinspection PyCompatibility
homework = raw_input('NEW HOMEWORK NAME: ')  # Request homework name
if homework is '':
    raise Exception('Homework name cant be empty')

# Create new website archive
web = open(homework + '.html', 'w')
web.close()
