---
layout: page
title: "Shortkey.js"
description: "A Shortkey input type"
---
{% include JB/setup %}

This is a module that allows for a new `shortcut` input type in HTML `<input>`. It also provides a global parser that reads your input an helps you check if the shortcut has occured during a `keypress`, `keydown` or `keyup` event.

You can get this module in three different parts,

 * [shortkey-global.min.js][parser-only] for just the global parser.
 * [shortkey.min.js][minified] for the full module.

See the source on Github [here][source]


# Global Usage

### shortkey.parse(string[, options])

Tries to parse the given input returning a `shortcut` object. If it can't parse the input then it will

Here is an example usage of the global shortcut parser

{% highlight javascript %}
// Note: the seperator is optional, as shortkey can guess at a few of the more common formats
// What it will do though is set the text field for the output using the given seperator
// var shortcut = shortkey.parse('Shift+A');
var shortcut = shortkey.parse('Shift+A', {seperator: '+'});

element.onkeydown = function(event) {
	if (!shortcut.valid_keydown(event)) {
		return;
	}

	// The user typed the shortcut
	// YOUR CODE GOES HERE
};

{% endhighlight %}

### Creating shortcut groups

You can group together a bunch of shortcuts adding an event listener that will check for all of them.

{% highlight javascript %}
// Create the group you will be working with from now on
var shortcuts = new shortkey.Group();

// Register a new shortcut
shortcuts.register(shortcut, callback);

// Register a named shortcut (so you can update/remove it later)
shortcuts.register(shortcut, 'name', callback);

// Listen to the following elements
shortcuts.onkeydown(elements);
shortcuts.onkeyup(other_elements);

// Update the named shortcut, changing the shortcut keys
shortcuts.update(shortcut, 'name');
// Update it changing both the shortcut and the callback
// (This will create it if it doesn't exist)
shortcuts.update(shortcut, 'name', callback);

// Remove the named shortcut
shortcuts.unregister('name')
// Remove a known shortcut
shortcuts.unregister(shortcut);

shortcuts

{% endhighlight %}

### shortkey.Group

Creates a new shortcut group

#### new shortkey.Group()

#### new shortkey.Group(shortcuts);

This also registers every shortcut in the given list. Each shortcut need to have the following properties:

`shortcut`: The actual shortcut object
`callback`: The callback
`name`: (optional) to register a named shortcut

### .register

Adds a new shortcut for the group to respond to. The given callback needs to implement the following interface:

{% highlight javascript %}
shortcuts.register(shortcut, function(event) {
	// Do Stuff
};
{% endhighlight %}

#### .register(shortcut, callback)

This registers an unnamed shortcut

#### .register(shortcut, 'name', callback)

This registers a named shortcut, which you you can later update


### .unregister

Stops the group from listening to the given shortcut

#### .unregister(shortcut)

#### .unregister('name')

Removes the named shortcut instead


### .update

Updates the shortcut to listen to a different set of keys. You can only update named shortcuts.

#### .update(shortcut, 'name')

#### .update(shortcut, 'name', callback)

Removes any old shortcuts with the given name, creating a new one with the given shortcut and callback.


### .onkeyup(element[s])

Adds the onkeyup listener to the given element[s] (Node or list of Nodes)

### .onkeydown(element[s])

Adds the onkeydown listener to the given element[s] (Node or list of Nodes)



<br />



# Data

The shortcut input type deals with a `shortcut` object.

## The shortcut object

This is the return value of the input field.

Note that the `text` field is what will be visible on the input tag's value field.

Note that this does not record the order you press the keys thus `Shift+Cmd+A` is the same as `Cmd+Shift+A` and will end up being normalized to the same textual representation.

{% highlight javascript %}
shortcut = {
	'text': 'Alt-A',
	'modifiers': {
		'shift': false,
		'ctrl': false,
		'cmd': false,
		'alt': true
	},
	'key': 'a',

	'valid_keydown': function(event) { ... },
	'valid_keyup': function(event) { ... }
};
{% endhighlight %}

### text `string`

A textual representation of the shortcut.

### modifiers

A mapping of the following modifiers to whether this shortcut has them pressed down or not.

 * `shift`
 * `alt`
 * `control`
 * `cmd`

### key `string`

The key that needs to be pressed to finish the shortcut


### Events

The three events test whether the given event (of their namesake) should trigger the shortcut. Thus you can use them in your own event listeners.

Remember that since the three event have differing specs and browser compatibilities that you should only use one of these handlers for the event of its namesake.

{% highlight javascript %}
element.onkeydown = function(event) {
	if (!my_shortcut.valid_keydown(event)) {
		return;
	}

	// Your code goes here
}
{% endhighlight %}


<br />



# API

<hr />

### .reset()

Resets the shortcut to the given `default` value, or removes the shortcut entirely if `null` is the default.

<hr />

### .disable()

Disables the input field

<hr />

### .enable()

Enables the input field

<hr />

### .data()

Returns the current `shortcut`

### .data(shortcut)

Changes the currently set `shortcut` to the given value

Note: this will trigger the `change` event

### .data(string)

Parses the given string, changing the `shortcut` to the given value if possible. `ParseError` will be raised if the text can't be parsed.

Note: this will trigger the `change` event

<hr />

### .text()

Returns the text representation of the current `shortcut`

<hr />


<br />



# Customization

### disabled `boolean`

default: `false`

This works like any other input type, showing the field's value, but not allowing the user to change it. If you've set this using javascript, then note that the html will have the `disabled` attribute set on it, thus you can apply css styles.

### lock_modifiers `boolean`

default: `false`

This makes the user unable to change the modifier keys, only prompting the user for a character

### default `shortcut`

default: `null`

The default shortcut for the input to show, this is different from the current value of the input in that it supplies a `reset` functionality

A value of `null` means no shortcut

### can_reset `boolean`

default: `true`

Toggles whether the input tag shows a reset button

### seperator `string`

default: `'-'`

Changes the seperator in the text formatted version of the shortcut



## Events

All events get passed the `shortcut` object as their first argument.


You can specify any event either by name using javascript.

{% highlight javascript %}
	// TODO!!!
{% endhighlight %}


You can also use an html attribute in the `onevent` format.

{% highlight html %}
<input type="shortcut" onactivate="console.log('This is being changed')" />
{% endhighlight %}


### activate

Gets triggered when the user starts changing the shortcut

### progress

Gets triggered when the user changes the keys that are currently held down.

### change

Gets triggered when the user's shortcut changes. This occurs when the user clicks on the first non-modifier key.


<br />



## Reference

* [Github Source][source]

[source]: https://github.com/Saevon/shortkey
[minified]: https://saevon.ca/??
[parser-only]: https://saevon.ca/?2


