---
title: "Publications"
permalink: /publications/
layout: single
author_profile: true
---

{% assign pub_all = site.publications | sort: "date" | reverse %}
{% assign pub_books = pub_all | where: "pub_type", "book" %}
{% assign pub_other = pub_all | where_exp: "p", "p.pub_type != 'book'" %}

## Books
{% for p in pub_books %}
- [{{ p.title }}]({{ p.url | relative_url }})
  {% if p.citation %}{{ p.citation }}{% endif %}
  {% if p.doi %}[DOI](https://doi.org/{{ p.doi }}){% endif %}
{% endfor %}

## Articles, chapters, proceedings
{% for p in pub_other %}
- [{{ p.title }}]({{ p.url | relative_url }})
  {% if p.venue %} — {{ p.venue }}{% endif %}{% if p.date %} ({{ p.date | date: "%Y" }}){% endif %}
  {% if p.citation %}{{ p.citation }}{% endif %}
  {% if p.doi %}[DOI](https://doi.org/{{ p.doi }}){% endif %}
{% endfor %}