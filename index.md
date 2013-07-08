---
layout: page
title: "Welcome!"
tagline: "Choose your poison (or honey if you prefer)"
icon: "home"
sitemap: true
---
{% include JB/setup %}


#### Coding:
<ul class="posts">
    {% for post in site.categories.coding %}
        {% include post.html %}
    {% endfor %}
</ul>

#### Rants:
<ul class="posts">
    {% for post in site.categories.rant %}
        {% include post.html %}
    {% endfor %}
</ul>


