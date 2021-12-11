#!/bin/sh

if [ $# -eq 0 ] 
then
    date=$( date +%-d )
else
    date=$1
fi

day_folder="day_$date"

if [ ! -d "$day_folder" ]
then
    mkdir "$day_folder"
    echo "Directory for day $date created!"
else
    echo "Directory for day $date already exists."
fi

for i in 1 2
do
    if [ ! -e "$day_folder"/task_$i.py ]
    then
        touch "$day_folder"/task_$i.py
        echo "File task_$i.py created!"
    else
        echo "File task_$i.py already exists."
    fi
done

response=$(curl -s -S -f -o "$day_folder"/input.txt -H "cookie: session=${AOC_SESSION_COOKIE}" -w "%{http_code}\n" "https://adventofcode.com/2021/day/$date/input")
if [ ! "$response" -eq 200 ]
then
    if [ -e "$day_folder"/input.txt ] 
    then
        rm "$day_folder"/input.txt
    fi
    echo "Wasn't able to fetch the input, make sure you've added your session cookie to AOC_SESSION_COOKIE and that it's still valid."
else
    echo "Input fetched!"
fi
