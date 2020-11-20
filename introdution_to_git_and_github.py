# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "skip"}
#

# + [markdown] slideshow={"slide_type": "slide"}
# # Introduction to Git and GitHub
#
# For NEUR608 \
# 2020-11-19 \
# Kendra Oudyk

# + [markdown] slideshow={"slide_type": "slide"}
# # Goals
#
# ### 1. Explain why git & GitHub are useful
#
# ### 2. Be able to track and share your work using git & GitHub
#

# + [markdown] slideshow={"slide_type": "subslide"}
# # What's your experience?
# ### Respond with 'yes'  if you're comfortable with 
# ![](figures/zoom_icons/yes.png)

# + [markdown] slideshow={"slide_type": "fragment"}
# Bash

# + [markdown] slideshow={"slide_type": "fragment"}
# Git
# (These commands: `status` &nbsp; &nbsp; 
# `add` &nbsp; &nbsp; 
# `init` &nbsp; &nbsp; 
# `commit` &nbsp; &nbsp; 
# `diff` &nbsp; &nbsp; 
# `push` &nbsp; &nbsp;)

# + [markdown] slideshow={"slide_type": "fragment"}
# GitHub

# + [markdown] slideshow={"slide_type": "fragment"}
# # Is this workshop for you?

# + [markdown] slideshow={"slide_type": "slide"}
# # On learning git & GitHub 
# ![](figures/doing_and_understanding_with_line.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# # When you're not following, 
# # turn on your mic and say something :) 
#

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - **Setup**
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - Goals
# - Conclusion

# + [markdown] slideshow={"slide_type": "fragment"}
# Much of this is borrowed from the **"Version control with Git"** tutorial by Software Carpentries
#
# https://swcarpentry.github.io/git-novice/
#

# + [markdown] slideshow={"slide_type": "slide"}
# # Setup

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Which operating system are you using?
#
#
# Windows
# ![](figures/zoom_icons/no.png)
#
# MacOS
# ![](figures/zoom_icons/slower.png)
#
# Linux
# ![](figures/zoom_icons/yes.png)
#
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ## To follow on your machine, you'll need
# 1. Bash 
# 2. Git 
# 3. Text editor 
# 4. GitHub account

# + [markdown] slideshow={"slide_type": "fragment"}
# ## Check if you're ready
# - Can you open a text editor?
# - Can you go your GitHub account?
# - When you open a Bash shell and type `git --version`, does it output the version number?

# + [markdown] slideshow={"slide_type": "fragment"}
# If you answered 'yes' to all 3, click 'yes'
# ![](figures/zoom_icons/yes.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Configure git
# ```
# git config --global user.name "Vlad Dracula"
# git config --global user.email "vlad@tran.sylvan.ia"
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# #### macOS / Linux
# ```
# git config --global core.autocrlf input
# ```
#
# #### Windows
# ```
# git config --global core.autocrlf true
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# When you're done, click 'yes'
# ![](figures/zoom_icons/yes.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - **Why use git & GitHub?**
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - Goals
# - Conclusion

# + [markdown] slideshow={"slide_type": "slide"}
#
# ![](https://uidaholib.github.io/get-git/images/phd101212s.gif)
# “Piled Higher and Deeper” by Jorge Cham, http://www.phdcomics.com

# + [markdown] slideshow={"slide_type": "slide"}
# #### Why use git & GitHub?
#
# # Automated version control

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Record versions by tracking *changes*
# It's like having an unlimited "undo" button
# ![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Make independent changes
# e.g., while collaborating
#
# ![](https://swcarpentry.github.io/git-novice/fig/versions.svg)

# + [markdown] slideshow={"slide_type": "fragment"}
# ### And incorporate the changes
#
# ![](https://swcarpentry.github.io/git-novice/fig/merge.svg)
#
# https://swcarpentry.github.io/git-novice/

# + [markdown] slideshow={"slide_type": "slide"}
# ### Why use git & GitHub?
# # Open Science

