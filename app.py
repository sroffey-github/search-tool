import argparse
import os, sys, glob

my_parser = argparse.ArgumentParser(description='Search tool made with python', allow_abbrev=False)

my_parser.add_argument('-p', '--path', action='store', help='The path to search', required=True)

my_parser.add_argument('-n', '--name', action='store', help='Filename to search for', required=False)

my_parser.add_argument('-k', '--key', action='store', help='Key Word to search for', required=False)

args = my_parser.parse_args()

input_path = args.path
file_name = args.name
key_word = args.key

def search_file_by_name(path, file_name):
    files = []

    text_files = glob.glob(path + "/**/*", recursive = True)

    for i in text_files:
        if file_name in i.split('/')[-1]:
            if os.path.isfile(i):
                files.append(i)
            else:
                pass # not a file, could be dir
        else:
            pass
    
    if len(files) > 0:
        for x in files: print(f'\n[+] File Found: {x}')
    else:
        print('[!] No Files Found!')

def search_file_by_key(path, key_word):
    pass

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

if file_name != None:
    search_file_by_name(input_path, file_name)
if key_word != None:
    search_file_by_key(input_path, key_word)