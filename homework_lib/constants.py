# coding=utf-8
"""
CONSTANTS
Constants used by homework-downloader

Author: Pablo Pizarro R. @ ppizarror.com
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

# General constants
TEST = False
VERSION = '0.8.3'

# Files
CONFIG_FILE = 'config.json'
LANGS_FILE = 'lang.json'

# HTML Entries
FOOTER = """
</div>
<div id="about">
\t<div id="generatedtime">{0}</div>
\t<div id="ppizarror">
\t\t<a href="https://github.com/ppizarror/github-homework-downloader">
\t\t\t<img src="res/favicon-32x32.png" /> github-homework-downloader
\t\t</a> v{1} by
\t\t<a href="http://ppizarror.com">
\t\t\t<img src="https://avatars0.githubusercontent.com/u/12925256" /> ppizarror
\t\t</a>
\t</div>
</div>
</body>
</html>"""
HEADER = """<!DOCTYPE html>
<meta charset="UTF-8">
<!--
GITHUB-HOMEWORK-DOWNLOADER

Author: Pablo Pizarro R. @ ppizarror.com
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
-->

<html lang="{4}">
<head>
\t<title>{0}</title>
\n
\t<link rel="apple-touch-icon" sizes="180x180" href="res/apple-touch-icon.png">
\t<link rel="icon" type="image/png" sizes="32x32" href="res/favicon-32x32.png">
\t<link rel="icon" type="image/png" sizes="16x16" href="res/favicon-16x16.png">
\t<link rel="manifest" href="res/manifest.json">
\t<link rel="mask-icon" href="res/safari-pinned-tab.svg" color="#000000">
\t<link rel="shortcut icon" href="res/favicon.ico">
\t<meta name="msapplication-config" content="res/browserconfig.xml">
\t<meta name="theme-color" content="#ffffff">
\t<meta name="description" content="Created by github-homework-downloader v{2}">
\n
\t<script type="text/javascript" src="res/jquery-3.2.1.min.js"></script>
\t<script type="text/javascript" src="res/pace.min.js"></script>
\t<script type="text/javascript" src="res/js.cookie-2.1.4.min.js"></script>
\t<script type="text/javascript" src="res/progressbar.min.js"></script>
\t<script type="text/javascript" src="res/config.min.js"></script>
\t<script type="text/javascript" src="res/onload.min.js"></script>
\n
\t<link rel="stylesheet" type="text/css" href="res/style.min.css" media="screen">
\t<link rel="stylesheet" type="text/css" href="res/pace.min.css" media="screen">
\t<link rel="stylesheet" type="text/css" href="res/scrolltop.min.css" media="screen">
</head>

<body>
<a href="#" class="back-to-top" id="scrolls">Back to Top</a>
<div id="header">
\t<div id="title_page">
\t\t<a href="{1}" id="homework_name">{0}</a>
\t</div>
\t<div id="toolbar">
\t\t<div id="toolbar_button"><a href="#" id="reset_button" class="tooltip">
\t\t\t<img src="res/delete.png"/><span class="tooltiptext">{3}</span>
\t\t</a></div>
\t</div>
</div>
<div id="main_list">
"""
USER_ENTRY = """
\t<div id="{0}" class="new_user">
\t\t<div class="user_inner">
\t\t\t<div class="id_num">{1}</div>
\t\t\t<div class="entry_name"><a href="{4}" id="usernamelink">{2}</a> <a href="{6}"><b>({5})</b></a></div>
\t\t\t<a href="{7}" title="{8}" id="calendar" rel="nofollow">
\t\t\t\t<div class="entry_calendar"><img src="res/calendar.png" class="button-img" /></div>
\t\t\t</a>
\t\t\t<a href="{3}" title="{9}" id="download" user="{0}" rel="nofollow">
\t\t\t\t<div class="entry_url"><img src="res/download.png" class="button-img" /></div>
\t\t\t</a>
\t\t\t<div class="status">
\t\t\t\t<div id="progress-bar-circle"></div>
\t\t\t\t<img src="res/error.png" class="button-img" title="{10}"/>
\t\t\t\t<div id="status_date"></div>
\t\t\t</div>
\t\t</div>
\t</div>
"""
USER_ENTRY_NON_EXIST = """
\t<div class="user_not_found">
\t\t<div class="user_inner">
\t\t\t<div class="id_num">{0}</div>
\t\t\t<div class="entry_name">{1}</div>
\t\t\t<div class="error_msg">{2}</div>
\t\t</div>
\t</div>
"""
USER_ENTRY_NON_ACCEPTED = """
\t<div class="user_not_found">
\t\t<div class="user_inner">
\t\t\t<div class="id_num">{0}</div>
\t\t\t<div class="entry_name">{1}</div>
\t\t\t<div class="error_msg">{2}</div>
\t\t</div>
\t</div>
"""
USER_ENTRY_NON_INVITED = """
\t<div class="user_not_found">
\t\t<div class="user_inner">
\t\t\t<div class="id_num">{0}</div>
\t\t\t<div class="entry_name">{1}</div>
\t\t\t<div class="error_msg">{2}</div>
\t\t</div>
\t</div>
"""

# Download link format
COMMITS_LINK = '{0}{1}-{2}/commits/master'
DOWNLOAD_LINK = '{0}{1}-{2}/archive/master.zip'
USER_LINK = '{0}{1}-{2}'
