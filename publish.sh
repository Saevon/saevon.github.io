#!/bin/bash

URL='git@github.com:Saevon/saevon.github.io.git'
KEEP='assets'

branch=`git rev-parse --abbrev-ref HEAD`
uuid=`uuidgen`

cur=`pwd`
tmp_prefix="blog-pelican"
tmp="/tmp/$tmp_prefix-$uuid"
output="$cur/.site"


# Always use the source branch to publish
if [[ $branch != 'source' ]]; then
	exit 5;
fi

function cleanup {
	echo 'Cleaning Up'

	# Cleanup all tmp folders
	rm -rf /tmp/$tmp_prefix*
	rm -rf $cur/$output
}
trap cleanup SIGHUP SIGINT SIGTERM EXIT


# Create the static site
pelican -s publishconf.py -o $output
mkdir -p $tmp

cd $tmp
if [[ `pwd` != $tmp ]]; then
	echo 'ERROR: Not working in the correct directory'
fi

git init
git remote add -f origin $URL

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

# Get all the extra files files from the source branch
cp $cur/.publish-copy .
while read file; do
	cp $cur/content/$file .
	if [[ $? != 0 ]]; then
		echo "WARNING: File not found $file"
	fi
done < .publish-copy


# Move the newly generated files to the directory
cp -R $output/ $tmp
git add *

# Update master
git commit -a -m "Publishes new static content `date`"
git push -f origin master
