import subprocess
import os
import argparse
# from future import print_function


def parsey():
    parser = argparse.ArgumentParser(description='Commit and push git repositories in working directory.')
    parser.add_argument('-repo', dest='repo', metavar='N', type=str, nargs='*',
                        help='Array of repositories to commit and push')
    parser.add_argument('-A', dest='all', action='store_true',
                        help='Push and Commit all repositories. Void if -repo flag is called')
    args = parser.parse_args()
    return args

def commit(repos, dirsincwd):
    currentdir = os.getcwd()
    for dirname in repos:
        if os.path.isdir(dirname) and dirname in dirsincwd:
            dirpath = os.path.join(currentdir, dirname)
            os.chdir(dirpath)  # enter git repository directory
            print('\nCommitting and Pushing: ', dirname)
            subprocess.call('git add -A', shell=True)  # update
            subprocess.call('git commit -m \"automated commit with python tools\"', shell=True)  # update
            subprocess.call('git push', shell=True)
            os.chdir(currentdir)  # return to main working directory
        else:
            print(dirname, 'is not a repository in the working directory')


def main():
    args = parsey()
    dirsincwd = os.listdir('.')
    if args.all:
        commit(dirsincwd, dirsincwd)
        return 0
    if args.repo != None:
        commit(args.repo, dirsincwd)
    elif args.repo == None:
        print('Error: You must enter at least one repository, or add the -A flag')
        return 1
    print('All done!')


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('clc', shell=True)

    main()
