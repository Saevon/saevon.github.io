#!/bin/bash -e

branch=`git rev-parse --abbrev-ref HEAD`
uuid=`uuidgen`

tmp="/tmp/jekyll-$uuid"


# Always use the source branch to publish
jekyll build
mkdir $tmp
mv .site $tmp

# Get the latest version of master
git checkout master

# Remove all generated files
git rm -r -q .

# Get all the generated files from the source branch
git checkout source -- .publish-copy
while read file; do
	git checkout source -- $file
done < .publish-copy

# Move the newly generated files to the directory
cp -R $tmp/.site/ .
git add *

# Update master
git commit -a -m "Publishes for `date`"
git push -f origin master

# Clean up
git checkout $branch
rm -rf $tmp
