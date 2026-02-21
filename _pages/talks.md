---
title: "Talks"
permalink: /talks/
layout: archive
author_profile: true
---

{% if site.talkmap_link == true %}
<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>
{% endif %}

{% assign talks_all = site.talks | sort: "date" | reverse %}
{% for post in talks_all %}
  {% include archive-single-talk.html %}
{% endfor %}
