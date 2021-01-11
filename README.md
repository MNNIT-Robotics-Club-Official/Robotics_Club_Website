# Robotics_Club_Website

## For Windows 
If already installed python follow next steps

### Preferably use Python virtual env for development
1. open Powershell terminal in an empty folder (Shift+ right click) and run  `python -m venv robo` where robo is the environment name(can be anything)
2. then run `.\robo\Scripts\activate` , this will activate the environment(green text in the beginning of every line will appear)
3. then install Django inside this environment with this command `pip install Django`
4. then clone the git repo `git clone https://github.com/MNNIT-Robotics-Club-Official/Robotics_Club_Website.git`
5. `cd Robotics_Club_Website`
6. run `python manage.py runserver`
7. goto server http://127.0.0.1:8000/

### If you want to install Django Globally and do not want an Virtual env, then do following steps:
1. open Powershell terminal in an empty folder (Shift+ right click) and run `pip install Django`
2. then clone the git repo `git clone https://github.com/MNNIT-Robotics-Club-Official/Robotics_Club_Website.git`
3. `cd Robotics_Club_Website`
4. run `python manage.py runserver`
5. goto server http://127.0.0.1:8000/