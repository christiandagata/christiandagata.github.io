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
{% if teaching == empty %}
- Nessun insegnamento disponibile al momento.
{% else %}
{% for a in teaching %}
### {{ a.title }}{% if a.period %} — {{ a.period }}{% endif %}
{{ a.content }}

[Apri la scheda completa]({{ a.url | relative_url }})
{% endfor %}
{% endif %}

<a id="training"></a>
## Formazione
{% if training == empty %}
- Nessuna attività di formazione disponibile al momento.
{% else %}
{% for a in training %}
### {{ a.title }}{% if a.period %} — {{ a.period }}{% endif %}
{{ a.content }}

[Apri la scheda completa]({{ a.url | relative_url }})
{% endfor %}
{% endif %}

<a id="research"></a>
## Gruppi di ricerca e attività
{% if research == empty %}
- Nessun gruppo o attività di ricerca disponibile al momento.
{% else %}
{% for a in research %}
### {{ a.title }}{% if a.period %} — {{ a.period }}{% endif %}
{{ a.content }}

[Apri la scheda completa]({{ a.url | relative_url }})
{% endfor %}
{% endif %}
