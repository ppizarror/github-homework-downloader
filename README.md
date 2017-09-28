<h1 align="center">
  <img alt="Github homework downloader" src="http://ppizarror.com/resources/other/github.png" width="200px" height="200px" />
  <br /><br />
  Github homework downloader</h1>
<p align="center">Python app that create a html website to download several homeworks from a student github organization</p>
<div align="center"><a href="http://ppizarror.com"><img alt="@ppizarror" src="http://ppizarror.com/badges/author.svg" /></a>
<a href="https://opensource.org/licenses/MIT/"><img alt="MIT License" src="http://ppizarror.com/badges/licensemit.svg" /></a>
<a href="https://www.python.org/downloads/"><img alt="Python 2.7" src="http://ppizarror.com/badges/python27.svg" /></a>
</div><br />

A simple application that request homework name on github (for example *01-homework*) and lists all users from a organization with a download link to that homework.

Example:
<p align="center">
  <img src="http://ppizarror.com/resources/images/github-homework-downloader/example_homework_downloader.PNG" alt="Example" width="80%" />
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

Then add user file and organization link to <a href="https://github.com/ppizarror/github-homework-downloader/blob/master/config.json">config.json</a>. Finally execute script ```main.py``` and write the homework name to create a webpage containing the list of users and download links.

## To do
- <strike>Add support to several langs</strike> <i>(02/09/17)</i>.
- Set maximum limit time to accept an homework.
- Verify homework status with Python.
- Download multiple files at once.
- Add <a href="https://theory.stanford.edu/~aiken/moss/">moss</a> support to detect plagiarism.
- Add more user file structures.
- <strike>Add icon to access each user commit</strike> <i>(02/09/17)</i>.
- Add entry to create anotations to each user, disable users from list, sort by name or user-id.
- Create excel file with scores of each user.
- Visualize total commits of each user (only commits before homework time limit).

## License
This project is under MIT License [https://opensource.org/licenses/MIT]

## Author
<a href="http://ppizarror.com" title="ppizarror">Pablo Pizarro R.</a> | 2017
