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


# + [markdown] slideshow={"slide_type": "subslide"}
# # Introduction to Git and GitHub
# ## Hackathon edition
#
# Kendra Oudyk
#
# 2021-02
#
# Much of this is borrowed from the [**"Version control with Git"**](https://swcarpentry.github.io/git-novice/) tutorial by Software Carpentries
# -

# # Roadmap
#
# - **Goals**
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - How do I contribute to an existing project?
# - Goals

# + [markdown] slideshow={"slide_type": "slide"}
# # Goals
# 1. Explain why git/GitHub are useful
# 2. Track and share your work using git/GitHub (git level 1: commit push)
# 3. Contribute to a project using git/GitHub (git level 2: branches PRs)
# -


# # On learning git & GitHub
# ![](figures/doing_and_understanding_cleaner.png)

# # Roadmap
#
# - Goals
# - **Setup**
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - How do I contribute to an existing project?
# - Goals

# + [markdown] slideshow={"slide_type": "slide"}
# ## Side note 1/2:
# # Not a fan of zoom chat for tutorials

# + [markdown] slideshow={"slide_type": "fragment"}
# ### When you have clarification question or need me to slow down
# ![](figures/zoom_icons/mic.png)

# + [markdown] slideshow={"slide_type": "fragment"}
# ### When you have a specific question/issue, ask in the mattermost channel
# help-git-GitHub_BHG2020-Montreal
#
# (e.g., "I'm seeing this error...")

# + [markdown] slideshow={"slide_type": "slide"}
# ## Side note 2/2:
#
# # Replace <> with your own info

# + [markdown] slideshow={"slide_type": "fragment"}
# e.g.,
#
# `github.com/<your_username>`
#
# becomes
#
# `github.com/koudyk`

# + [markdown] slideshow={"slide_type": "slide"}
# # Setup
# ### To follow on your machine, you'll need
# 1. Bash
# 2. Git
# 3. Text editor
# 4. GitHub account

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Check if you're ready
# 1. Can you open a text editor? (e.g., Linux: gedit, nano. macOS: textedit. Windows: notepad)
# 2. Can you go your GitHub account?
# 3. When you open a Bash shell and type `git --version`, does it output the version number? (**macOS / Linux**: you might need to run this: `conda install -c anaconda git`)
#
#
# Check off your answers in the poll
# ![](figures/zoom_icons/poll.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Configure git (if you haven't already)
# ```
# git config --global user.name "<Vlad Dracula>"
# git config --global user.email "<vlad@tran.sylvan.ia>"
# ```
# *use the email you used for your GitHub account*  👆
#
# #### macOS / Linux
# ```
# git config --global core.autocrlf input
# ```
#
# #### Windows
# ```
# git config --global core.autocrlf true
#
# ```
#
# When you're done, click
# ![](figures/zoom_icons/faster.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - **Why use git & GitHub?**
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - How do I contribute to an existing project?
# - Goals

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
# ![](https://swcarpentry.github.io/git-novice/fig/versions.svg)

# + [markdown] slideshow={"slide_type": "fragment"}
# ### And incorporate the changes
#
# ![](https://swcarpentry.github.io/git-novice/fig/merge.svg)
#
# https://swcarpentry.github.io/git-novice/

# + [markdown] slideshow={"slide_type": "slide"}
# # Open Science

# + [markdown] slideshow={"slide_type": "fragment"}
# ![](figures/open_science_buffet.png)
#
# <font color='lightgrey'>(Credit to Christina Bergmann for the idea of the 'Open Science Buffet')</font>


# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - **Where does git store information?**
# - How do I record changes in git?
# - How do I share my changes on the web?
# - How do I contribute to an existing project?
# - Goals

# + [markdown] slideshow={"slide_type": "slide"}
# Open your Bash shell (where you typed `git --version` at the beginning)
#
# Create a directory (remember Windows' slashes are the other way)
# ```
# cd ~/Desktop
# # # mkdir oudyks_desserts
# cd oudyks_desserts
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
# - How do I contribute to an existing project?
# - Goals

# + [markdown] slideshow={"slide_type": "slide"}
# ![](figures/workflow/w0_init.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/w1_local.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### `git add`
# ![](https://i.gifer.com/YKCS.gif)
# ### `git commit`
# ![](https://www.nydailynews.com/resizer/nJ3qGqkV_0Z6WzIGAWktQ0pKlIE=/415x229/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/JOYD6SAJXDW4JQJSKWAZIY266Y.jpg)

# + [markdown] slideshow={"slide_type": "slide"}
# Let's make a change!
# First, open a new file
# ```
# <text editor> desserts.md
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Write this in the file:
#
# > pie\
# > ice cream\
# > cookies
#
# Save and exit

# + [markdown] slideshow={"slide_type": "fragment"}
# Reminder to let me know if you need me to slow down
# ![](https://goldstarteachers.com/wp-content/uploads/2018/09/Confused-GIF.gif)

# + [markdown] slideshow={"slide_type": "subslide"}
# Let's check the status of our repo
# ```
# git status
# ```

