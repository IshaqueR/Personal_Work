# [Introduction to Version Control with Git](https://learn.microsoft.com/en-us/training/paths/intro-to-vc-git/)

## [Module: Introduction to Git](https://learn.microsoft.com/en-us/training/modules/intro-to-git/)

### Unit 1: Intro

* Consider a scenario where software development is involved.
* Quality control is important.
* Developers work in teams using Git for version control.
* Git helps keep track of changes.
* Also keeps all source code files backed up for server failure.

> The video link covers a lot of commands. Just know that it's showing the capability of Git
[Intro to Git Recap](https://www.youtube.com/watch?v=9uGS1ak_FGg)

#### Learning Objectives
* Learn what version control is
* Understand distributed version control systems, like Git
* Recognize the differences between Git and GitHub and the roles they play in the software development life-cycle

### Unit 2: What is version control?
* A version control system (VCS) is a program or set of programs that tracks changes to a collection of files.
* One goal is to easily recall earlier versions of individual files or of the entire project.
* Another goal is collaboration on the same files without affecting each other's work.
* Another name for VCS is Software Configuration Management (SCM).


With VCS you can:

* See all the changes made to your project, when the changes were made, and who made them.
* Include a message with each change to explain the reasoning behind it.
* Retrieve past versions of the entire project or of individual files.
* Create branches, where changes can be made experimentally.
* Attach a tag to a version—for example, to mark a new release.

#### Distributed version control
* Earlier versions of VCSes (CVS, SVN, Perforce) used a centralized server to store a project's history.
* This means one server is a potential single point of failure.
* Git is **distributed** - meaning project stored on client and server side.
* Check locally and sync when network connection is available.
* If server fails, you have access to a local copy.

#### Git terminology

Here is a short list of terms that Git users frequently use.
* Working tree: The set of nested directories and files that contain the project that's being worked on.
* Repository (repo): The directory, located at the top level of a working tree, where Git keeps all the history and metadata for a project.
* Hash: A number produced by a hash function that represents the contents of a file or another object as a fixed number of digits.
* Object: A Git repo contains four types of objects, each uniquely identified by an SHA-1 hash (blob, tree, commit, tag).
* Commit: It means you are committing the changes you have made so that others can eventually see them, too.
* Branch: A branch is a named series of linked commits. The most recent commit on a branch is called the *head*.
* Remote: A remote is a named reference to another Git repository.
* Commands, sub-commands, and options: Git operations are performed by using commands like `git push` and `git pull`. `git` is the command, and `push` or `pull` is the sub-command.

#### The Git command line
* There are various GUIs available for Git (GitHub Desktop)
* Programming editors also have interfaces to Git
* Git command line is Git commands executed in command prompt (for this module: in Azure Cloud Shell)

#### Git and GitHub
##### Git
* is a distributed version control system.
* multiple developers can use to work on a project.
* provides a way to work with one or more local branches and then push them to a remote repository.

##### GitHub
* is a cloud platform that uses Git as its core technology.
* simplifies the process of collaborating on projects.
* provides a website, more command-line tools, and overall flow that developers and users can use to work together.
* acts as the remote repository.

Some features of GitHub include:

* Issues
* Discussions
* Pull requests
* Notifications
* Labels
* Actions
* Forks
* Projects

### Unit 3: Try out Git
> Before you can create your first repo, you must make sure that Git is installed and configured.
I followed this [link](https://www.youtube.com/watch?v=2j7fD92g-gE), and am using GitBash to practice.

#### Configure Git

* To double check that git is installed, type `git --version`.

> Note: this should also work on windows power shell and cmd.

* To configure git, you must define some global variables: `user.name` and `user.email`
* Both are required to make commits.

use the following commands:

```bash
git config --global user.name "<USER_NAME>"

git config --global user.email "<USER_EMAIL>"
```

to check run the command:
```bash
git config --list
```

#### Set up Git repository
Git works by checking for changes to files within a certain folder.
To create a repository:

* Create a folder to serve as the working tree (project directory)
* Initialize a git repository into that folder
* That way git can track changes

Creating a folder:
```bash
mkdir Cats
```
```bash
cd Cats
````
* `mkdir` is the command for making a directory (folder)
* `cd` is the command for changing to a directory specified

Initializing the new repository:
Version 2.28.0 or later:
```bash
git init --initial-branch=main
```
Or:
```bash
git init -b main
```
Earler Versions:
```bash
git init
git checkout -b main
```
Here you are setting the name of the repository to `main`.

To view the status of the working tree:
```bash
git status
```
To view the contents of the working tree:
```bash
ls -a
```
* `ls` means list `-a` means all (including hidden files)

You typically don't do anything with the .git directory directly. Git updates the metadata there as the status of the working tree changes to keep track of what's changed in your files. This directory is hands-off for you, but it's incredibly important to Git.

#### Get help from Git

Git, like most command-line tools, has a built-in help function that you can use to look up commands and keywords. Use the command:

```bash
git --help
```

* This will display the options available with git.
* Each command comes with its own help page.

### Unit 4: Basic Git commands

#### git status
* the most common command
* displays the state of the working tree (and staging area)
* lets you see which changes are being tracked by git

#### git add
* the command used to start keeping track of changes
* technical term is **staging** changes
* used to stage changes to prepare for a commit
* all changes in files added but not yet committed are stored in staging area

#### git commit
* after staging changes for commit, save your work to a snapshot using `git commit`
* commit is commit to a change
* means putting a copy in the repository as a new version
* data saved in commit includes author name, email, date, comments, optional digital signature, and unique identifier of the preceding commit.

#### git log
* see information about previous commits
* each commit has a message attached to it
* log prints the info about most recent commits like timestamp, author, commit message.
* helps keep track of what you've been doing

#### git help
* easily get information about commands

> `git <command> --help` gives information about that specific command

