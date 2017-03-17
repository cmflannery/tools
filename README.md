# Python Tools
A collection of useful python scripts. All scripts prefer python, but _should_ run on python2.

## Directory Structure
Directory structure should be set up as follows:

-> github_directory
--> tools
---> pull_all_git.py
---> other_tools.py
--> repo1
--> repo2

### pull_all_git.py
Pulls all changes to repositories in the current working directory

<code>python tools/pull_all_git.py</code>

Directory structure should be set up as follows:

-> github_directory
--> tools
---> pull_all_git.py
--> repo1
--> repo2

### commit_all_git.py
Commits and Pushes changes to git repositories in the current working directory.
#### Notes
* By default, the script will commit and push all changed files. I.e. the script executes the command <code>git add -A</code>
* The script commits with a message <code>git commit -m "automated commit with python tools" </code>
#### Flags
* <code>-repo</code> followed by the directories you want to commit and push will update those directories only.
 * _not_ case sensitive
* <code>-A</code> will commit and push all repositories in the current working directory.

#### Execution
Run: <code>python tools/commit_all_git.py -repo repo1 repo2 repo3</code>
