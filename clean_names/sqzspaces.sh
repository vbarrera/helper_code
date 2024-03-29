#!/bin/sh
# this shell script removes the spaces out of the name of every file argument
# passed to it (handles an arbitrary number of files on the command line).
# example:
# sqzspaces.sh "/Users/Kurt/Name With Spaces"
# results in changing the filename to "/Users/Kurt/NameWithSpaces"
# Obtain from http://hints.macworld.com/article.php?story=20020611094717930
# Creator: klieb2002
# Modified to change spaces to underscores
  for OriginalFile
  do

    Location=`dirname "$OriginalFile"`
    FileName=`basename "$OriginalFile"`

    ShortName=`echo $FileName | sed 's/ /_/g'`

    if [ $ShortName != "$FileName" ]
    then
      cd "$Location"
      mv "$FileName" "$ShortName"
    fi

  done
