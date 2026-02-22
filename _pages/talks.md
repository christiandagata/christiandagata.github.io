---
title: "Convegni e conferenze"
permalink: /talks/
layout: archive
author_profile: true
---

{% if site.talkmap_link == true %}
<p style="text-decoration:underline;"><a href="/talkmap.html">Vedi la mappa di tutti i luoghi in cui ho tenuto un intervento.</a></p>
{% endif %}

{% assign talks_all = site.talks | sort: "date" | reverse %}
{% for post in talks_all %}
  {% include archive-single-talk.html %}
{% endfor %}
