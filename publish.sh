#!/bin/bash

# Asks the user a y/n question
function ask_yn {
	echo -n "Continue? [y/n]: "
	read item
	case "$item" in
		y) $1; break;;
		n) $2; break;;
		*) $2; break;;
	esac
}

# Asks the user if they wish to continue or exit
function ask_continue {
	ask_yn "true" "exit 1"
}

# Print a fancy warning message
function warn {
	echo -e '\x1b[0;33mWARN:' $@ '\x1b[0;0m' 1>&2
}

function section {
	echo -e '\n\x1b[38;5;33m' $@ '\x1b[0;0m' 1>&2
}


function err {
	echo -e '\x1b[0;91mERROR:' $@ '\x1b[0;0m' 1>&2
}

# Warn the user, then ask them if they want to continue
function ask_warn {
	warn $@
	ask_continue
}


#
# The actual script starts here
#
URL='git@github.com:Saevon/saevon.github.io.git'
KEEP='assets'

branch=`git rev-parse --abbrev-ref HEAD`
uuid=`uuidgen`

tmp_prefix="blog-pelican"
tmp="/tmp/$tmp_prefix-$uuid"
output="/tmp/$tmp_prefix-$uuid-site"


function cleanup {
	local status=$?

	section "Cleanup..."

	# Cleanup all tmp folders
	rm -rf /tmp/$tmp_prefix*

	if [ $status == 0 ]; then
		exit 0
	fi

	exit 1
}
trap cleanup SIGHUP SIGINT SIGTERM EXIT



# Warn the user if there are un-pushed changes
unpushed=`git log @{upstream}..`
if [[ -n $unpushed ]]; then
	ask_warn "You have unpushed changes"
fi


# make the temporary folder
mkdir -p $tmp
cd $tmp
if [[ `pwd` != $tmp ]]; then
	err 'Not working in the correct directory'
fi


# Set-up the git repo
section "Setup..."
git init
git remote add -f origin $URL


# Create the static site
section "Generating..."
git checkout source
if [[ $? != 0 ]]; then
	err "Can't checkout master"
	exit 1;
fi
pelican -s publishconf.py -o $output

# Cleanup all the .pyc files
find . -name '*.pyc' | xargs rm


# Get all the extra files files from the source branch
while read file; do
	cp ./content/$file $output/
	if [[ $? != 0 ]]; then
		warn "File not found $file"
	fi
done < .publish-copy


# Get the latest version of master
section "Updating..."
git checkout master
if [[ $? != 0 ]]; then
	err "Can't checkout master"
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
section "Pushing..."
git commit -a -m "Publishes new static content `date`"
git push -f origin master

# Make sure the cleanup script sees we finished without errors
exit 0
