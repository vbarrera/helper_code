#!/usr/local/bin/bash
for file in ./* ; do
    mv "$file" "$(echo $file|sed -e 's/\([A-Z]\)/\L\1/g' -e 's/ /_/g')"
done
