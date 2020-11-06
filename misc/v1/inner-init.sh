#!/bin/sh

set -e

SCRIPT_PATH=$(readlink -f $0)

GOROOT=`dirname $SCRIPT_PATH`
GOPATH=$HOME/go

if [ ! -d $GOPATH ]; then
  mkdir -p $GOPATH
fi

/home/action/.sysinner/inagent confrender --in ${GOROOT}/misc/profile.d_golang.sh --out /home/action/local/profile.d/golang.sh --var__inpack_prefix_golang ${GOROOT}
source /home/action/local/profile.d/golang.sh

