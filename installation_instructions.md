# Installation instructions

*These instructions are largely quoted from the [setup instructions for NeuroHackademy](https://neurohackademy.org/setup/)*

## Summary
For this class, you'll need
1. A Bash shell
2. The version control system [Git](https://git-scm.com/)
3. A text editor you’re comfortable with (nano, emacs, vi, Sublime Text, Atom, VSCode, etc.)
4. A [GitHub](https://github.com/) account. Basic GitHub accounts are free, and we encourage you to create a GitHub account if you don’t have one already. Please consider what personal information you’d like to reveal. For example, you may want to review these [instructions for keeping your email address private provided at GitHub](https://help.github.com/articles/keeping-your-email-address-private/).
5. A modern browser (current versions of Chrome, Firefox or Safari, or Internet Explorer version 9 or above)

## Detailed instructions
Here are the instructions for installing a Bash shell, Git, and a text editor on [Windows](#windows), [Mac OS X](#mac-os-x), or [Linux](#linux). 

Bash is a commonly-used shell that gives you the power to do simple tasks more quickly. Git is a version control system that lets you track who made changes to what when and has options for easily updating a shared or public version of your code on github.com. 

### Windows
#### THE BASH SHELL and GIT
Installing Git Bash will give you both Git and Bash.

[Video tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)

1. Download the Git for Windows installer.
2. Run the installer and follow the steps bellow:
    - Click on “Next”.
    - Click on “Next”.
    - **Keep “Use Git from the Windows Command Prompt” selected and click on “Next”.**
    - Click on “Next”.
    - **Keep “Checkout Windows-style, commit Unix-style line endings” selected and click on “Next”.**
    - **Keep “Use Windows’ default console window” selected and click on “Next”.**
    - Click on “Install”.
    - Click on “Finish”.
3. If your “HOME” environment variable is not set (or you don’t know what this is):
    - Open command prompt (Open Start Menu then type `cmd` and press [Enter])
    - Type the following line into the command prompt window exactly as shown:`setx HOME "%USERPROFILE%"`
    - Press [Enter], you should see `SUCCESS: Specified value was saved`.
    - Quit command prompt by typing exit then pressing [Enter]

To check your installation, open your bash shell and type `git --version` and press [enter]. The output should be something like `git version 2.17.1` (the numbers will probably be different).

#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **Notepad** is a text editor that comes with Windows, and it will serve for the purpose of our workshop. 

### Mac OS X
#### THE BASH SHELL
The default shell in all versions of Mac OS X is Bash, so no need to install anything. You access Bash from the Terminal (found in `/Applications/Utilities`). See the Git installation [video tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY) for an example on how to open the Terminal. You may want to keep Terminal in your dock for this class.

#### GIT
[Video Tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY)

For OS X 10.9 and higher, install Git for Mac by downloading and running the most recent “mavericks” installer from this list. After installing Git, there will not be anything in your /Applications folder,
as Git is a command line program. 

For older versions of OS X (10.5-10.8) use the most recent available installer labelled “snow-leopard” available here.

To check your installation, open your bash shell and type `git --version` and press [enter]. The output should be something like `git version 2.17.1` (the numbers will probably be different).

#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **TextEdit** is a text editor that comes with Mac OS X, and it will serve for the purpose of our workshop. 


### Linux
#### THE BASH SHELL
The default shell is usually Bash, but if your machine is set up differently you can run it by opening a
terminal and typing `bash`. There is no need to install anything.

#### GIT
Option 1: Install through the bash terminal
- If you have a Debian/Ubuntu operating system, open bash and run `sudo apt-get install git` 
- If you have a Fedora operating system, open bash and run `sudo yum install git`

Option 2: Install through the package manager
- Search for 'git' on your distrubution's package manager (e.g., this is called 'Ubuntu Software' on the Ubuntu OS)
- Click 'install' 

To check your installation, open your bash shell and type `git --version` and press [enter]. The output should be something like `git version 2.17.1` (the numbers will probably be different).

#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **Gedit** is a text editor that comes with many linux distributions, and it will serve for the purpose of our workshop. 
