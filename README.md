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

### git_tools.py
Allows adds, commits, pushes, pulls, and status checking of any git repository in current working directory.

<code>python tools/git_tools.py</code>

#### Notes
* The default commit message is <code>git commit -m "automated commit with python tools" </code>
#### Flags
* <code>-repo</code> followed by the directories you want to execute git commands on will update those directories only.
 * _not_ case sensitive
* <code>-A</code> specifies to execute the git command on all repositories in the current working directory.
* <code>-git</code> allows user to specify git commands to execute
 * Valid Options:
   * <code>add</code>
   * <code>commit</code>
   * <code>push</code>
   * <code>pull</code>
   * <code>status</code>

#### Execution
Run: <code>python tools/commit_all_git.py -repo repo1 repo2 repo3</code>
