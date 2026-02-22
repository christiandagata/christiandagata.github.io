---
title: "Attività"
permalink: /activity/
layout: single
author_profile: true
---

{% assign acts = site.activity | sort: "date" | reverse %}
{% assign teaching = acts | where: "activity_type", "Teaching" %}
{% assign training = acts | where: "activity_type", "Training" %}
{% assign research = acts | where: "activity_type", "Research" %}

In questa pagina trovi gli elenchi delle attività principali, organizzate in tre aree:
`Insegnamenti`, `Formazione`, `Gruppi di ricerca e attività`.

Vai direttamente a:
- [Insegnamenti](#teaching)
- [Formazione](#training)
- [Gruppi di ricerca e attività](#research)

<a id="teaching"></a>
## Insegnamenti
<ul>
{% for a in teaching %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
{% if teaching == empty %}
  <li>Nessun insegnamento disponibile al momento.</li>
{% endif %}
</ul>

<a id="training"></a>
## Formazione
<ul>
{% for a in training %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
{% if training == empty %}
  <li>Nessuna attività di formazione disponibile al momento.</li>
{% endif %}
</ul>

<a id="research"></a>
## Gruppi di ricerca e attività
<ul>
{% for a in research %}
  <li><a href="{{ a.url | relative_url }}">{{ a.title }}</a>{% if a.period %} — {{ a.period }}{% endif %}</li>
{% endfor %}
{% if research == empty %}
  <li>Nessun gruppo o attività di ricerca disponibile al momento.</li>
{% endif %}
</ul>
