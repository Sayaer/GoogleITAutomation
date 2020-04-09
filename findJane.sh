#!/bin/bash

if test -e ~/scripts/oldFiles.txt; then echo "oldFiles exists no need to create"; else > ~/scripts/oldFiles.txt; fi
FILE=($(grep " jane " ~/data/list.txt | cut -d ' ' -f 3))
for file in "${FILE[@]}"
  do
    echo $file
    if test -e ~/$file;
      then echo ~/$file >> ~/scripts/oldFiles.txt
    fi
  done
