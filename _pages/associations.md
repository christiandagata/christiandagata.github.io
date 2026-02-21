---
title: "Associazioni"
permalink: /associations/
layout: single
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign items = site.associations | default: empty | sort: "date" | reverse %}

<div class="mag-wrap">
  <section class="mag-section" style="margin-top:0;">
    <h2>Appartenenze e incarichi</h2>

    {% if items == empty %}
      <p>Al momento non ci sono associazioni pubblicate.</p>
    {% else %}
      <ul class="mag-list">
        {% for a in items %}
          <li>
            <div class="mag-date">
              {% if a.period %}
                {{ a.period }}
              {% elsif a.date %}
                {{ a.date | date: "%Y" }}
              {% else %}
                —
              {% endif %}
            </div>

            <div class="mag-main">
              <div><a href="{{ a.url | relative_url }}">{{ a.title }}</a></div>

              {% if a.excerpt %}
                <div class="mag-sub">{{ a.excerpt | strip_html | truncate: 180 }}</div>
              {% endif %}
            </div>

            <div class="mag-right">
              <a class="mag-btn secondary" href="{{ a.url | relative_url }}">Scheda</a>
            </div>
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  </section>
</div>
