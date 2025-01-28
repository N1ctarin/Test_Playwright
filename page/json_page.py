import json

class CreduForWatchdog:

    with open('kredu.json', 'r') as config_file:
        config = json.load(config_file)
    email = config['email']
    password = config['password']


class DateForTesting:

    name_new_project = 'Testing1'
    description_new_project = 'Description1'