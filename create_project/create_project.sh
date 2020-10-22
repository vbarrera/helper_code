#!/bin/bash

# This script creates the structure and repo for a new project.

echo "Creating project for "$USER""

echo "##############"
echo "## Indicate ##"
echo -n "Technology (i.e: RNAseq) [ENTER] "
read technology
echo -n "PI last name (i.e: Smith) [ENTER] "
read pilastname
echo -n "Intervention (or extra info) [ENTER] "
read intervention
echo -n "Tissue (i.e: )[ENTER] "
read tissue
echo -n "Organism (i.e: human)[ENTER] "
read organism
echo -n "hbc code (i.e: 1234)[ENTER] "
read hbccode

project_name=hbc_${technology}_${pilastname}_${intervention}_${tissue}_${organism}_hbc${hbccode}
# Remove trailing and leading whitespaces 
project_name=`echo $project_name | sed 's/^[ \t]*//;s/[ \t]*$//'`

# Substitute whitespaces with underscores
project_name=`echo $project_name | sed 's/  */ /g' | sed 's/ /_/g'`

echo "Your project name is:"
echo "## ${project_name} ##" 
echo -n "Is this correct? [Y/N]"
read correct
if [ ${correct} == Y ]; then
  echo "Creating folder structure"
  for folder in data meta templates docs report
  do
  	mkdir -p ./${project_name}/${folder}
  done
else
  echo "Exiting"
  exit 1
fi

echo -n "Do you want to create a GitHub repository? [Y/N]"
read gh_repo
echo -n "Indicate github user or organization" [hbc/vbarrera]
read github_id
if [ ${gh_repo} == Y ]; then
   echo "Creating github repository: $github_id/${project_name}"
   pushd ${project_name}
   git init
   gh repo create $github_id/${project_name}
   popd
else
   exit 1 
fi
