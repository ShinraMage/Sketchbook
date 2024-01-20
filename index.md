---
layout: page
---


{%- for post in site.posts limit: 15 -%}
    <br>
    <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
    <a class="post-link" href="{{ post.url | relative_url }}">
    {{ post.title | escape }}
    </a>
    {{ post.content }}
{%- endfor -%}

[older posts](./all)