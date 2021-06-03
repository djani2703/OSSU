#!/usr/bin/env bash

# Define the path for the output files:
out_path=/tmp/out.tmp
err_path=/tmp/err.tmp

# Create output files:
> $out_path
> $err_path

# Create counter:
count=0

# Finding the zero value:
while [ true ]; do

    count=$(( count+1 ))
    rand_value=$(( RANDOM % 100 ))

    if [[ rand_value -eq 0 ]]; then
        echo "A zero value was detected.." >> $out_path
        (( 100 / $rand_value )) 2> $err_path
        break
    fi

    echo "$count: $rand_value" >> $out_path
done

echo "The program ran $count iterations before stopping.."