# + [markdown] slideshow={"slide_type": "fragment"}
# ![](figures/open_science_buffet.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - **Where does git store information?**
# - How do I record changes in git?
# - How do I share my changes on the web?
# - Goals
# - Conclusion

# + [markdown] slideshow={"slide_type": "slide"}
# Open your Bash shell (where you typed `git --version` at the beginning)
#
# Create a directory
# ```
# cd ~/Desktop
# # # mkdir kendras_desserts
# cd kendras_desserts
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# What's in our directory?
# ```
# # # ls -a
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Create a git repository
# ```
# git init
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# What's in our directory now?
# ```
# # # ls -a
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# **The `.git` subdirectory is where git stores all the info it needs to do version control**

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - **How do I record changes in git?**
# - How do I share my changes on the web?
# - Goals
# - Conclusion

# + [markdown] slideshow={"slide_type": "slide"}
# ![](figures/workflow/wf1_our_machine.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/wf2_dot_git.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/wf3_full_our_machine.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/wf4_our_machine_workflow.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### `git add`
# ![](https://i.gifer.com/YKCS.gif)
# ### `git commit`
# ![](https://lh3.googleusercontent.com/proxy/X4XJAX5f-JVxMBrXfHTupEagyCxjUc5VXY-th6wWMoC_NprWkloraT0JA5c69rkhtuZ1w0eyLA-F28SJP8TXB8UV4AeZWku5zPHd4mBdcZphJuHQD1TggyRo4vmn81H7nHeDKXdCBswm7TZP05jAOYBi__tSA36DfaYrzcrVOyG1m-3YZ4kidsGsr-1cg9U8lZS9fzgCuTNP8bQJUhRyH-4Y05SJmMB6)

# + [markdown] slideshow={"slide_type": "slide"}
# Let's make a change!
# First, open a new file
# ```
# <text editor> desserts.md
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Write this in the file:
#
# > My favorite desserts are:
# > 1. pie
# > 2. ice cream
# > 3. cookies
#
# Save and exit

# + [markdown] slideshow={"slide_type": "subslide"}
# Let's check the status of our repo
# ```
# git status
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's stage the change
# ```
# git add desserts.md
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's check the status of our repo
# ```
# git status
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's commit the change
# ```
# git commit -m "list my favorite desserts"
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's check the status of our repo
# ```
# git status
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# # We forgot cake! 

# + [markdown] slideshow={"slide_type": "fragment"}
# ```
# <text editor> desserts.md
# ```
#
# > My favorite desserts are:
# > 1. pie
# > 2. ice cream
# > 3. cookies
# > 4. cake
#
# Save and exit

# + [markdown] slideshow={"slide_type": "subslide"}
# Let's see what git tracked
# ```
# git diff
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's check the status of our repo
# ```
# git ____
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's stage and commit the change
# ```
# git ____ desserts.md
# git commit -m "add cake to list of desserts"
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# # ACTUALLY, cookies are better than ice cream
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ```
# <text editor> desserts.md
# ```
# > My favorite desserts are:
# > 1. pie
# > 2. cookies
# > 3. ice cream
# > 4. cake
#
# Save and exit

# + [markdown] slideshow={"slide_type": "subslide"}
# Let's \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
# ```
# git diff
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's stage and commit the change
# ```
# git ____ desserts.md
# git ____ -m "switch cookies and ice cream"
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# # Check your understanding
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ## What does git track?
# ![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ## How do I get Git to track a change?
#

# + [markdown] slideshow={"slide_type": "fragment"}
# Put these in order
# - `git commit -m "<this is what I did>"`
# - make the change
# - `git add <file>`
# ![](figures/workflow/wf4b_empty_workflow.png)

# + [markdown] slideshow={"slide_type": "fragment"}
# ### Add your favorite dessert to the list and track the change
#

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - **How do I share my changes on the web?**
# - Goals
# - Conclusion

# + [markdown] slideshow={"slide_type": "slide"}
# ![](figures/workflow/wf5_remote_workflow.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Create a remote repo

# + [markdown] slideshow={"slide_type": "fragment"}
# - Go to github.com

