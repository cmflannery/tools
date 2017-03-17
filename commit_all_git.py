import subprocess
import os
import argparse
# from future import print_function


def parsey():
    parser = argparse.ArgumentParser(description='Commit and push git repositories in working directory.')
    parser.add_argument('-repo', dest='repo', metavar='N', type=str, nargs='*',
                        help='Array of repositories to commit and push')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    return args


def main():
    args = parsey()
    currentdir = os.getcwd()
    dirsincwd = os.listdir('.')
    for dirname in args.repo:
        if os.path.isdir(dirname) and dirname in dirsincwd:
            dirpath = os.path.join(currentdir, dirname)
            os.chdir(dirpath)  # enter git repository directory
            print('Updating: ', dirname)
            subprocess.call('git add -A', shell=True)  # update
            subprocess.call('git commit -m \"automated commit with python tools\"', shell=True)  # update
            subprocess.call('git push', shell=True)
            os.chdir(currentdir)  # return to main working directory
        else:
            print(dirname, 'is not a repository in the working directory')
    print('All done!')


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('clc', shell=True)

    main()
