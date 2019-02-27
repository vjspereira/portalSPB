#!/bin/sh
#Run inside of repository clone
revlist=$(git rev-list HEAD)
(
    for rev in $revlist
    do
            files=$(git log -1 --pretty="format:" --name-only $rev)
            for file in $files
            do
                echo "$(git log -1 --pretty="%an" $rev);$file"
            done
            
    done
) > out.csv
