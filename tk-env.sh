#!/bin/bash

#
# This script helps to prepear environment for test-kitchen installation
#

RUBYVER="2.2.5"

# check rvm
if rvm --version >/dev/null 2>&1 ; then
  echo "RVM is installed! Please delete"
  exit 0
fi

# check git
if ! git --version >/dev/null 2>&1 ; then
  echo "Git is not installed!"
  exit 0
fi

# check virtualbox
if ! VBoxHeadless --version >/dev/null 2>&1 ; then
  echo "Virtualbox is not installed!"
  exit 0
fi

# install rbenv
if whoami | grep 'root' ; then
  echo "root! run this script as a user"
  exit 0
else
  if ! rbenv --version >/dev/null 2>&1 ; then
    git clone https://github.com/rbenv/rbenv.git ~/.rbenv
    git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
    ~/.rbenv/bin/rbenv init
    # or apt-get install -y rbenv ruby-build
  fi
  if ! [ "$(grep 'rbenv/bin' ~/.bashrc)" ] ; then
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
  fi
  if ! [ "$(grep 'rbenv init' ~/.bashrc)" ] ; then
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
  fi
fi

# install ruby
if [ $(rbenv global) == 'system' ] ; then
  sudo apt-get update && sudo apt-get install -y libssl-dev libreadline-dev zlib1g-dev
  rbenv install $RUBYVER
  rbenv global $RUBYVER
  gem install bundler
else
  echo "ruby ${RUBYVER} installed"
fi
