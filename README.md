# Saevon's Blog

---

This is the `source` repo, all code is generated from here

---

The `master` and `source` branches are different repositories.

`master` contains the resulting static html
`source` contains the templates used to generate master

## Usage

#### Pubishing

Luckily there's a script for that

```bash
./publish.sh
```

In detail, what actually happens is the following.

To publish the site, one needs to generate the source, copy over the files in `.publish-copy`, then make a new commit on master. Remember old pages might need to be removed/updated, and new ones might need to be added. Also remember that the assets folder is currently not generated at all, but used to server usefull data.

## TODO

The following is my todo list for this site, feel free to ignore this, unless you're trying to get inspiration from this site, in which case, pay attention to what you might need to fix up.

* [ ] Menu bar is empty
* [ ] 404 page needs to auto search based on the url (and maybe email me?)
* [ ] Page search
* [ ] I don't want any individual pages for each tag, need to remove them
* [ ] Pagination is plain right now
* [ ] No Feeds are enabled (working) at all right now
* [ ] No Favicon
* [ ] Publish script needs to checkout the full repository including the assets folder


## License

[MIT](http://opensource.org/licenses/MIT)
