import subprocess
import os
import shutil



def efs_create_directory(name_app, ambiente):
    user = 1004
    group = 1005
    if ambiente == 'hml':
        efs_directory = "/volumes/HML-NEW/" + name_app
        status_exit = subprocess.call(['ls', efs_directory], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(status_exit)
        if status_exit != 0:
            os.mkdir(efs_directory)
            shutil.chown(efs_directory, user, group)
            print(f'created {efs_directory} directory in efs')
    elif ambiente == 'qa':
        efs_directory = "/volumes/TST-NEW/" + name_app
        status_exit = subprocess.call(['ls', efs_directory], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if status_exit != 0:
            os.mkdir(efs_directory)
            shutil.chown(efs_directory, user, group)
            print(f'created {efs_directory} directory in efs')    
