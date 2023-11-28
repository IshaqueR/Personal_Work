# [Introduction to Version Control with Git](https://learn.microsoft.com/en-us/training/paths/intro-to-vc-git/)

## [Module: How to create and modify a Git project](https://learn.microsoft.com/en-us/training/modules/create-git-project/)

### Unit 1: Introduction

In this module, you'll get to start your own project in Git and gain some practice editing some errors that might exist in your code. Git can surely seem confusing when you first start, but as you gain more practice working with it you will be able to navigate it smoothly.

#### Learning Objectives
* Learn how to create a new Git Project
* Understand how to track changes in Git
* Know how to fix simple mistakes in Git
* Recover deleted files in Git


### Unit 2: Start a project

* You'll start using Git by adding a simple HTML file to your working tree.
* Then, you'll make some changes in the directory and learn how to commit the changes.

#### Create and add (stage) a file
* Use `touch` command to create a file
```bash
touch index.html
```
* `touch` updates a file's last modified time if it exists.
* if not then it creates an empty file with that file name.

Use `git status` regularly between commands to view hints of what to do next:

```output
No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    index.html

nothing added to commit but untracked files present (use "git add" to track)
```
* Use `git add` to add the new file to Git's index.
* Don't forget the **period** at the end of the command

```bash
git add .
```
* A commit has now been staged
* Git's index is a staging area for commits

If you use git status you should see all the files that are staged for a commit:
```output
On branch main

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   index.html
```

#### Make a commit

* Next step is to commit

Use the following  command to create a commit:
```bash
git commit index.html -m "Create an empty index.html file"
```
* so the command is `git commmit`
* this is followed by the file name
* `-m` specifies that you want to provide a **commit message**
* this is followed by the message

Git responds with a confirmation of what you did:
```output
[main (root-commit) 87e874c] Create an empty index.html file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index.html
```
As usual, follow up with git status to confirm the working tree is clean, i.e. it contains no changes that haven't been committed.

* Now use `git log` to show info about the commit:

```output
commit f0c64c28a467ed0704f103e54bc6053639bbeeec (HEAD -> main)
Author: Flarez <flarez0912@gmail.com>
Date:   Tue Nov 28 12:06:45 2023 +0200

    Create an empty index.html file
```

#### Modify the file and commit the change
> index.html was created to serve as the website's home page, but it's currently empty. The next step is to add some HTML to it. So you can use the gitbash editor by typing `nano <filename>`, or you could go to the directory of your repository and modify the file from there using a text editor. I used the first method for practice, but in future I will most likely just go to the file and edit it directly.

Add the html code:
```html
<h1>Our Feline Friends</h1>
```
Run `git status`:
```output
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
```
Commit the changes:
```bash
git commit -a -m "Add a heading to index.html"
```

* This time we didn't run `git add` to stage the changes.
* Instead we use `-a` flag
* `-a` option adds all the files **modified** since the last commit
* it won't add new files, that uses `git add`

The output after the commit should look like:
```output
[main 71754a1] Add a heading to index.html
 1 file changed, 1 insertion(+)
```
* Use git status once again to ensure a clean working tree

There are now two versions of the file in the repo, although you see only one of them (the current one). One of the benefits of using Git is that you can roll back the changes you have made, or you can go backward in time and see previous versions. More on this important topic later.

### Unit 3: Make changes and track them with Git
Iteration:
* Projects are iterative
* means many changes
* code additions, bug fixes, deletions, and replacements

As you work Git helps track these changes. It also lets you undo mistakes.

#### Modify index.html

I'm modifying the html file with the following content. For now I don't need to know what this is but I can modify it later.
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Our Feline Friends</title>
  </head>
  <body>
    <h1>Our Feline Friends</h1>
    <p>Eventually we will put cat pictures here.</p>
    <hr>
  </body>
