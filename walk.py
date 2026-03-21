import os
import argparse


def my_walk(dir : str):
    files = []
    print(dir + ':')
    for i in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, i)):
            my_walk(os.path.join(dir, i))
        else :
            files.append(i)
    
    print(files)

# my_walk(os.path.join('/home', 'amir', 'Общедоступные', 'tips', 'obsidian'))
# /home/amir/Общедоступные/programming
parser = argparse.ArgumentParser()
parser.add_argument('--proj_dir')
args = parser.parse_args()
my_walk(args.proj_dir)