# Installation instructions

*These instructions are largely quoted from the [setup instructions for Software Carpentries](https://carpentries.github.io/workshop-template/#git)*

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

<h1> <img src="https://diymediahome.org/wp-content/uploads/Windows_7_logo.png"
  width="60"
  height="60"
  style="float:left;">
    ### Windows

#### THE BASH SHELL and GIT

Installing Git Bash will give you both Git and Bash.

[Video tutorial](https://youtu.be/339AEqk9c-8)

1. Download the [Git for Windows installer](https://gitforwindows.org/).
2. Find the installer in your Downloads folder, click on it, and follow the steps bellow:
    - Click on "Next" four times (two times if you've previously installed Git). You don't need to change anything in the Information, location, components, and start menu screens.
    - **From the dropdown menu select "Use the Nano editor by default" (NOTE: you will need to scroll up to find it) and click on "Next".** If this doesn't work, select "Vim".
    - On the page that says "Adjusting the name of the initial branch in new repositories", ensure that "Let Git decide" is selected. This will ensure the highest level of compatibility for our lessons.
    - Ensure that "Git from the command line and also from 3rd-party software" is selected and click on "Next". (If you don't do this Git Bash will not work properly, requiring you to remove the Git Bash installation, re-run the installer and to select the "Git from the command line and also from 3rd-party software" option.)
    - Ensure that "Use the native Windows Secure Channel Library" is selected and click on "Next".
    - Ensure that "Checkout Windows-style, commit Unix-style line endings" is selected and click on "Next".
    - **Ensure that "Use Windows' default console window" is selected and click on "Next".**
    - Ensure that "Default (fast-forward or merge) is selected and click "Next"
    - Ensure that "Git Credential Manager Core" is selected and click on "Next".
    - Ensure that "Enable file system caching" is selected and click on "Next".
    - Click on "Install".
    - Click on "Finish" or "Next".
3. If your “HOME” environment variable is not set (or you don’t know what this is):
    - Open command prompt (Open Start Menu then type cmd and press [Enter])
    - Type the following line into the command prompt window exactly as shown:`setx HOME "%USERPROFILE%"`
    - Press [Enter], you should see SUCCESS: Specified value was saved.
    - Quit command prompt by typing `exit` then pressing [Enter]


#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **Notepad** is a text editor that comes with Windows, and it will serve for the purpose of our workshop. 

### Mac OS X
#### THE BASH SHELL
[Video tutorial](https://youtu.be/9LQhwETCdwY)

The default shell in some versions of macOS is Bash, and Bash is available in all versions, so no need to install anything. You access Bash from the Terminal (found in `/Applications/Utilities`). See the Git installation [video tutorial](https://carpentries.github.io/workshop-template/#shell-macos-video-tutorial) for an example on how to open the Terminal. You may want to keep Terminal in your dock for this workshop.

To see if your default shell is Bash type `echo $SHELL` in Terminal and press the Return key. If the message printed does not end with '/bash' then your default is something else and you can run Bash by typing `bash` .


#### GIT
[Video Tutorial](https://youtu.be/9LQhwETCdwY)

For OS X 10.9 and higher, install Git for Mac by downloading and running the most recent "mavericks" installer from this list. Because this installer is not signed by the developer, you may have to right click (control click) on the .pkg file, click Open, and click Open on the pop up window. After installing Git, there will not be anything in your `/Applications` folder, as Git is a command line program. 

For older versions of OS X (10.5-10.8), use the most recent available installer labelled "snow-leopard" [available here](http://sourceforge.net/projects/git-osx-installer/files/).


#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **TextEdit** is a text editor that comes with Mac OS X, and it will serve for the purpose of our workshop. 


### Linux
#### THE BASH SHELL
The default shell is usually Bash and there is usually no need to install anything.

To see if your default shell is Bash type `echo $SHELL` in a terminal and press the Enter key. If the message printed does not end with '/bash' then your default is something else and you can run Bash by typing `bash` .


#### GIT
If Git is not already available on your machine you can try to install it via your distro's package manager:
- For Debian/Ubuntu run `sudo apt-get install git`
- For Fedora run `sudo dnf install git` 

#### TEXT EDITOR
If you don't already have a text editor that you're familiar with, **Gedit** is a text editor that comes with many linux distributions, and it will serve for the purpose of our workshop. 
