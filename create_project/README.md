# Description

Script to create a project and its corresponding github repository.

The script asks a few questions and creates a local folder with `data meta templates docs report` subfolders. It will also create a github repository if desired. 

# Installation 

## Prerequisites

`create_project.sh` requires [github client](https://github.com/cli/cli) installed. 

The easiest way to installed it is with [Homebrew](https://brew.sh/). 

Please, check for updated instructions but a brief summary is:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

`echo "eval $(/home/$(whoami)/.linuxbrew/bin/brew shellenv)" >> /home/$(whoami)/.bash_profile`

(`.bash_profile` might be `.profile` in other OSs.)

`eval $(/home/$(whoami)/.linuxbrew/bin/brew shellenv)`

`brew install gh`

Check version:

`gh --version`


Authenticate to github:

`gh auth login` (recommended: If you're on a server, follow instructions to generate a token).

Set ssh as git protocol. This will allow the use of ssh key. If you have not specified it during the previous step, do:

`gh config set git_protocol ssh`




## Install create_project.sh




## Recommended

Add you the script.

# Use



# Bibliography

[Github client manual](https://cli.github.com/manual/)

