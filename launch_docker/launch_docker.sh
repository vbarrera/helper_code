#!/bin/bash

# This script launches a docker container for a project using a provided image

echo "Creating container"

echo "##############"
echo "## Indicate ##"
read -p "Container Name [ENTER] " container_name
read -p  "Docker image  [ENTER] " docker_image
read -p "Host Port [8787] " port
port=${port:-8787}

# Confirm values are correct

echo "Container Name: ${container_name}"
echo "Docker image: ${docker_image}"

echo -n "Is this correct? [Y/N]"
read correct
if [ ${correct} == Y ]; then
  echo "Creating container"
	docker run -d -p ${port}:8787 --name ${container_name} \
	-e USER='rstudio' -e PASSWORD='docker_container'  \
	-e DISABLE_AUTH=true -e ROOT=TRUE \
	-v $DOCKER_VOLUME_DEF_LOCATION:/home/rstudio/projects \
	${docker_image}
else
  echo "Exiting"
  exit 1
fi
