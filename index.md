---
layout: page
title: "Welcome!"
tagline: "Choose your poison."
icon: "home"
sitemap: true
---
{% include JB/setup %}


### Coding:
<ul class="posts">
    {% for post in site.categories.coding limit:2 %}
        {% include post_excerpt.html %}
    {% endfor %}
</ul>

### Media:
<ul class="posts">
    {% for post in site.categories.media | limit:2 %}
        {% include post_excerpt.html %}
    {% endfor %}
</ul>

### Roleplaying:
<ul class="posts">
    {% for post in site.categories.roleplaying | limit:2 %}
        {% include post_excerpt.html %}
    {% endfor %}
</ul>


### Misc:
<ul class="posts">
    {% for post in site.categories.misc | limit:2 %}
        {% include post_excerpt.html %}
    {% endfor %}
</ul>



