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
<ul>
{% for p in pub_books %}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.title }}</a>
    {% if p.citation %}<br><small>{{ p.citation }}</small>{% endif %}
    {% if p.doi %}<br><small><img class="doi-badge" alt="DOI" src="https://img.shields.io/badge/DOI-{{ p.doi | uri_escape }}-blue"> <a href="https://doi.org/{{ p.doi }}" target="_blank" rel="noopener">doi.org</a></small>{% endif %}
  </li>
{% endfor %}
</ul>

## Articles, chapters, proceedings
<ul>
{% for p in pub_other %}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.title }}</a>
    {% if p.venue %} — <em>{{ p.venue }}</em>{% endif %}
    {% if p.date %} ({{ p.date | date: "%Y" }}){% endif %}
    {% if p.citation %}<br><small>{{ p.citation }}</small>{% endif %}
    {% if p.doi %}<br><small><img class="doi-badge" alt="DOI" src="https://img.shields.io/badge/DOI-{{ p.doi | uri_escape }}-blue"> <a href="https://doi.org/{{ p.doi }}" target="_blank" rel="noopener">doi.org</a></small>{% endif %}
  </li>
{% endfor %}
</ul>
