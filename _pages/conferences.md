---
title: "Conferences"
permalink: /conferences/
layout: single
author_profile: true
---

{% assign confs = site.conferences | sort: "date" | reverse %}

<ul>
{% for c in confs %}
  <li>
    <a href="{{ c.url | relative_url }}">{{ c.title }}</a>
    {% if c.location %} — {{ c.location }}{% endif %}
    {% if c.date %} ({{ c.date | date: "%d/%m/%Y" }}){% endif %}
  </li>
{% endfor %}
</ul>
