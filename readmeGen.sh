#!/bin/bash

# Field ID's count from 1
#ID_COL=1
#NAME_COL=2
#DATE_COL=3

genTable()
{
	IFS=','
	sed '/^#/d' data.csv | while read -t 0.1 -r -a line
	do
		# Print table entries
		printf '%s | ' "${#line[0]}" #Print ID
		printf '%s | ' "${#line[1]}" #Print ID
		printf '%s | ' "${#line[2]}" #Print ID
		printf '%s | ' "${#line[3]}" #Print ID
		printf '\n'
	done
}

genTable
