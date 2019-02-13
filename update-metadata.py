#!/usr/local/bin/python3
# Will update cookbook versions to latest, that exist on chef-server

# pychef should be installed

import chef
import fileinput
import re

api = chef.autoconfigure()
cookbooks = api['/cookbooks']

with fileinput.FileInput('metadata.rb', inplace=True) as file:
    for line in file:
        dependsfound = re.search(r"depends \'(.*)\',", line)
        if dependsfound:
            version = cookbooks[dependsfound.group(1)]['versions'][0]['version']
        else:
            version = ''
        print(re.sub(r"~> (.*)\'", "~> %s'" % version, line), end='')
