#!/bin/bash

URL='git@github.com:Saevon/saevon.github.io.git'
KEEP='assets'

branch=`git rev-parse --abbrev-ref HEAD`
uuid=`uuidgen`

tmp_prefix="blog-pelican"
tmp="/tmp/$tmp_prefix-$uuid"
output="/tmp/$tmp_prefix-$uuid-site"


function cleanup {
	echo 'Cleaning Up'

	# Cleanup all tmp folders
	rm -rf /tmp/$tmp_prefix*
	rm -rf $output
}
trap cleanup SIGHUP SIGINT SIGTERM EXIT


# make the temporary folder
mkdir -p $tmp
cd $tmp
if [[ `pwd` != $tmp ]]; then
	echo 'ERROR: Not working in the correct directory'
fi


# Set-up the git repo
git init
git remote add -f origin $URL


# Create the static site
git checkout source
if [[ $? != 0 ]]; then
	echo "ERROR: Can't checkout master"
	exit 1;
fi
pelican -s publishconf.py -o $output


# Get all the extra files files from the source branch
while read file; do
	cp ./content/$file $output/
	if [[ $? != 0 ]]; then
		echo "WARNING: File not found $file"
	fi
done < .publish-copy


# Get the latest version of master
git checkout master
if [[ $? != 0 ]]; then
	echo "ERROR: Can't checkout master"
	exit 1;
fi

# Remove all generated files
find . -maxdepth 1 \! \( -name ".*" -or -name $KEEP \) | xargs git rm -r

# Copy over the output content
cp -R $output/ $tmp


# Move the newly generated files to the directory
cp -R $output/ $tmp

git add *

# Update master
git commit -a -m "Publishes new static content `date`"
git push -f origin master
