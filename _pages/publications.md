---
title: "Publications"
permalink: /publications/
layout: single
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign books = site.books | default: empty | sort: "date" | reverse %}
{% assign pub_all = site.publications | sort: "date" | reverse %}
{% assign pub_other = pub_all | where_exp: "p", "p.pub_type != 'book'" %}

<div id="books"></div>
## Books
<div class="mag-wrap">
  <section class="mag-section" style="margin-top:0;">
    <div class="mag-grid">
      {% for b in books %}
        <div class="mag-card">
          {% if b.cover %}
            <div style="display:flex; gap:1rem; align-items:flex-start;">
              <div style="flex:0 0 120px;">
                <a href="{{ b.url | relative_url }}">
                  <img src="{{ b.cover | relative_url }}" alt="Cover {{ b.title }}" style="width:120px;border-radius:12px;border:1px solid var(--mag-border);">
                </a>
              </div>
              <div style="flex:1 1 auto;">
                <p class="mag-kicker">Libro</p>
                <h3 class="mag-title">
                  <a href="{{ b.url | relative_url }}">{{ b.title }}</a>
                </h3>

                <div class="mag-meta">
                  {% if b.publisher %}{{ b.publisher }}{% endif %}
                  {% if b.date %} · {{ b.date | date: "%Y" }}{% endif %}
                </div>

                {% if b.synopsis_short %}
                  <div class="mag-excerpt">{{ b.synopsis_short }}</div>
                {% elsif b.excerpt %}
                  <div class="mag-excerpt">{{ b.excerpt | strip_html | truncate: 220 }}</div>
                {% endif %}

                <div class="mag-actions" style="margin-top:.7rem;">
                  <a class="mag-btn secondary" href="{{ b.url | relative_url }}">Scheda</a>

                  {% if b.index_pdf %}
                    <a class="mag-btn secondary" href="{{ b.index_pdf | relative_url }}" target="_blank" rel="noopener">Indice (PDF)</a>
                  {% endif %}

                  {% if b.buy_links %}
                    {% for l in b.buy_links %}
                      <a class="mag-btn" href="{{ l.url }}" target="_blank" rel="noopener">{{ l.label | default: "Acquista" }}</a>
                      {% break %}
                    {% endfor %}
                  {% endif %}
                </div>
              </div>
            </div>
          {% else %}
            <p class="mag-kicker">Libro</p>
            <h3 class="mag-title"><a href="{{ b.url | relative_url }}">{{ b.title }}</a></h3>
            <div class="mag-meta">
              {% if b.publisher %}{{ b.publisher }}{% endif %}
              {% if b.date %} · {{ b.date | date: "%Y" }}{% endif %}
            </div>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </section>
</div>

## Articles, chapters, proceedings
{% for p in pub_other %}
- [{{ p.title }}]({{ p.url | relative_url }})
  {% if p.venue %} — {{ p.venue }}{% endif %}{% if p.date %} ({{ p.date | date: "%Y" }}){% endif %}
  {% if p.citation or p.doi %}
  <div class="pub-entry-meta">
    {% if p.citation %}{{ p.citation }}{% endif %}
    {% if p.doi %}<a href="https://doi.org/{{ p.doi }}">DOI</a>{% endif %}
  </div>
  {% endif %}
{% endfor %}
