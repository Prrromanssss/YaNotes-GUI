<div align="center">
  <h1><span style="color:red">Ya</span>Notes</h1>
</div>


![flake8 test](https://github.com/Prrromanssss/NotesPyQt_GUI/actions/workflows/python-package.yml/badge.svg)



## Contents
* [About](#about)
  * [Authorization](#authorization)
  * [Text notes](#text-notes)
  * [Table notes](#)
  * [Calendar notes](#)
* [Deployment instructions](#deployment-instructions)
  * [Cloning project](#1-cloning-project-from-github)
  * [Activation venv](#2-creation-and-activation-venv)
  * [Requirements](#3-installation-all-requirements)
  * [.Env](#4-generate-file-with-virtual-environment-variables-env)
  * [Running](#5-running-project)
* [Database](#database)
  * [ER-diagram](#er-diagram)
* [Architecture](#architecture)
  * [General architecture](#general-architecture)
  * [Architecture of the apps folder](#architecture-of-the-apps-folder)
  * [Architecture of the bot folder](#architecture-of-the-bot-folder)
  * [The rest of the architecture](#the-rest-of-the-architecture)


## About
#### The pace of life is so frantic that a handy note-taking app is essential!!!

So, this is a note-taking application written with the [PyQt5](https://doc.qt.io/qtforpython/) library.

### Authorization
Each user can sign in and use their personal notes.

![Image of the signing in](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/sign_in.png)

Sign up

![Image of the signing up](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/sign_up.png)


Recovery their password

![Image of the recovery password](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/recovery_password.png)

Then, the user can see his profile

![Image of the account](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/account.png)

There are 3 types of the notes:
* Text notes
* Table notes
* Calendar notes

### Text notes
The user can create an unlimited number of note folders.

![Image 1 of the text notes](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/text_notes_folders.png)

Each folder has 10 pages for editing: you can write some text or change the name of the page on which you write. Click "save page" to save your edits.

![Image 2 of the text notes](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/text_notes_pages.png)

### Table notes
Also user can load his .csv files in this app
You can create an unlimited number of note tables.

![Image 1 of the table notes](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/table_notes_tables.png)


Load your .csv files with appropriate configuration of the file. Follow this link to understand what setting is responsible for [CSV File Reading and Writing in Python](https://docs.python.org/3/library/csv.html).

![Image 2 of the table notes](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/table_notes_pages.png)


### Calendar notes

A telegram bot written on the [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/0.3.0/) api is integrated into my project.
So, you can set some notifications in these notes to receive them in the bot.
* Firstly, follow this link [YaNotes_bot](https://t.me/YaNotes_bot) and click "/start".
* I have read too little "this" to understand how to poll bot asynchronously with PyQt5. That's why you need to get your chat id and enter it after pressing the button "Connect tg bot".
* You can get chat id with [username_to_id_bot](https://t.me/username_to_id_bot) or other bots that can do it.
* Do not forget to choose your GMT!!!

When notes began to refer to a date in the past, they are automatically deleted.


![Image of the calendar notes](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/calendar_notes.png)

***

## Deployment instructions


### 1. Cloning project from GitHub

1.1 Run this command
```commandline
git clone https://github.com/Prrromanssss/NotesPyQt_GUI.git
```

### 2. Creation and activation venv

2.1 First of all, from root directory run this command
```commandline
python -m venv venv
```
2.2 Then run this command to activate venv
#### Mac OS / Linux
```commandline
source venv/bin/activate
```
#### Windows
```commandline
.\venv\Scripts\activate
```

### 3. Installation all requirements

3.3 Run this command 
```commandline
pip install -r requirements.txt
```

### 4. Generate file with virtual environment variables (.env)

4.1 Generate file '.env' in root directory with structure specified in the 'examples/test-env.txt' file

### 5. Running project

5.1 Run this command
```commandline
python main.py
```

***

## Database

This project uses the [sqlite3](https://www.sqlite.org/docs.html) database

Test database for work is presented in the YaNotes.sqlite3 file

### ER-diagram

![Image of the ER-diagram](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/ER-diagram.png)

***

## Architecture

In this project I tried to stick to the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) design pattern or MTV in python.
The project also works asynchronously with [asyncio](https://docs.python.org/3/library/asyncio.html) and [asyncqt](https://github.com/gmarull/asyncqt)

### General Architecture

![Image of the general architecture](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/general_architecture.png)

### Architecture of the apps folder

![Image of the apps folder](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/apps_folder_architecture.png)

I placed all PyQt5 widgets in the apps folder.
Each window has its own folder corresponding to its name.
In which this structure is presented:
* templates:
All design files (.ui, .py) are located in templates folder.
  * models: 
This file presents work with the database, according to this structure:
  ```python
  import sqlite3
  
  from settings import DATABASE
  
  
  class TableNameModel:
      @staticmethod
      def description_of_the_request(*, arg1, arg2):
          con = sqlite3.connect(DATABASE)
          request = ''' Some SQL request
                    '''
          con.execute(request)
          con.commit()
  ```
  It was better to write a simple ORM, but I didn’t have enough time :(
* widgets aka views:
  The rest of the files ending in _widget are allegedly views that connect to load data from the database into templates, and they also contain all the functionality of this window.
* validators

![Image of the each app](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/each_app_folder_architecture.png)

### Architecture of the bot folder

![Image of the each app](https://github.com/Prrromanssss/NotesPyQt_GUI/raw/main/media_for_README/bot_architerture.png)

All entities associated with telegram bot are in the bot folder.
It should be noted that the api token for the bot is a virtual environment variable.

### The rest of the architecture
* media: User avatars are stored in this folder
* tables: User .csv files are stored in this folder