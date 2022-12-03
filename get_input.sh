#!/bin/sh

date=${1:-$( date +%-d )}
year=${2:-$( date +%-Y )}

day_folder="$year/day_$date"

if [ ! -d "$day_folder" ]
then
    mkdir -p "$day_folder"
    echo "Directory for day $date created!"
else
    echo "Directory for day $date already exists."
fi

for i in 1 2
do
    task_file="$day_folder"/task_$i.py
    if [ ! -e "$task_file" ]
    then
        cat <<EOT >> "$task_file"
from utils.read_input import read_input

if __name__ == "__main__":
    _ = read_input("$day_folder/input.txt")
EOT
        echo "File task_$i.py created!"
    else
        echo "File task_$i.py already exists."
    fi
done

response=$(curl -s -S -f -o "$day_folder"/input.txt -H "cookie: session=${AOC_SESSION_COOKIE}" -w "%{http_code}\n" "https://adventofcode.com/$year/day/$date/input")
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
