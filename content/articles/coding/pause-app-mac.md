Template: article
Title: Quickly pausing an app in Mac-OS
Tagline: pause and resume apps with multiple processes
Date: 2015-08-14
Category: coding
Tags: Mac OSX, bash


Chrome has always annoyed me when my battery is low, or when I'm low on memory. So I made a quick terminal command that freezes its processes. Of course I use this for pausing any of my apps.

# Overview

!alert! info
    You can see the code in my config file repository, along with my other bash aliases.
    [Click here to see the entire pause script](bash-pauser)
!endalert!

I added the following bash functions

`pause_process(pid)`: nicer kill command that pauses a process (`kill -STOP`)

`pause_app(string)`: searches for any proccesses with the given string, pausing them all

As well as the opposing functions `resume_app()` and `resume_process()` (which use `kill -CONT`).



## Implementation

!alert! thoughts
    I'm not too great at bash, so if there's a better way to do this, do comment!
    Thanks!
!endalert!

First thing I needed was a nice way to work with lists in bash, so I made a function to map a command on each item.
Using that I made a function that searches for processes that contain a given string. Then it maps a command on them

```bash
function map() {
    for pid in `eval $1`; do
        $2 ${pid};
    done
}

PGREP_FLAGS="-U ${USER}"

function search_map() {
    map "pgrep ${PGREP_FLAGS} -f \"$1\"" $2
}
```

Using this the `pause_app()` command is quite simple, and the resume_app one as well.

```bash
function pause_app() {
    echo pausing $1
    search_map "$1" pause_process;
}
```

## Usage

Using this just requires knowing part of the app name:

```bash
$ pause_app Chrome.app
pausing Chrome.app
  pausing:  378
  pausing:  406
  pausing:  414
$ resume_app Chrome.app
resuming Chrome.app
  resuming:  378
  resuming:  406
  resuming:  414
```

!alert! warning
    `pgrep` will find more that one app if they contain the same text in the process tag.
    The best search string is one which contains the entire app name, (or at least the `.app` prefix)
!endalert!


## More Uses

I've also made a bash script that freezes all the processes I consider extraneous to give my computer some resources during clinch moments. `pause_all` reads a list of app names, mapping the pause script on them all. `resume_all` does the opposite. You can see it [here][bash-pauser-all]





# Reference

* [The entire pause Script][bash-pauser]
* [Pausing a list of apps at once][bash-pauser-all]

[bash-pauser]: https://github.com/Saevon/config/blob/master/cbash/pauser.sh
[bash-pauser-all]: https://github.com/Saevon/config/blob/master/cbash/pauser_template.sh

