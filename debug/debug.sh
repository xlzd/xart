#!/bin/bash

for font in `cat font_options.txt`
do
	python ../xart/__init__.py -f $font
done
