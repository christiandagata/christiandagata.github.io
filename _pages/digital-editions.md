---
title: "Edizioni digitali"
permalink: /digital-editions/
layout: single
collection: digital_editions
entries_layout: list
author_profile: true
---
<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign items = site.digital_editions | default: empty | sort: "date" | reverse %}

<div class="mag-wrap">

  <section class="mag-section" style="margin-top:0;">
    <h2>Edizioni digitali</h2>

    {% if items == empty %}
      <p>Al momento non ci sono edizioni digitali pubblicate.</p>
    {% else %}
      <div class="mag-grid">
        {% for e in items %}
          <div class="mag-card">
            <p class="mag-kicker">Edizione digitale</p>

            <h3 class="mag-title">
              <a href="{{ e.url | relative_url }}">{{ e.title }}</a>
            </h3>

            <div class="mag-meta">
              {% if e.date %}{{ e.date | date: "%Y" }}{% endif %}
              {% if e.tech %}{% if e.date %} · {% endif %}{{ e.tech }}{% endif %}
            </div>

            {% if e.excerpt %}
              <div class="mag-excerpt">{{ e.excerpt | strip_html | truncate: 170 }}</div>
            {% endif %}

            <div class="mag-actions" style="margin-top:.7rem;">
              <a class="mag-btn secondary" href="{{ e.url | relative_url }}">Scheda</a>
              {% if e.link %}
                <a class="mag-btn" href="{{ e.link }}" target="_blank" rel="noopener">Apri progetto</a>
              {% endif %}
            </div>
          </div>
        {% endfor %}
      </div>
    {% endif %}
  </section>

</div>