#!/bin/bash

i=0
while [ "$i" -lt 277 ]
do
	python __init__.py -f $i
	i=$(($i+1))	
done
