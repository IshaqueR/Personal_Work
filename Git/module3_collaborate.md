# [Introduction to Version Control with Git](https://learn.microsoft.com/en-us/training/paths/intro-to-vc-git/)

## [Module: Collaborate with Git](https://learn.microsoft.com/en-us/training/modules/collaborate-with-git/)

### Unit 1: Introduction

* Quality control is critical, and developers work in small teams and use Git for version control.
* Version control is most useful for working on code with a team


#### Learning Objectives
* Clone a repository
* Push changes to a remote repository
* Stash changes
* Pull changes from other users to update a repository


### Unit 2: Collaborate by using a push command

When collaborating with others there is a process that is followed:
* First a copy of the Git project is required.
* Using Git, two or more people can work together on a project without fear of overwriting the other's work.
* You can check work before merging it with your work.


#### Clone a repository (git clone)
* In Git, you copy a repo by **cloning** it using the `git clone` command.
* `git clone` accepts a file system path (SSH or URL).
* In Unix and Linux, the cloning operation uses hard links
* it's fast and uses minimal space because only the directory entries need to be copied, not the files.


#### Remote repositories (git pull)
* When Git clones a repository, it creates a reference to the original repo that's called a remote by using the name `origin`.
* It sets up the cloned repo so that,
* the cloned repo will pull from, or retrieve data from, the remote repository.
* `origin` is the default location for Git to pull/push changes.
* `git pull` copies changes from the remote repository to the local one.
* it copies only new commits and objects.

Other methods of copying files:
* The `scp` command copies everything.
* If there are 10,000 files in the remote directory, `scp` copies them all.
* Rsync looks at every file in the local and remote directories and copies only the ones that are different.
* It's used for making backups, but it still has to hash every file unless the files have different sizes or creation dates.

Git:
* looks only at commits.

It already knows the last commit that it got from the remote repository because it saved the list of commits. Then, Git tells the computer that it's copying from to send everything that changed, including the new commits and the objects they point to. Those commits and objects are bundled up in a file called a pack and sent over in one batch. Finally, Git updates the working tree by unpacking all the objects that changed and merging them (if necessary) with the commits and objects in the working tree.

#### Create pull requests (git request-pull)
* If users don't have permission to make changes to your repo by pushing their code onto it, then you will have to review incoming changes before merging them into the main code base.
* Users will have to submit a pull request to ask you to pull changes into the main code base.
* This is done by using `git request-pull`
```bash
git request-pull -p origin/main .
```
* You refer to the `main` branch on the `origin` remote as `origin/main`.
* It's essentially the same as a pull request on GitHub.
* A pull request gives you a chance to review other collaborators' changes before you incorporate their work into the work you're doing.
* Code reviews are an important part—some would say the most important part—of collaborative programming.

### Create a remote (git remote) and complete the pull request (git pull)
Process:
* First use `git remote` command to set up another developer's repo as a *remote*.
* Then, you use that remote for pulls and pull requests by using the `git pull` command.

Behind the scenes, `git pull` is a combination of two simpler operations: `git fetch`, which gets the changes, and `git merge`, which merges those changes into your repository.

### Unit 3: Clone a repo
In a new directory type:
```bash
git clone ../Cats .
```
* `../Cats` tells Git where to clone from and `.` tells Git where to clone to.
* In Unix, `.` refers to your current directory.

The output after cloning should look like this:
```output
Cloning into '.'...
done.
```
### Unit 4: Make a pull request
> The command `pwd` is used to verify your folder location.

If you use the `git pull` command on a project with no changes since the clone, then you will get a message:
`Already up to date`.

#### Make a change and submit a pull request
If you set up a new identity in a different directory, the config settings are stored in the repo in the `.git/config` file. You won't have to enter them each time. Each time you change to the directory where you created the identity, it will effectively assume that identity.

The change to be made is on the module link. Have a look.

#### Create a remote and complete the pull request
Because your project directory and the Alice directory are on the same computer, you can pull directly from the Alice directory. In real life, the Alice directory would be on Alice's computer. You solve this situation by setting up a remote by using the `git remote` command. Then, you use that remote for pull and push requests. For this exercise, it's not practical to set up two machines to do these steps, so we'll set up a remote that uses a local path name. In reality, you would use a network path or URL instead.

### Unit 5: Collaborate by using a shared repo
Pulling directly from someone else's repository works, provided you're both on the same network. But, it's a clumsy process, and most collaborators aren't on the same network. It's better to set up a central repository that all collaborators can push to and pull from.

#### Create a bare repository
* You need a repo that doesn't have a working tree.

Bare repositories have multiple advantages over a working tree:
* Without a working tree, everybody can push changes without worrying about which branch is checked out.
* It's easy for Git to detect when another user has pushed changes that might conflict with yours.
* A shared repo scales to any number of developers. With a bare repo, you have to know only about the shared repo, and not about all the other collaborators from whom you might need to pull.
* By putting the shared repo on a server that you all can access, you don't have to worry about firewalls and permissions.
* You don't need separate accounts on the server because Git keeps track of who made each commit. (GitHub has millions of users who all share the `git` account. Everyone uses the Secure Shell (SSH) cryptographic network protocol, and users are distinguished by their public keys.)

Creating the bare repo:
```bash
cd ..
mkdir Shared.git
cd Shared.git
```
the `.git` is to distinguish the bare repo from working trees.

Use the command to create a bare repo within the shared directory:
```bash
git init --bare
```
When a repo is still bare, the git checkout command can't be used to set the name of the default branch. To accomplish this task, you can change the HEAD branch to point at a different branch; in this case, it's the main branch:
```bash
git symbolic-ref HEAD refs/heads/main
```
The next step is to get the contents of your repo into the shared repo. Use these commands to return to the project directory where your repo is stored, set up an origin remote, and perform an initial push:
```bash
cd ../Cats
git remote add origin ../Shared.git
git push origin main
```
You want push and pull to use the main branch of origin by default, as if you had made your repo by cloning it in the first place. But first, you need to tell Git which branch to track.
```bash
git branch --set-upstream-to origin/main
```

#### Set up for collaborators
You can then add more collaborators who want to clone the repo:
```bash
cd ..
mkdir Bob
cd Bob
git clone ../Shared.git .
```
Alice's repo is configured to push to and pull from their own repo. Use the following commands to change to the Alice directory and change origin to point to the shared repo:
```bash
cd ../Alice
git remote set-url origin ../Shared.git
```

#### Begin Collaborating
You can then work on the files and all make git requests to shared

### Unit 6: Knowledge Check

### Unit 7: Summary
In this module, you learned:

* How to clone a repository
* How to stash changes
* How to push changes to a repo
* What pull requests are and how to initiate a pull request