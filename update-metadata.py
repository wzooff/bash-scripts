#!/usr/bin/python3.6

import chef
import fileinput
import re
import os
import sys
import getopt

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:",["ifile="])
      if not opts:
         print('Usage: metadata.py -i <path_to_metadata.rb>')
         sys.exit(2)
   except getopt.GetoptError:
      print('Usage: metadata.py -i <path_to_metadata.rb>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      else:
         print ('Usage: metadata.py -i <path_to_metadata.rb>')
         sys.exit()
      
      input_path = os.path.abspath(inputfile)

      api = chef.autoconfigure()
      cookbooks = api['/cookbooks']

      with fileinput.FileInput(input_path, inplace=True) as file:
          for line in file:
              dependsfound = re.search(r"depends \'(.*)\',", line)
              if dependsfound:
                  version = cookbooks[dependsfound.group(1)]['versions'][0]['version']
              else:
                  version = ''
              print(re.sub(r"~> (.*)\'", "~> %s'" % version, line), end='')

if __name__ == "__main__":
    main(sys.argv[1:])
