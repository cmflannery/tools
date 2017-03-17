import subprocess
import os
# from future import print_function


def main():
    currentdir = os.getcwd()
    for dirname in os.listdir('.'):
        if os.path.isdir(dirname):
            dirpath = os.path.join(currentdir, dirname)
            os.chdir(dirpath)  # enter git repository directory
            print('Updating: ', dirname)
            subprocess.call('git pull', shell=True)  # update
            os.chdir(currentdir)  # return to main working directory

    print('All done!')


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('clc', shell=True)

    main()