</html>
```
* The `git diff` command can be used to see what changed.
* This shows changes made to the actual file.
* plus sign shows lines that were added
* minus sign shows lines that were deleted

The default is for `git diff` to compare the working tree to the index. In other words, it shows you all the changes that haven't been staged (added to Git's index) yet. To compare the working tree to the last commit, you can use `git diff HEAD`.

* Now just commit the change
* Instead of using `-a` you can specify the file name explicitly
```bash
git commit -m "Add HTML boilerplate to index.html" index.html
```
* Use `git diff` again to compare the working tree to the index
* It produces no output because the working tree, index, and `HEAD` are all in agreement.

> if you happened to use another editor, including an editor called sed, the editor probably created an index.html.bak file that you don't want to commit. Editors like Vim and Emacs create backup files with names like index.html~ and index.html.~1~, depending on how they're configured.

Use the following command to create and open a file named .gitignore in the built-in code editor:
```bash
code .gitignore
```

Add the following lines to the file:
```bash
*.bak
*~
```

This line instructs Git to ignore files that have file names ending in .bak or ~.

.gitignore is a very important file in the Git world because it prevents extraneous files from being submitted to version control. Boilerplate .gitignore files are available for popular programming environments and languages.

Save and close the editor, and then use these commands to commit the changes:
```bash
git add -A
git commit -m "Make small wording change; ignore editor backups"
```

#### Add a subdirectory
* Most websites use HTML and CSS style sheets
* style sheets are typically stored in a subdirectory

Add a subdirectory
```bash
mkdir CSS
```
> git status will not show anything to commit since it's an empty directory. It only tracks changes to files no directories.

Sometimes, especially in the initial stages of development, you want to have empty directories as placeholders. A common convention is to create an empty file, often called .git-keep, in a placeholder directory.

create an empty file with that name in the CSS subdirectory and add the contents of the subdirectory to the index:
```bash
touch CSS/.git-keep
git add CSS
```
git status should report a new file.

#### Replace a file
replace the .git-keep with a CSS file and update index.html to reference it
1. Delete .git-keep for CSS subdirectory:
```bash
rm CSS/.git-keep
```
2. create a file named site.css in the CSS subdirectory
3. add the following CSS to the file, save and close.
```css
h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
body { font-family: serif; }
```
4. add the following line to index.html (don't forget to go back up to the Cats directory) after the \<title\> line, and save the modified file:
```html
<link rel="stylesheet" href="CSS/site.css">
```

> Note that to change to the previous directory use `cd ..`

5. Use git status to see a summary of the files that have changed. Then, use the following commands to stage untracked files to version control and commit your changes to site.css and index.html:
```bash
git add .
git commit -m "Add a simple stylesheet"
```

#### List commits
You can use git log to view all the changes made, but use `git log --oneline` instead for concise listing.
Another useful option is `-nX`, where `X` is a commit number: 1 for the latest commit, 2 for the one before that, and so on. To see for yourself, try a `git log -n2` command.

### Unit 4: Fix simple mistakes
Sometimes, things go wrong. You might forget to add a new file, or maybe you add a file by mistake. Perhaps you made a spelling error in your latest commit or you committed something you didn't intend to. Perhaps you accidentally deleted a file.

With Git you always have a way to return to a previous state. You can also change commit history as long as it isn't shared.

#### Amend a commit: --amend flag
Suppose you were supposed to add the reference code in the html file:
```html
<link rel="stylesheet" href="CSS/site.css">
```
but you later realise that you added:
```html
<link rel="stylesheet" href="CS/site.css">
```
with the incorrect path CS.

You update the html with the correct reference. At this point you can:
* commit the corrected version
* put it in the same commit as the original

The `--amend` option to `git commit` lets you change history:
```bash
git commit --amend --no-edit
```
The `--no-edit` option tells git not to include a commit message. You can also use --amend to edit a commit message, to add files that were accidentally left out of the commit, or to remove files that were added by mistake.

#### Recover a deleted file: git checkout
* If you made changes to a file that breaks the project
* If you accidentally deleted a file
* You can revert to a previous version of that file, even if it no longer exists.
* `git checkout` updates files in the working tree to match the version in the index or in the specified tree.

If you've accidentally deleted a file, you can recover it by using this command:
```bash
git checkout -- <file_name>
```
You can also check out a file from an earlier commit (typically, the head of another branch), but the default is to get the file from the index. 

> The `--` in the argument list serves to separate the commit from the list of file paths. It's not strictly needed in this case, but if you had a branch named <file_name> (perhaps because that's the name of the file being worked on in that branch), `--` would prevent Git from getting confused.

#### Recover files: git reset
You can delete a file using `git rm`. This command deletes the file on your disk, but it also has Git record the file deletion in the index.

If you ran:
```bash
git rm index.html
git checkout -- index.html
```
Git would not restore the file:
```output
error: pathspec 'index.html' did not match any file(s) known to git.
```

To recover the file use `git reset` to unstage changes.
```bash
git reset HEAD index.html
git checkout -- index.html
```

Here, `git reset` unstages the file deletion from Git. This command brings the file back to the index, but the file is still deleted on disk. You can then restore it to the disk from the index by using `git checkout`.

> Many VCSes make files read-only to ensure that only one person at a time can make changes; users use an unrelated `checkout` command to get a writable version of the file. They also use `checkin` for an operation similar to what Git does with a combination of `add, commit, and push.` This fact occasionally causes confusion when people begin to use Git.

#### Revert a commit: git revert
* `git checkout` only works in situations where the changes to undo are in the index.
* After you committed changes you need to use something else.
* `git revert` reverts to the previous commit
* it makes another commit that cancels out the first commit.

We can use `git revert HEAD` to make a commit that's the exact opposite of our last commit, undoing the previous commit while leaving all history intact. The `HEAD` part of the command just tells Git that we want to "undo" only the last commit.

As an aside, you can also remove the most recent commit by using the `git reset` command:
```bash
git reset --hard HEAD^
```

There are several types of resets in Git:
* --mixed (default), resets index but not working tree and moves HEAD if you specify a different commit.
* --soft, moves HEAD only, leaves index and working tree. It leaves all changes as 'changes to be committed'.
* --hard, changes both index and working tree to match specified commit, any changes made to tracked files are discarded.

### Unit 5: Use Git to fix mistakes

> I recommend going through the module and practicing there.

#### Practice recovering a deleted file
#### Practice recovering a file that was deleted: git rm
#### Revert a commit

### Unit 6: Knowledge Check
### Unit 7: Summary
Congratulations! In this module, you learned how to create a git project and edit errors that existed within it.

You learned:

* How to create a new project in Git
* How to make commits to your Git workspace
* How to track changes and modify files in your Git workspace
* How to edit past commits in your Git workspace
* How to recover deleted files in your Git workspace
* How to undo a commit in Git

At this point, you know enough about Git to use to make and modify a project. Collaboration with other developers is where version control shines. Check out the other modules in this learning path for more about using Git with others!