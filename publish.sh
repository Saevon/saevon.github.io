#!/bin/bash -e

branch=`git rev-parse --abbrev-ref HEAD`
output='./.site'

# Always use the source branch to publish
if [[ $branch != 'source' ]]; then
	exit 5;
fi

# Create the static site
workon blog && pelican -s publishconf.py -o $output

# Get the latest version of master
git checkout master
if [[ $? != 0 ]]; then
	exit 1;
fi

# Remove all generated files
git rm -r -q !(assets)

# Get all the generated files from the source branch
git checkout source -- .publish-copy
while read file; do
	git checkout source -- $file
done < .publish-copy

# Move the newly generated files to the directory
cp -R $tmp/$output/ .
git add *

# Update master
git commit -a -m "Publishes new static content `date`"
git push -f origin master

# Clean up
git checkout $branch
rm -rf $tmp
