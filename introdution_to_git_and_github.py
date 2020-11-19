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

# + [markdown] slideshow={"slide_type": "slide"}
# # Introduction to Git and GitHub
#
# For NEUR608 \
# 2020-11-19 \
# Kendra Oudyk

# + [markdown] slideshow={"slide_type": "slide"}
# # Goals for today
#
# ## 1. Explain why git & GitHub are useful
#
# ## 2. Be able to track and share your work using git & GitHub
#

# + [markdown] slideshow={"slide_type": "fragment"}
# # Is this workshop for you?

# + [markdown] slideshow={"slide_type": "slide"}
# # On learning git & GitHub 
# ![](figures/doing_and_understanding_with_line.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Outline
#
# - Setup
# - Why use git & GitHub
# - How git works
#   - Where does git store information?
#   - 
# - Hands-on: How to and share your work (Goal 2)
# -

# # Setup
#
# ## To follow on your machine, you'll need
# 1. Bash 
# 2. Git 
# 3. Text editor 
# 4. GitHub account
#
# ## Let's check
# - Open a Bash shell and type
# ```
# git --version
# ```
# - Open a text editor
# - Go to your github page
#
# ## Configure git
# ```
# git config --global user.name "Vlad Dracula"
# git config --global user.email "vlad@tran.sylvan.ia"
# ```
#
# ## Line endings
# #### macOS / Linux
# ```
# git config --global core.autocrlf input
# ```
#
# #### Windows
# ```
# git config --global core.autocrlf input
# ```

# + [markdown] slideshow={"slide_type": "slide"}
# #### Part 1/3
# # Why use git & GitHub?
# #### (Goal 1)
#

# + [markdown] slideshow={"slide_type": "slide"}
# ![](https://uidaholib.github.io/get-git/images/phd101212s.gif)
# “Piled Higher and Deeper” by Jorge Cham, http://www.phdcomics.com

# + [markdown] slideshow={"slide_type": "slide"}
# ### Why use git & GitHub?
# # Version control
#

# + [markdown] slideshow={"slide_type": "fragment"}
# ### What is version control and why should I use it?
# - your ideas

# + [markdown] slideshow={"slide_type": "slide"}
# ## Record versions by tracking *changes*
# It's like having an unlimited "undo" button
# ![](https://swcarpentry.github.io/git-novice/fig/play-changes.svg)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Make independent changes
# ![](https://swcarpentry.github.io/git-novice/fig/versions.svg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## And incorporate the changes
# ![](https://swcarpentry.github.io/git-novice/fig/merge.svg)

# + [markdown] slideshow={"slide_type": "slide"}
# ### Why use git & GitHub?
# # Open Science

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/open_science_buffet.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ![](figures/open_science_buffet_with_circle.png)
# -

# #### Part 2/3
# # How git & GitHub work
# #### (FYI)

#

#

# ![](https://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

#

# # Goal 2: Track and share your work

# # Git buffet
# ![](figures/git_github_buffet.png)

# # Git buffet
# ![](figures/git_github_buffet_with_square.png)

#

#

#

#

#

#

# + [markdown] slideshow={"slide_type": "slide"}
#

# + [markdown] slideshow={"slide_type": "slide"}
#

# + [markdown] slideshow={"slide_type": "slide"}
#
# -

#

#

# + [markdown] slideshow={"slide_type": "slide"}
# # Did we meet our goals?
#

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 1. Explain why git & GitHub are useful
# To a 10-year-old

# + [markdown] slideshow={"slide_type": "subslide"}
# ## 2. Track and share your work 
#
# Short exercise: fill in the blanks

# + [markdown] slideshow={"slide_type": "subslide"}
# Git commands: `clone` &nbsp; &nbsp; `status` &nbsp; &nbsp; `add` &nbsp; &nbsp; `commit` &nbsp; &nbsp; `push` \
# Other stuff: `"add abstract to README"` &nbsp; &nbsp;`README.md`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 1. Make a GitHub repo 
# Create a repo called 'autism_connectivity'

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 2. Copy the GitHub repo onto your machine
# `git ____ https://github.com/username/autism_connectivity.git`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 3. Modify something 
# Add your abstract to the README.md

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 4. Stage the change
# `git ____ ___`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 5. Record the change
# `git ____ -m ____`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 6. Update the GitHub repo with your changes
# `git ____ origin main`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 3. Modify something 
# Create the file preprocessing.py

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 4. Stage the change
# `git ____ ___`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 5. Record the change
# `git ____ -m "____"`

# + [markdown] slideshow={"slide_type": "fragment"}
# #### 6. Update the GitHub repo with your changes
# `git ____ origin main`
# -

#

# + [markdown] slideshow={"slide_type": "slide"}
# # Git is hard
# Here are some tips

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Sit down and learn on your own
# ![](figures/swc_git_website.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Don't expect to remember everything
# ![](figures/google_stuff.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Keep common commands on a sticky note
# ![](figures/sticky_note_on_laptop.jpg)
# -











# # SKIP THIS SLIDE. It's for putting the steps out of order agian
#
# a) Make a GitHub repo
#
# b) Record the change
#
# c) Stage the change
#
# d) Update the GitHub repo with your changes
#
# e) Copy the GitHub repo onto your machine
#
# f) Modify something






