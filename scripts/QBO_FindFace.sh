#!/bin/bash

#busca un proceso especifico
DATO=`ps -aux | grep -v grep | grep FindFace.py`
if [ -z "$DATO" ]; then
    	EXISTE=false
else
	EXISTE=true
fi

START="start"
STOP="stop"

# echo "EXISTE: " $EXISTE
# start FindFace.py
if [[ $1 = $START ]]; then
	if $EXISTE = true;
	then
		echo "FindFace.py is already running"
	else
		echo "launching FindFace.py"
		/opt/qbo/FindFace.py > /dev/null &
	fi
fi

# stop FindFace.py
if [[ $1 = $STOP ]];
then
	if $EXISTE = true;
	then
		kill -9 `ps -ef |grep -v grep |grep FindFace.py| awk '{print $2}'`
		echo "FindFace.py stoped"
	else
		echo "FindFace.py was not running"
	fi
fi
