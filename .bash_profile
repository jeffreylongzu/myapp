# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

export PATH=$PATH:$HOME/bin:/usr/local/mysql/bin

export PS1="`hostname`:\$PWD# "
