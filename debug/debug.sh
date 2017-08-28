#!/bin/bash

for font in `cat font_options.txt`
do
	python ../xart/main.py -f $font
	echo "$font"
	echo "\n"
	echo "--------------------------------------"
done
