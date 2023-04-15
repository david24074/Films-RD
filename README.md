# Website
In the explanation below I will be using the `py` command, based on the way you installed python this command might be `python` or `python3` instead.

## Start the server
If you followed the installation steps then you can move on to starting the server.  
It's important that you first start a virtual environment before you start the server.  
1. `.\venv\Scripts\activate`
2. `py server.py`

## Installation
In this guide I'm assuming that you're running on Windows and not on Linux or Mac.  
1. Clone this repository
2. Navigate to the repository on your computer in powershell (has to be powershell, can't be a regular commandprompt)
3. Execute the next command to make a virtual environment `py -m venv venv`
4. Execute the next command to start the virtual environment `.\venv\Scripts\activate`
5. It should now say `(venv)` in your powershell prompt, now execute the command `pip install -r requirements.txt`

## Editing modules
If you added, deleted or edited one of the modules in your virtual environment then you have to update the requirements.txt file.  
You can do this by running the next command while you're in the root of the repository `pip freeze > requirements.txt`.  
Make sure to do this before you make a new commit.  