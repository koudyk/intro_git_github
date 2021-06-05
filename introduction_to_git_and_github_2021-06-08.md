---
jupyter:
  jupytext:
    encoding: '# -*- coding: utf-8 -*-'
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "skip"} -->

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
Kendra, click record!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
# Introduction to Git and GitHub

Kendra Oudyk

2021-06-06

Much of this is borrowed from the [**"Version control with Git"**](https://swcarpentry.github.io/git-novice/) tutorial by Software Carpentries
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Goals
1. **Explain why git/GitHub are useful**
2. Explain basically how git works
3. Track and share your work using git/GitHub
4. Contribute to a project using git/GitHub
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->

![](https://uidaholib.github.io/get-git/images/phd101212s.gif)
“Piled Higher and Deeper” by Jorge Cham, http://www.phdcomics.com

*Note: we don't usually track doc's with git*
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Automated version control
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Record versions by tracking *changes*
It's like having an unlimited "undo" button
![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Make independent changes
![](https://swcarpentry.github.io/git-novice/fig/versions.svg)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
### And incorporate the changes

![](https://swcarpentry.github.io/git-novice/fig/merge.svg)

https://swcarpentry.github.io/git-novice/
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
# Git vs GitHub

Git is the "language". It can be installed on any platform

GitHub hosts git repositories in remote locations. GitHub is a company, the future of this company is unknown !  
Other places specialized in hosting git repositories on the web:
- Gitlab
- Bitbucket
- ...


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
# Git & GitHub make your work more efficient

"Time is money"

- Git was built because Linus Torwarld realized that merging the work of thousands of linux kernel contributors was getting impossible with other source control systems
- Since then: it has been adopted very widely: there is a reason :)
- Git is good for companies and large project: it is also for scientists
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
# Git & GitHub let you track your work
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
# ... as well as info *about* your work

- what was the change
- who did it
- why
- when
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
![](figures/git_log_on_github.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
![](figures/merge.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
![](figures/pull_request_convo.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Git/GitHub can help you do Open Science
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
![](figures/open_science_buffet.png)

<font color='lightgrey'>(Credit to Christina Bergmann for the idea of the 'Open Science Buffet')</font>
<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
# Goals
1. Explain why git/GitHub are useful
2. **Explain basically how git works**
3. Track and share your work using git/GitHub
4. Contribute to a project using git/GitHub
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
# What's a repository?

- all files & folders in the project
- each file's revision history
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
![](figures/file_history.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## What do we "track" with git ?

- Generally : ascii files
- Generally : small files (ascii files are often "small")
- A repository is composed of a set of files and directories ! 
- We know a directory (equivalently: folder) is a git repository because there is a ".git" folder in it
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# What are branches?
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
![](figures/branches_tutorial.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
![](figures/branches_statsmodels.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
git was originally made for Linux development, which involves 1000's of contributers.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Goals
1. Explain why git/GitHub are useful
2. Explain basically how git works
3. **Track and share your work using git/GitHub**
4. Contribute to a project using git/GitHub
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Common workflow
# Track and share your work using git/GitHub
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
![](figures/workflow/w3_remote.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Create a new directory
And change into the directory

`mkdir <directory name>`\
`cd <directory name>`
![](figures/code/mkdir.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## Make it into a git repository
`git init`
![](figures/code/init.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Make a change
e.g., create a file called 'README.md'

![](figures/code/touch.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## Check what git is aware of
`git status`

![](figures/code/status_before_add.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Add the file so git is aware of it
Put it in the "staging area"
![](https://i.gifer.com/YKCS.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
`git add <filename>`
![](figures/code/add_then_status.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Take a snapshot of the staging area
![](https://www.nydailynews.com/resizer/nJ3qGqkV_0Z6WzIGAWktQ0pKlIE=/415x229/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/JOYD6SAJXDW4JQJSKWAZIY266Y.jpg)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
`git commit -m "<short, informative commit message>"`
![](figures/code/commit.png)
<!-- #endregion -->

<!-- #region -->
## What does all this *actually* look like?


- commits: what are they under the hood ? 

Commits are simply "hashes". You take hashes of files, hashes of the directories, and then hash these hashes !!! 
See https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html for a great explanation of what is a "commit"

(but, what is a "hash" ?)
(where are these in .git ?) 


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Create a corresponding GitHub repo for sharing your work

![](figures/github_new_repo.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Tell git the address of your remote repository
`git remote add <remote name> <remote location>`
![](figures/code/remote_add.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## Rename principal branch from *master* to *main* (if needed)
![](figures/code/branch_name_to_main.png)
<!-- #endregion -->

## while we are talking of branches ...

- branches: what are they ? 

So small, so simple ! branches are little ascii files, the name of the file is the branch name, the content is the commit hash !

- and while we are here : what is a tag ?

A tag is very much like a branch, but will always keep the same commit. It is another name for a commit !

<!-- #region slideshow={"slide_type": "subslide"} -->
## Push changes to github
`git push <remote> <branch>`\
(the `-u` is needed only the first time) 
![](figures/code/push.png)
*Note that GitHub is depreciating this authentication method*
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Goals
1. Explain why git/GitHub are useful
2. Explain basically how git works
3. Track and share your work using git/GitHub
4. **Contribute to a project using git/GitHub**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Common workflow
# Contributing to a project using git/GitHub
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
![](figures/workflow/w5_upstream.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Open/find an issue to work on
![](figures/code/issue.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## (Wait for approval)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Fork the respository on GitHub
(If you haven't already)
![](figures/fork.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Download the forked repository onto your machine
`git clone <remote's url>.git`
![](figures/code/clone_then_cd.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
## Or, if you already have it, pull any changes that your collaborators made
`git pull <remote> <branch>`
![](figures/code/pull_upstream.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Prepare to make changes
Create a new branch on which store any new changes, and switch to that branch

`git checkout -b <yourBranch>` \
(`git branch <yourBranch>` + `git checkout <yourBranch>`)

![](figures/code/checkout_b.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Make changes
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## See changes
`git status`
![](figures/code/status_before_add2.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
`git diff`
![](figures/code/diff_before_add.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Stage changes
`git add <file1> <file2>`
![](figures/code/add.png)

![](https://i.gifer.com/YKCS.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Take the snapshot of the staging area
`git commit -m "<short, informative commit message>"`

![](figures/code/commit2.png)

![](https://www.nydailynews.com/resizer/nJ3qGqkV_0Z6WzIGAWktQ0pKlIE=/415x229/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/JOYD6SAJXDW4JQJSKWAZIY266Y.jpg)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Share your work
`git push <remote> <branch>`

![](figures/code/push2.png)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Pull request
(ask collaborators to add your changes)
![](figures/code/pull_request.gif)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Let's see how the graph changed
![](figures/code/network_graph_pr.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Goals
1. Explain why git/GitHub are useful
2. Explain basically how git works
3. Track and share your work using git/GitHub
4. Contribute to a project using git/GitHub

*We'll practice 3. and 4. at the end of this workshop*
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Check your understanding

# Why would you use git? 
Explain it in one sentence to a new grad student.
![](figures/zoom_icons/chat.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Check your understanding

# What does git track?
a) letter changes\
b) line changes\
c) document changes

![](figures/zoom_icons/poll.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Check your understanding
# Put these commands in order
to form a basic workflow for tracking and sharing a change. 


`commit` &nbsp; &nbsp;
`push` &nbsp; &nbsp;
`add` &nbsp; &nbsp;

- make a change
- stage the change: `git ____ <filename>`
- commit the change: `git ____ -m "<commit message>"`
- put the change on GitHub: `git ____ origin main`

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# There's so much more!
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
# Git buffet
![](figures/git_github_buffet.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
# Git is hard
Here are some tips
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Sit down and go through a tutorial
![](figures/swc_git_website.png)

![](figures/swc_coverage.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Don't expect to remember everything
![](figures/google_stuff.png)
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
## Keep common commands on a sticky note
![](figures/sticky_note_on_laptop.jpg)
<!-- #endregion -->
<!-- #region slideshow={"slide_type": "slide"} -->
# The End


Software Carpentry's tutorial: https://swcarpentry.github.io/git-novice/

![](https://media.riffsy.com/images/f9fd6fdf307421f068d82cd050eae236/tenor.gif)

<!-- #endregion -->
