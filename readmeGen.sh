#!/bin/bash

# Field ID's count from 1
#ID_COL=1
#NAME_COL=2
#DATE_COL=3

genTable()
{
	x=0
	IFS=','
	sed '/^#/d' data.csv | while read -t 0.1 -r -a line
	do
		# Print table entries
		if [ $x -ne 0 ]; then
			printf '#%s | ' "${line[0]}" #Print ID
		else
			printf '%s | ' "${line[0]}" #Print ID
		fi
		printf '%s | ' "${line[1]}" #Print Product Name
		printf '%s | ' "${line[2]}" #Test Date
		printf '%s | ' "${line[3]}" #CPU Test 1 Single
		printf '%s | ' "${line[4]}" #Cpu Test 1 Multi
		printf '%s | ' "${line[5]}" #Cpu Test 2
		printf '%s | ' "${line[6]}" #Gpu Test 1
		printf '%s | ' "${line[7]}" #Gpu Test 2
		printf '%s | ' "${line[8]}" #Memory Test 1
		printf '%s | ' "${line[9]}" #Memory Test 2
		printf '%s | ' "${line[10]}" #Network Upload Test 1
		printf '%s | ' "${line[11]}" #Network Upload Test 2
		printf '%s | ' "${line[12]}" #Network Down Test 1
		printf '%s | ' "${line[13]}" #Network Down Test 2
		printf '%s | ' "${line[14]}" #Network Bidiretional Test 1
		printf '%s | ' "${line[15]}" #Network Bidiretional Test 2
		printf '\n'

		if [  $x -ne 1 ]
		then
			y=0
			printf '%s' '|'
			while [ $y -le 15 ]
			do
				printf '%s' '----|'
				y=$((y+1))
			done
			printf '\n'
		fi
		x=1
	done
}

genTable
