Template: article
Title: Python Virtual Environments and PIP
Tagline: Keep your projects separate.
Date: 2013-07-12
Category: coding
Tags: python, virtualenv, pip


virtualenv is a pretty awesome tool for any python user, however it is often too easy to accidentally install new packages into the wrong place. Here I show you how to separate your system packages and that of your project environments.



# Intro

Jump "straight" to the [Syspip](#Syspip) section if you know all about python packaging and virtualenv.



# virtualenvwrapper

This is a really useful tool, even if it adds binaries with amazingly long names. It lets you easily and quickly list, add, and switch to a virtualenv.

I don't usually need all the many options this script provides, and would also prefer for it to be easier to combine the virtualenvwrapper's and git's PS1 prompt changes.


### Changing Environments

To change environments is pretty easy, you just use the `workon` command. This works whether you have a currently active environment or not.

	:::bash
	workon $env_name

To deactivate the current environment you use the `deactivate` command, just like normal. Though personally I though workoff was more obvious.

	:::bash
	alias workoff=deactivate



### Tab Completion!

When using the `workon` command you can tab complete to see the list of all the environments you have.


### Add/Remove Environments

```bash
# Add a new environment
mkvirtualenv $env_name
```

```bash
# Remove an environment
rmvirtualenv $env_name
```



# Syspip

Heres where stuff gets interesting. To prevent mistakes while installing packages, I've added the following things to my bash startup scripts (`.bashrc`, `.bash_aliases`, etc.)

	:::bash
	# .bashrc

	source /usr/local/bin/virtualenvwrapper.sh

	export WORKON_HOME=$HOME/.environments
	export PIP_VIRTUALENV_BASE=WORKON_HOME

	export PIP_REQUIRE_VIRTUALENV=true

First notice that we set `PIP_REQUIRE_VIRTUALENV`, this ensures that pip *will not* run without an active virtual environment.

Second, do remember to set `PIP_VIRTUALENV_BASE`, since that is what pip uses to tell if you have an environment active. (AFAIK)

	:::bash
	# .bash_aliases

	export SYSTEM_PIP=`which pip`
	function syspip {
	    PIP_REQUIRE_VIRTUALENV="" sudo $SYSTEM_PIP "$@"
	}

Here we first find which version of pip we use, then add a new way of using the global pip binary. Now you have 2 ways of installing a package, each of which always installs to the expected location.

* To install **only** for the currently active environment, (or fail if it doesn't find one)

		:::bash
		pip install $package

* To install **only** globally

		:::bash
		syspip install $package

!alert!  warning
	Don't forget to load `.bash_aliases` before you activate any environments, otherwise `syspip` might not work as advertised.
!endalert!