# + [markdown] slideshow={"slide_type": "fragment"}
# Is this file being tracked by git?
# ![](figures/zoom_icons/poll.png)
#
# <font color='grey'>(hint: look at what your terminal says)</font>

# + [markdown] slideshow={"slide_type": "fragment"}
# How can we include this file in what will be committed?
# ![](figures/zoom_icons/chat_mic.png)


# + [markdown] slideshow={"slide_type": "subslide"}
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
# ## I change my mind...
# ## cookies are better than ice cream


# + [markdown] slideshow={"slide_type": "fragment"}
# ```
# $ <text editor> desserts.md
# ```
#
# > pie\
# > cookies\
# > ice cream
#
# Save and exit

# + [markdown] slideshow={"slide_type": "subslide"}
# Let's \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
# ```
# git diff
# ```
#
# How could we figure out what this command does?
# ![](figures/zoom_icons/chat_mic.png)

# + [markdown] slideshow={"slide_type": "fragment"}
# Let's stage and commit the change
# ```
# git ____ desserts.md
# git ____ -m "switch cookies and ice cream"
# ```
# ![](figures/zoom_icons/chat_mic.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Check your understanding


# + [markdown] slideshow={"slide_type": "fragment"}
# ## What does git track?
# ![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)


# + [markdown] slideshow={"slide_type": "fragment"}
# ### Does git track changes to each letter?
# ![](figures/zoom_icons/chat_mic.png)


# + [markdown] slideshow={"slide_type": "subslide"}
# ## How do I get Git to track a change?


# + [markdown] slideshow={"slide_type": "fragment"}
# Put these in order:
#
# a) `git commit -m "<this is what I did>"`\
# b) make the change\
# c) `git add <file>`
#
# ![](figures/zoom_icons/poll.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - **How do I share my changes on the web?**
# - How do I contribute to an existing project?
# - Goals

# + [markdown] slideshow={"slide_type": "slide"}
# ![](figures/workflow/w2_inspect.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/w3_remote.png)

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
# git remote add origin https://github.com/koudyk/oudyks_desserts.git
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


# + [markdown] slideshow={"slide_type": "fragment"}
# Refresh your GitHub repo

# + [markdown] slideshow={"slide_type": "fragment"}
# Click 'go faster' if you see `desserts.md` on your GitHub repo
# ![](figures/zoom_icons/faster.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - **How do I contribute to an existing project?**
# - Goals

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/w4_update.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/workflow/w5_upstream.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Branches

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/branches_features.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/branches_collab.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # I want to contribute!

# + [markdown] slideshow={"slide_type": "fragment"}
# ## Contributing task 1: Get everyone's favorite desserts!
#
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ![](figures/issues.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Roadmap
#
# - Goals
# - Setup
# - Why use git & GitHub?
# - Where does git store information?
# - How do I record changes in git?
# - How do I share my changes on the web?
# - How do I contribute to an existing project?
# - **Goals**

# + [markdown] slideshow={"slide_type": "slide"}
# # Did we meet our goals?

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 1. Explain why git & GitHub are useful

# + [markdown] slideshow={"slide_type": "fragment"}
# ... to a new grad student
# ![](figures/zoom_icons/chat_mic.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 2. Track and share your work using git/GitHub (git level 1: commit push)
#


# + [markdown] slideshow={"slide_type": "fragment"}
# `status` &nbsp; &nbsp;
# `add` &nbsp; &nbsp;
# `init` &nbsp; &nbsp;
# `commit` &nbsp; &nbsp;
# `diff` &nbsp; &nbsp;
# `push` &nbsp; &nbsp;
#
# **Basic workflow for tracking a change and putting it on GitHub**
# - make a change
# - stage the change: `git ____ <filename>`
# - commit the change: `git ____ -m "<commit message>"`
# - put the change on GitHub: `git ____ origin main`
#
# **See what's happening with git**
# - show the working tree status: `git ____`
# - show how the file changed: `git ____`
#
# ![](figures/zoom_icons/poll.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 3. Contribute to a project using git/GitHub (git level 2: branches PRs)

# + [markdown] slideshow={"slide_type": "fragment"}
# #### Contributing task 2: Correct spelling mistakes in desserts lists
#
# ![](figures/issues.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](https://media1.tenor.com/images/ae1fd92f4ed82fba165d777e4a05c9de/tenor.gif?itemid=14220287)


# + [markdown] slideshow={"slide_type": "slide"}
# # There's so much more!

# + [markdown] slideshow={"slide_type": "fragment"}
# # Git buffet
# ![](figures/git_github_buffet.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Git is hard
# Here are some tips

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Sit down and go through a tutorial
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
# ![](figures/doing_and_understanding_cleaner.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Quick feedback
#
# ### How much of this tutorial could you follow?
# - 100 %
# - 75 %
# - 50 %
# - 25 %
# - 0 %
#
# ![](figures/zoom_icons/poll.png)


# + [markdown] slideshow={"slide_type": "slide"}
# # The End
#
#
# Software Carpentry's tutorial: https://swcarpentry.github.io/git-novice/
#
# ![](https://media.riffsy.com/images/f9fd6fdf307421f068d82cd050eae236/tenor.gif)
#
