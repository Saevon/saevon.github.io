# Saevon's Blog

---

This is the `source` repo, all code is generated from here

---

The `master` and `source` branches are different repositories.

`master` contains the resulting static html
`source` contains the templates used to generate master

## Usage

### Publishing

Luckily there's a script for that

```bash
./publish.sh
```

In detail, what actually happens is the following.

To publish the site, one needs to generate the source, copy over the files in `.publish-copy`, then make a new commit on master. Remember old pages might need to be removed/updated, and new ones might need to be added. Also remember that the assets folder is currently not generated at all, but used to server usefull data.

## Development

I use the my alerts plugins, and if you want to develop the alerts plugin at the same time as the blog, you need to run

```bash
python setup.py develop
```

### Article Customization

The following define the basic article info
<br />`Title`
<br />`Tagline`
<br />`Date`
<br />`Category`
<br />`Tags`

Optional Tags:
<br />`status`:   Status of the article: `draft` (not published), `hidden` (not listed), `published`
<br />`slug`:     what
<br />`Template`: The html style to use should be `article`
<br />`Style`:    The css style to use: `simple`, `default`

Flags:
<br />`IsNumbered`:  Makes headers show numbers
<br />`NoSidenav`:   Hides the sidebar
<br />`NoFooter`:    Hides the footer
<br />`NoTags`:      Hides the tags section
<br />`NoComments`:  Hides the comments section
<br />`NoPermalink`: Makes the header not be a link to itself



### Markdown


#### Plugins

##### Definition Lists

```
Apple
: Red fruit

Orange
: Orange Fruit
```

##### Abbreviations

```
This code contains HTML sometimes.

*[HTML]: Hyper Text Markup Language
```

##### Attribute Lists

Adds html tags to things

```
{: #someid .someclass somekey='some value' }
```

##### Code Blocks

```
    ```python hl_lines="2 4"
    #
    # Important Comment

    print "hello world"
    ```
```

##### Footnotes

```
This is important[^1], this isn't[^other]

[^1]: Define the footnote
[^other]:
    Long definition

    That spans multiple lines
```

##### AutoFootnotes

<br />`TODO`: This needs to be finished

##### Table of Contents

```
[TOC]
```

##### mdx_del_ins

Adds diffs (del, ins tags)

```
++added++ ~~removed~~
```

<ins>added</ins> <del>removed</removed>


##### Alerts

Adds bootstrap alerts

```
!alert! info
    Some optionally indented markdown that also gets processed
!endalert!
```

##### Header Outline

Forces headers to be wrapped in section tags for formatting



## TODO

The following is my todo list for this site, feel free to ignore this, unless you're trying to get inspiration from this site, in which case, pay attention to what you might need to fix up.

* [ ] 404 page needs to auto search based on the url (and maybe email me?)
* [ ] Need to comment up css better
* [ ] Page search
* [ ] Pagination is plain right now
* [ ] No Feeds are enabled (working) at all right now
* [ ] Go back to X button should head to the previous url
* [ ] No Favicon
* [ ] Publish script needs to checkout the full repository including the assets folder, which is annoying
* [ ] Merge markdown Alerts and admonitions?
* [ ] Header Permalinks need to be enabled


## License

[MIT](http://opensource.org/licenses/MIT)
