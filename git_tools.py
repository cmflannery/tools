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
    parser.add_argument('-git', dest='git', metavar='N', type=str, nargs='*',
                        help='Specify which git commands to execute. Valid options: add, commit, push, status')
    parser.add_argument('-m', dest='msg', type=str, nargs=1, help='Commit message: if nothing is entererd, default is used.')
    args = parser.parse_args()
    return args


def executeGitCmd(command, msg):
    if 'add' in command:
        subprocess.call('git add -A', shell=True)  # update
    if 'commit' in command:
        defaultmsg = '\"automated commit with python tools\"'
        if msg is None:
            commitcmd = 'git commit -m' + defaultmsg
        else:
            commitcmd = 'git commit -m' + str(msg)
        subprocess.call(commitcmd, shell=True)  # update
    if 'push' in command:
        subprocess.call('git push', shell=True)
    if 'status' in command:
        subprocess.call('git status', shell=True)


def iterateDir(repos, dirsincwd, command, msg):
    currentdir = os.getcwd()
    for dirname in repos:
        if os.path.isdir(dirname) and dirname in dirsincwd:
            dirpath = os.path.join(currentdir, dirname)
            os.chdir(dirpath)  # enter git repository directory
            print('\nCurrent Repository: ', dirname)
            executeGitCmd(command, msg)
            os.chdir(currentdir)  # return to main working directory
        else:
            print(dirname, 'is not a repository in the working directory')


def main():
    args = parsey()
    dirsincwd = os.listdir('.')
    print(args.msg)
    if args.all:
        iterateDir(dirsincwd, dirsincwd, args.git, args.msg)
        return 0
    if args.repo is not None:
        iterateDir(args.repo, dirsincwd, args.git, args.msg)
    elif args.repo is None:
        print('Error: You must enter at least one repository, or add the -A flag')
        return 1
    print('All done!')


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('clc', shell=True)

    main()
