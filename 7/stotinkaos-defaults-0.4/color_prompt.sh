if [[ ! -z $BASH ]]; then
# If root, just print the user and host in red. Otherwise, print the current user
# and host in blue.
  if [[ $EUID -eq 0 ]]; then
    PS1="\[\033[33m\][\[\033[m\]\[\033[31m\]\u@\h\[\033[m\] \[\033[33m\]\W\[\033[m\]\[\033[33m\]]\[\033[m\]# "
  else
    PS1="\[\033[36m\][\[\033[m\]\[\033[34m\]\u@\h\[\033[m\] \[\033[32m\]\W\[\033[m\]\[\033[36m\]]\[\033[m\]$ "
  fi
fi
