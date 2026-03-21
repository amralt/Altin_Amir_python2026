import os

def my_rm(dir):
    files = []
    for i in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, i)):
            my_rm(os.path.join(dir, i))
        else :
            files.append(i)
    for i in files:    
        os.remove(os.path.join(dir, i)) 
    os.removedirs(dir)

if __name__ == "__main__":
    my_rm(os.path.join('/home', 'amir', 'Общедоступные', 'programming', 'nsu', 'python', 'git', 'Altin_Amir_python2026', 'ksks'))
# /home/amir/Общедоступные/programming/nsu/python/git/Altin_Amir_python2026/ksks