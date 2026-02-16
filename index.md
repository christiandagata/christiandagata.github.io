---
title: "Home"
layout: single
permalink: /
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

<div class="mag-wrap">

{% assign featured_books = site.books | where: "featured", true | sort: "featured_rank" %}
{% assign fb = featured_books | first %}

{% if fb %}
  <section class="mag-hero">
    {% if fb.cover %}
      <div>
        <img src="{{ fb.cover | relative_url }}" alt="Cover {{ fb.title }}">
      </div>
    {% endif %}
    <div>
      <p class="mag-kicker">Featured Book</p>
      <h2 style="margin-bottom:.2rem;">
        <a href="{{ fb.url | relative_url }}">{{ fb.title }}</a>
      </h2>
      <div class="mag-meta">
        {% if fb.publisher %}{{ fb.publisher }}{% endif %}{% if fb.date %} · {{ fb.date | date: "%Y" }}{% endif %}
      </div>

      {% if fb.synopsis_short %}
        <p class="mag-excerpt">{{ fb.synopsis_short }}</p>
      {% endif %}

      <div class="mag-actions">
        {% if fb.index_pdf %}
          <a class="mag-btn" href="{{ fb.index_pdf | relative_url }}" target="_blank" rel="noopener">Indice (PDF)</a>
        {% endif %}

        <a class="mag-btn secondary" href="{{ fb.url | relative_url }}">Scheda libro</a>

        {% if fb.buy_links %}
          {% for l in fb.buy_links %}
            <a class="mag-btn secondary" href="{{ l.url }}" target="_blank" rel="noopener">Pagina editore</a>
            {% break %}
          {% endfor %}
        {% endif %}
      </div>
    </div>
  </section>
{% endif %}

{% capture render_card %}
<div class="mag-card">
  <p class="mag-kicker">{{ kicker }}</p>
  <h3 class="mag-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if meta %}<div class="mag-meta">{{ meta }}</div>{% endif %}
  {% if excerpt %}<div class="mag-excerpt">{{ excerpt }}</div>{% endif %}
</div>
{% endcapture %}

<section class="mag-section">
  <h2>Featured Publications</h2>
  <div class="mag-grid">
    {% assign items = site.publications | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = "Publication" %}
      {% capture meta %}
        {% if item.venue %}{{ item.venue }}{% endif %}{% if item.date %} · {{ item.date | date: "%Y" }}{% endif %}
        {% if item.doi %} · <img class="doi-badge" alt="DOI" src="https://img.shields.io/badge/DOI-{{ item.doi | uri_escape }}-blue">{% endif %}
      {% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
  <p style="margin-top:.8rem;">
    <a class="mag-btn secondary" href="{{ '/publications/' | relative_url }}">Vedi la lista completa delle pubblicazioni</a>
  </p>
</section>

<section class="mag-section">
  <h2>Featured Software</h2>
  <div class="mag-grid">
    {% assign items = site.software | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = "Software" %}
      {% capture meta %}{% if item.github %}<a href="{{ item.github }}" target="_blank" rel="noopener">GitHub</a>{% endif %}{% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
</section>

<section class="mag-section">
  <h2>Featured Datasets</h2>
  <div class="mag-grid">
    {% assign items = site.datasets | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = "Dataset" %}
      {% capture meta %}
        {% if item.doi %}DOI: {{ item.doi }} · <img class="doi-badge" alt="DOI" src="https://img.shields.io/badge/DOI-{{ item.doi | uri_escape }}-blue">{% endif %}
      {% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
</section>

<section class="mag-section">
  <h2>Featured Activity</h2>
  <div class="mag-grid">
    {% assign items = site.activity | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = item.activity_type | default: "Activity" %}
      {% capture meta %}{% if item.period %}{{ item.period }}{% endif %}{% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
  <p style="margin-top:.8rem; display:flex; gap:.6rem; flex-wrap:wrap;">
    <a class="mag-btn secondary" href="{{ '/activity/' | relative_url }}">Vedi la lista completa delle attività</a>
    <a class="mag-btn secondary" href="{{ '/activity/#teaching' | relative_url }}">Teaching</a>
    <a class="mag-btn secondary" href="{{ '/activity/#training' | relative_url }}">Training</a>
    <a class="mag-btn secondary" href="{{ '/activity/#research' | relative_url }}">Research</a>
  </p>
</section>

<section class="mag-section">
  <h2>Featured Associations</h2>
  <div class="mag-grid">
    {% assign items = site.associations | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = "Association / Editorial" %}
      {% capture meta %}{% if item.period %}{{ item.period }}{% endif %}{% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
</section>

<section class="mag-section">
  <h2>Featured Conferences</h2>
  <div class="mag-grid">
    {% assign items = site.conferences | where: "featured", true | sort: "featured_rank" %}
    {% for item in items limit:10 %}
      {% assign kicker = "Conference / Talk" %}
      {% capture meta %}{{ item.location }}{% if item.date %} · {{ item.date | date: "%d/%m/%Y" }}{% endif %}{% endcapture %}
      {% assign excerpt = item.excerpt | strip_html | truncate: 160 %}
      {{ render_card }}
    {% endfor %}
  </div>
  <p style="margin-top:.8rem;">
    <a class="mag-btn secondary" href="{{ '/conferences/' | relative_url }}">Vedi la lista completa dei convegni</a>
  </p>
</section>

</div>
