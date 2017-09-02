# coding=utf-8
"""
MAIN FILE
Main file that downloads several files using a user list.

Author: Pablo Pizarro R. @ppizarror.com
Date: August 2017
Licence:
    The MIT License (MIT)
    Copyright 2017 Pablo Pizarro R.

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the Software
    is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Library import
from __future__ import print_function
from homework_lib import *
import json

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
    line = line.replace('\xef\xbb\xbf', '').split('\t')
    if len(line) < 2:
        continue
    if line[1] is '':
        continue
    if cfg['NUM_USER_ADD']:
        if line[0] is not '':
            lastd = int(line[0])
        else:
            lastd += 1
        users.append([str(lastd).zfill(2), line[1], line[2], is_yes(line[3]), is_yes(line[4])])
    else:
        if line[0] == '':
            line[0] = '&nbsp;'
        users.append([line[0], line[1], line[2], is_yes(line[3]), is_yes(line[4])])
data.close()

# Request homework name
if not TEST:
    # noinspection PyCompatibility
    homework = raw_input('NEW HOMEWORK NAME: ')
    if homework is '':
        raise Exception('Homework name cant be empty')
else:
    homework = '01-tarea'

# Create new website archive
web = open(homework + '.html', 'w')
web.write(HEADER.format(homework, cfg['ORGANIZATION'] + homework, VERSION))
for i in users:
    if len(i[2]) > 1:
        if i[3] and i[4]:
            u_id = 'user_id_{0}'.format(md5_user(i[2]))
            u_src = DOWNLOAD_LINK.format(cfg['ORGANIZATION'], homework, i[2])
            user_src = USER_LINK.format(cfg['ORGANIZATION'], homework, i[2])
            user_github = 'http://github.com/' + i[2]
            web.write(USER_ENTRY.format(u_id, i[0], i[1], u_src, user_src, i[2], user_github))
        elif not i[3]:
            web.write(USER_ENTRY_NON_INVITED.format(i[0], i[1]))
        elif not i[4]:
            web.write(USER_ENTRY_NON_ACCEPTED.format(i[0], i[1]))
    else:
        web.write(USER_ENTRY_NON_EXISTANT.format(i[0], i[1]))
web.write(FOOTER)
web.close()
