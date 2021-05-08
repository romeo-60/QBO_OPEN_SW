#!/bin/bash

#busca un proceso especifico
DATO=`ps -aux | grep -v grep | grep PiCmd.py`
if [ -z "$DATO" ]; then
    	EXISTE=false
else
	EXISTE=true
fi

START="start"
STOP="stop"

# echo "EXISTE: " $EXISTE
# start PiCmd
if [[ $1 = $START ]]; then
	if $EXISTE = true;
	then
		echo "PiCmd is already running"
	else
		echo "launching PiCmd"
		/opt/qbo/PiCmd.py > /dev/null &
	fi
fi

# stop PiCmd
if [[ $1 = $STOP ]];
then
	if $EXISTE = true;
	then
		kill -9 `ps -ef |grep -v grep |grep PiCmd.py| awk '{print $2}'`
		echo "PiCmd stoped"
	else
		echo "PiCmd was not running"
	fi
fi
