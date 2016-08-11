MD_EXTENSIONS = (
    # Enables the metadata at the top of the markdown files
    'meta',

    # Disable mixing of list types
    # 'sane_lists',

    # Enables smart char conversion (ellipses, m-dash, n-dash, double-angle-quotes)
    # The option disables the wierd fancy quotes replacement
    'smarty(smart_quotes=False)',

    # Adds syntax highlighting
    'codehilite(css_class=highlight)',

    #
    'extra',

    # Adds a table of contents
    # TODO: make the permalink the proper symbol
    'toc(permalink=False)',

    #################################
    # Non standard extensions

    # Adds bootstrap style alerts
    'alerts',

    # Adds my defn tables
    'defn_table',

    # Allows you to have strikeout and insertions (del/ins tags)
    # TODO: broken
    'del_ins',

    # Forces headers to also wrap the resulting HTML in a <section> tag
    'outline(wrapper_cls="section section%(LEVEL)d")',
)
