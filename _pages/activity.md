---
title: "Activity"
permalink: /activity/
layout: single
author_profile: true
---

{% assign acts = site.activity | sort: "date" | reverse %}
{% assign teaching = acts | where: "activity_type", "Teaching" %}
{% assign training = acts | where: "activity_type", "Training" %}
{% assign research = acts | where: "activity_type", "Research" %}

<a id="teaching"></a>
## Teaching
<ul>
{% for a in teaching %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
</ul>

<a id="training"></a>
## Training
<ul>
{% for a in training %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
</ul>

<a id="research"></a>
## Research groups & activities
<ul>
{% for a in research %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
</ul>