# + [markdown] slideshow={"slide_type": "fragment"}
# - Beside **Repositories**, click **New** 

# + [markdown] slideshow={"slide_type": "fragment"}
# - Enter your repo name
# - Choose to make your repo Public or Private
# - Don't check any boxes
# - Click **Create repository**


# + [markdown] slideshow={"slide_type": "subslide"}
# ## Link it to your local repo

# + [markdown] slideshow={"slide_type": "fragment"}
# Tell git the URL of your remote repo and name it 'origin'
# ```
# git remote add origin https://github.com/koudyk/kendras_desserts.git
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Set the name of your principle branch to main (if it's not already)
# ```
# git branch -M main
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Push your changes to GitHub
# ```
# git push -u origin main
# ```
#

# + [markdown] slideshow={"slide_type": "fragment"}
# Refresh your GitHub repo

# + [markdown] slideshow={"slide_type": "fragment"}
# Click 'yes' if you see `desserts.md` on your GitHub repo
# ![](figures/zoom_icons/yes.png)

# + [markdown] slideshow={"slide_type": "slide"}
# ### Use GitHub to look at your file's history

# + [markdown] slideshow={"slide_type": "fragment"}
# On your GitHub repo
# - Click on **desserts.md**
#
# - Click **History** 

# + [markdown] slideshow={"slide_type": "fragment"}
# - What do we see when we click on a commit message?

# + [markdown] slideshow={"slide_type": "fragment"}
# - What do we see when we click on **<>**

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - **Goals**
# - Conclusion

# + [markdown] slideshow={"slide_type": "slide"}
# # Did we meet our goals?

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 1. Explain why git & GitHub are useful

# + [markdown] slideshow={"slide_type": "fragment"}
# ... to a 10-year-old

# + [markdown] slideshow={"slide_type": "fragment"}
# ... for your final project in NEUR608

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 2. Track and share your work  using git & GitHub
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ### Fill in the blanks

# + [markdown] slideshow={"slide_type": "fragment"}
# `status` &nbsp; &nbsp; 
# `add` &nbsp; &nbsp; 
# `init` &nbsp; &nbsp; 
# `commit` &nbsp; &nbsp; 
# `diff` &nbsp; &nbsp; 
# `push` &nbsp; &nbsp; 

# + [markdown] slideshow={"slide_type": "fragment"}
# Basic workflow for tracking a change and putting it on GitHub
# - make a change
# - stage the change: `git ____ <filename>`
# - commit the change: `git ____ -m "<commit message>"`
# - put the change on GitHub: `git ____ origin main`
#
# See what's happening with git
# - check repo status: `git ____`
# - check what git tracked: `git ____`

# + [markdown] slideshow={"slide_type": "fragment"}
# ### Now use each command 
# to make a file called `snacks.md` in the `desserts` folder

# + [markdown] slideshow={"slide_type": "slide"}
# ![](https://media1.tenor.com/images/ae1fd92f4ed82fba165d777e4a05c9de/tenor.gif?itemid=14220287)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - Goals
# - **Conclusion**

# + [markdown] slideshow={"slide_type": "slide"}
# # There's so much more to git & GitHub!

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/wf6_extras.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/wf7_extras_remote.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# # Git buffet
# ![](figures/git_github_buffet.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Git is hard
# Here are some tips

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Sit down and go throuh a tutorial
# ![](figures/swc_git_website.png)
#
# ![](figures/swc_coverage.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Don't expect to remember everything
# ![](figures/google_stuff.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Keep common commands on a sticky note
# ![](figures/sticky_note_on_laptop.jpg)
# + [markdown] slideshow={"slide_type": "subslide"}
# ## To learn it, you need to *commit* to doing it
# ![](figures/doing_and_understanding_with_line.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # The End
#
#
# Sofware Carpentry's tutorial: https://swcarpentry.github.io/git-novice/
#
# My repo with these slides: https://github.com/koudyk/intro_git_github
#
# ![](https://media.riffsy.com/images/f9fd6fdf307421f068d82cd050eae236/tenor.gif)
#
