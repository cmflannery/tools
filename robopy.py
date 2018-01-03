from __future__ import division, absolute_import, print_function
import os
import subprocess
import argparse
import sys


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


class Git():
    def __init__(self, workingdir=os.getcwd(), **kwargs):
        self.defaultSources = {
            'github':'https://github.com',
            'bitbucket':'https://bitbucket.org'
        }
        if 'username' in kwargs:
            self.__username = kwargs['username']
        if 'source' in kwargs:
            if kwargs['source'] in self.defaultSources:
                self.__source = self.defaultSources['source']
            else:
                self.__source = kwargs['source']
        self.__workingdir = workingdir
        os.chdir(self.__workingdir)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, val):
        if val in self.defaultSources:
            self.__source = self.defaultSources[val]
        else:
            self.__source = val

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, val):
        self.__username = val

    @property
    def workingdir(self):
        return self.__workingdir

    @workingdir.setter
    def workingdir(self,dir):
        self.__workingdir = dir
        os.chdir(self.__workingdir)

    def clone(self, repos, username=False, source=False):
        """ clone will allow the user to clone repositories given the username
        in instance. A username can optionally be passed.

        If a username is passed to the instance through this method, the
        instance variable will be updated/
        
        repos is expected to be a list of repository names associated with
        the username.
        
        source is an optional argument that allows the user to declare the source for their code
        Passing source as an argument will update the source for all subsequent instance operations
        The argument can be a link of the form 'https://github.com', or a keyword, if the source
        is common. See init for common, predeclared sources."""

        if not(username or self.username):
            print('Error: username must be declared before running.')
            return 1
        
        if username:
            self.username = username
        if source:
            try:
                self.source = self.defaultSources[source]
            except KeyError:
                self.source = source
            self.source = source
        
        baselink = "%(source)s/%(username)s/%(repo)s"

        for repo in repos:
            link = baselink % {'source':self.source, 'username':self.username, 'repo':repo}
            print('Cloning %s...' % repo)
            subprocess.call('git clone %s' % link, shell=True)

        print('Done.')


def main():
    print('No functionality when run as a main script currently')


if __name__ == '__main__':
    try:
        subprocess.call('cls', shell=True)
    except OSError:
        subprocess.call('clear')
    
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     print('Keyboard Interrupt. Exiting...')
    #     sys.quit()