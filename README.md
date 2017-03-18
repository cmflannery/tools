# Python Tools
A collection of useful python scripts. All scripts prefer python, but _should_ run on python2.

## Directory Structure
Directory structure should be set up as follows:

-> github_directory </br>
---> tools </br>
-----> git_tools.py </br>
-----> other_tools.py </br>
---> repo1 </br>
---> repo2 </br>

## git_tools.py
Allows adds, commits, pushes, pulls, and status checking of any git repository in current working directory.

### Usage
#### Execution Examples
1. One common use case is to __add, commit, and push__ lots of changes in lots of repositories simultaneously. While this may be useful, remember that you aren't able to add specific commit messages to each repo commit. Also be warned that the <code>add</code> command adds *__all__* files in the repo that have been modified!! This is a dangerous way to commit changes.
 * Run: <code>python tools/git_tools.py -repo repo1 repo2 repo3 -git add commit push</code>
1. __Pull changes on all repositories.__ This is a simple and relatively safe command to run. <code>git_tools.py</code> is not capable of merging changes, and will abort if a merge conflict is detected.
 * Run: <code>python tools/git_tools.py -A -git pull</code>

#### Flags
 * <code>-repo</code> followed by the directories you want to execute git commands on will update those directories only.
  * _not_ case sensitive
 * <code>-A</code> specifies to execute the git command on all repositories in the current working directory.
  * By default, git_tools will add all changed files in the repo by executing <code>git add -A</code>. There is not currently an option to change this.
 * <code>-git</code> allows user to specify git commands to execute
  * Valid Options:
    * <code>add</code>
    * <code>commit</code>
    * <code>push</code>
    * <code>pull</code>
    * <code>status</code>

#### Notes
* The default commit message is <code>git commit -m "automated commit with python tools" </code>
