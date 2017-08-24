# Github homework downloader
[![@ppizarror](http://ppizarror.com/resources/images/github-homework-downloader/author.svg)](http://ppizarror.com)
[![Licencia MiT](http://ppizarror.com/resources/images/github-homework-downloader/licence.svg)](https://opensource.org/licenses/MIT/)
[![Python](http://ppizarror.com/resources/images/github-homework-downloader/python.svg)](https://www.python.org/downloads/)
<br>

A simple application that request homework name on github (for example *01-homework*) and lists all users from a organization with a download link to that homework.

Example:

<p align="center">
  <img src="http://ppizarror.com/resources/images/github-homework-downloader/example_homework_downloader.PNG" alt="Example" width="90%px" />
</p>

## Usage

Make a file where contains all user lists, like *users.txt*, make sure you use the following structure:

<pre>
<i>id</i><b>\t</b><i>Name</i><i></i><b>\t</b><i>User invited to organization</i><b>\t</b><i>User accepted invitation</i>
</pre>

Example:
```bash
1    John Doe    joe_john    true    true
2    Mark Houston B.    mark340    true    true
3    Jonathan K. B.    johnkb12    true    true
4    Pablo Pizarro R.    ppizarror    true    true
5    William R.        false    false
6    Paul Stephenson    true    true
```

Then add user file and organization link to <a href="https://github.com/ppizarror/github-homework-downloader/blob/master/config.json">config.json</a>.

Finally execute script ```main.py``` and write the homework name to create a webpage containing the list of users and dowload links.

## To do
- Add support to several languages.
- Set maximum limit time to accept an homework.
- Verify homework status from Python.
- Download multiple files at once.
- Add <a href="https://theory.stanford.edu/~aiken/moss/">moss</a> support to detect plagiarism.
- Add more user file structures.
- Add icon to access each user commit.
- Add entry to create anotations, disable users from list, sort by name or user-id.

## Author
<a href="ppizarror.com">Pablo Pizarro R.</a> | 2017