---
title: "Dataset"
permalink: /datasets/
layout: single
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign items = site.datasets | default: empty | sort: "date" | reverse %}

<div class="mag-wrap">

  <section class="mag-section" style="margin-top:0;">
    <h2>Dataset</h2>

    {% if items == empty %}
      <p>Al momento non ci sono dataset pubblicati.</p>
    {% else %}
      <ul class="mag-list">
        {% for d in items %}
          <li>
            <div class="mag-date">
              {% if d.date %}{{ d.date | date: "%Y" }}{% else %}—{% endif %}
            </div>

            <div class="mag-main">
              <div>
                <a href="{{ d.url | relative_url }}">{{ d.title }}</a>
                {% if d.doi %}
                  <img class="doi-badge" alt="DOI"
                       src="https://img.shields.io/badge/DOI-{{ d.doi | uri_escape }}-blue">
                {% endif %}
              </div>

              <div class="mag-sub">
                {% if d.description_short %}
                  {{ d.description_short }}
                {% elsif d.excerpt %}
                  {{ d.excerpt | strip_html | truncate: 160 }}
                {% endif %}
              </div>

              <div class="mag-sub" style="margin-top:.35rem;">
                {% if d.zenodo %}
                  <a href="{{ d.zenodo }}" target="_blank" rel="noopener">Zenodo</a>
                {% elsif d.doi %}
                  <a href="https://doi.org/{{ d.doi }}" target="_blank" rel="noopener">DOI</a>
                {% endif %}

                {% if d.github %}
                  {% if d.zenodo or d.doi %} · {% endif %}
                  <a href="{{ d.github }}" target="_blank" rel="noopener">GitHub</a>
                {% endif %}
              </div>
            </div>

            <div class="mag-right">
              <a class="mag-btn secondary" href="{{ d.url | relative_url }}">Scheda</a>
            </div>
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  </section>

</div>
