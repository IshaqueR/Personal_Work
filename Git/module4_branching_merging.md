# [Introduction to Version Control with Git](https://learn.microsoft.com/en-us/training/paths/intro-to-vc-git/)

## [Module: Edit code through branching and merging in Git](https://learn.microsoft.com/en-us/training/modules/branch-merge-git/)

### Unit 1: Introduction

In this module, you'll learn what branches are in Git, how to use branches for development, and how to merge them, including dealing with merge conflicts.

#### Learning Objectives
* Learn how branches work in Git
* Create new branches and switch between branches
* Merge branches together
* Learn basic techniques for resolving merge conflicts

### Unit 2: Branches in Git
* Branching can make separating work easier.
* New development won't get in the way of existing bug fixes.
* Work done on a branch does not have to be shared.
* Also doesn't interfere with work done on other branches.
* Branches let you keep commits related to each topic together and isolated from other work, so changes made to a topic are easy to review and track.
* The goal is to keep the main branch clean until the work is ready to check in. Then, you push your changes to the main branch, or better yet, submit a pull request to merge the changes.

Advantages of branching in Git:

* Creating branches is extremely fast
* Switching branches is also fast, because Git stores whole files and unzips them instead of trying to reconstruct them from lists of changes.
* Merging in Git isn't quite as simple, but it's straightforward and often completely automatic.

#### Branch structure and naming
* A branch is simply a chain of commits that branch off from the main line of development.
* Other terminology used by other VCSes: Subversion says trunk, Git uses master (can rename to main).
* Branch starts with commit on default branch (main)
* As commits are added, branch grows a separate history chain.
* Eventually branches merge back into main.

> You can see the visual representation online if you'd like

#### Create and switch branches (git branch and git checkout)
* A reason to create a new branch might be to make changes to an existing feature.
* This branch is called a topic branch or feature branch.
* New branches are created with git branch command.
* Switching between branches can be done with the git checkout command.
* Checkout was covered previously when recovering files (replacing files in working tree by getting them from the index)

#### Merge branches (git merge)
* When you finalize work in a branch, you can merge it back into the main branch.
* Use git merge command to merge a specific branch into the current branch.

Example if your current branch is my-feature:
```bash
# Switch back to the main branch
git checkout main

# Merge my-feature branch into main
git merge my-feature
```
 * After using these commands, you should resolve *merge conflicts*. This is discussed later.

### Unit 3: Create a Branch
> Check online for the commands

Tasks completed here:
1. Setup
    * create a shared directory
    * create a bare repo in shared directory
    * set the default branch for the new repo by pointing HEAD branch to main branch
    
2. Clone the shared repo for other user
    * move up a level and create a directory for other user
    * clone and configure the repo for other user (git clone, config, symbolic-ref)
    
3. Add base files
    * create index.html, Assets directory, site.css in Assets directory, add and commit
    * add code to html file
    * go to Assets directory, add code to css file
    * navigate to user directory, add and commit changes.
    * push the commits to origin: `git push --set-upstream origin main`
    
4. Create a branch for a user
    * make other user directory
    * clone the shared repo and configure for the user
    * verify files are copied
    * run git branch to add a new branch called add-style
    ```bash
    git branch add-style
    git checkout add-style
    ```
    * now on add-style branch, edit code, commit changes on this branch
    * switch back to main branch, and do a pull (in case anyone else has made changes):
    ```bash
    git checkout main
    git pull
    ```
    > Note: if it says Already up to date, then that means that this user's main matches the main in the shared repo. If this is the case, a fast-forward merge can be done (this merge only fails if the main has changed). It's good practice to see if it fails.
    * Merge the branch using a fast-forward merge then push main from this user to shared repo
    

### Unit 4: Merge a branch
> Check online for commands

Tasks completed here:
1. Create a branch for main user
    * You can create a branch and switch to the branch in a single command using the `-b` flag `git checkout -b add-cat`
    * Download image resources and move it into Assets directory
    * remove other files, as it's not necessary
    * edit html file with image resource
    * add and commit the new image file and edit of the html file
    * switch over to main branch again using checkout
    * perform a pull to check if changes have been made (it will pull the new main with previous changes made by the other user)
    * Then merge the branch into the main branch
    * Push main onto the shared repo
    > Note: you don't use fast-forward merge here, since you already know that the main had changed.
2. Sync the repos
    * So user 1 has an up to date repo, but user 2 does not.
    * Go to user 2 directory and perform a pull
    * Manually verify that repos are synced.
    

### Unit 5: Resolve merge conflicts
Here we are simulating merge conflicts and looking at gits ways to deal with them:

Tasks completed:
1. Create branches for both users
    * Create branch for user 1 and switch user 1 to that branch
    * Create branch for user 2 and switch user 2 to that branch
2. Make a change as user 2
    * Download assets
    * Make edit to html file to include different picture than user 1
    * Run git commands to push changes
3. Make changes as user 1
    * edit html file
    * attempt to merge (an merge conflict error will occur)
4. Resolve the conflict
    * Option 1: Run the `git merge --abort` command to restore the main branch to what it was before the attempted merge. Run the `git pull` command to get Alice's changes. Then, create a new branch, make their changes, and merge their branch into the main branch. Last, they push their changes.
    * Option 2: Run the `git reset --hard` command to get back to where they were before they started the merge.
    * Option 3: Resolve the conflict manually by using information that Git inserts into the affected files.

Developers seem to prefer the last option. When Git detects a conflict in content versions, it inserts both versions of the content into the file. Git uses special formatting to help you identify and resolve the conflict: left angle brackets `<<<<<<<`, double dashes (equal signs) `=======`, and right angle brackets `>>>>>>>`. The content above the line of dashes `=======` shows your changes in your branch. The content below the separator line shows the version of the content in the branch that you're trying to merge into.

### Unit 6: Knowledge Check

### Unit 7: Summary
You learned:

* What branches are, and how and when to use them
* How to merge branches
* How to resolve merge conflicts