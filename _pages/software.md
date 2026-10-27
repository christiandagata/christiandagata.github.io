---
title: "Software e siti web"
permalink: /software/
layout: single
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign items = site.software | sort: "featured_rank" %}

<div class="mag-wrap">
  <section class="mag-section" style="margin-top:0;">
    <p>Portali, archivi digitali e hyperedizioni alla cui progettazione, curatela e implementazione ho partecipato.</p>
    <div class="mag-grid">
      {% for item in items %}
        <div class="mag-card">
          {% if item.link %}{% include site-shot.html item=item %}{% endif %}
          <p class="mag-kicker">Sito web</p>
          <h3 class="mag-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
          {% if item.role %}<div class="mag-meta">{{ item.role }}</div>{% endif %}
          <div class="mag-actions" style="margin-top:.7rem;">
            <a class="mag-btn secondary" href="{{ item.url | relative_url }}">Scheda</a>
            {% if item.link %}<a class="mag-btn" href="{{ item.link }}" target="_blank" rel="noopener">Apri il sito</a>{% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  </section>
</div>
