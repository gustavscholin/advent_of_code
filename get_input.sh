#!/bin/bash

# Function to print usage/help message
usage()
{
    echo
    echo "Helper-script to create files and get input for an AoC-day"
    echo
    echo "Usage: $0 [day <1-25>] [year]"
    echo "No arguments runs for current day of month and year"
    echo
    echo "Options:"
    echo "-h   : print this help"
    echo
}

# Parse options
while getopts "h" option; do
   case $option in
      h) usage; exit;;
      ?) usage; exit 1;;
   esac
done

# Get and validate day
day=${1:-$( date +%-d )}
if ! [[ $day =~ ^[0-9]+$ ]] || [ "$day" -lt 1 ] || [ "$day" -gt 25 ]; then
    echo "Error: The day input ($day) is not a valid day (1-25)."
    exit 1
fi

# Get and validate year
year=${2:-$( date +%-Y )}
current_year=$(date +%-Y)
if ! [[ $year =~ ^[0-9]+$ ]] || [ "$year" -lt 2015 ] || [ "$year" -gt "$current_year" ]; then
    echo "Error: The year input ($year) is not a valid year (2015-current year)."
    exit 1
fi

day_folder="$year/day_$day"

if [ ! -d "$day_folder" ]
then
    mkdir -p "$day_folder"
    echo "Directory for day $day created!"
else
    echo "Directory for day $day already exists."
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

response=$(curl -s -S -f -o "$day_folder"/input.txt -H "cookie: session=${AOC_SESSION_COOKIE}" -w "%{http_code}\n" "https://adventofcode.com/$year/day/$day/input")
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
