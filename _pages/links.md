---
title: "Links"
permalink: /links/
layout: single
author_profile: true
---

<link rel="stylesheet" href="{{ '/assets/css/magazine.css' | relative_url }}">

{% assign tools = site.software | default: empty | sort: "date" | reverse %}

<div class="mag-wrap">
  <section class="mag-section" style="margin-top:0;">
    <h2>Pagine web e portali</h2>
    <div class="mag-grid">
      <div class="mag-card">
        <p class="mag-kicker">Sito personale</p>
        <h3 class="mag-title">
          {% if site.author.uri contains "http" %}
            <a href="{{ site.author.uri }}" target="_blank" rel="noopener">{{ site.author.uri }}</a>
          {% else %}
            <a href="https://{{ site.author.uri }}" target="_blank" rel="noopener">{{ site.author.uri }}</a>
          {% endif %}
        </h3>
        <div class="mag-excerpt">Portale principale con profilo, pubblicazioni, attività e risorse.</div>
      </div>

      <div class="mag-card">
        <p class="mag-kicker">Repository</p>
        <h3 class="mag-title">
          {% if site.author.github %}
            <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">GitHub / {{ site.author.github }}</a>
          {% else %}
            <span>GitHub</span>
          {% endif %}
        </h3>
        <div class="mag-excerpt">Codice, prototipi, script e materiali di ricerca in sviluppo.</div>
      </div>
    </div>
  </section>

  <section class="mag-section">
    <h2>Social e profili accademici</h2>
    <ul class="mag-list">
      {% if site.author.googlescholar %}
      <li>
        <div class="mag-date">Scholar</div>
        <div class="mag-main">
          <div><a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a></div>
          <div class="mag-sub">Profilo bibliografico e citazioni.</div>
        </div>
      </li>
      {% endif %}

      {% if site.author.orcid %}
      <li>
        <div class="mag-date">ORCID</div>
        <div class="mag-main">
          <div><a href="{{ site.author.orcid }}" target="_blank" rel="noopener">{{ site.author.orcid }}</a></div>
          <div class="mag-sub">Identificativo autore e tracciamento attività di ricerca.</div>
        </div>
      </li>
      {% endif %}

      {% if site.author.bluesky %}
      <li>
        <div class="mag-date">Bluesky</div>
        <div class="mag-main">
          <div>
            {% if site.author.bluesky contains "http" %}
              <a href="{{ site.author.bluesky }}" target="_blank" rel="noopener">{{ site.author.bluesky }}</a>
            {% else %}
              <a href="https://{{ site.author.bluesky }}" target="_blank" rel="noopener">{{ site.author.bluesky }}</a>
            {% endif %}
          </div>
          <div class="mag-sub">Aggiornamenti pubblici su attività e progetti.</div>
        </div>
      </li>
      {% endif %}
    </ul>
  </section>

  <section class="mag-section">
    <h2>Software e strumenti pubblicati</h2>
    {% if tools == empty %}
      <p>Al momento non ci sono schede software pubblicate.</p>
    {% else %}
      <ul class="mag-list">
        {% for s in tools %}
          <li>
            <div class="mag-date">{% if s.date %}{{ s.date | date: "%Y" }}{% else %}—{% endif %}</div>
            <div class="mag-main">
              <div><a href="{{ s.url | relative_url }}">{{ s.title }}</a></div>
              {% if s.excerpt %}
              <div class="mag-sub">{{ s.excerpt | strip_html | truncate: 180 }}</div>
              {% endif %}
              {% if s.github %}
              <div class="mag-sub" style="margin-top:.35rem;">
                <a href="{{ s.github }}" target="_blank" rel="noopener">GitHub</a>
              </div>
              {% endif %}
            </div>
            <div class="mag-right">
              <a class="mag-btn secondary" href="{{ s.url | relative_url }}">Scheda</a>
            </div>
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  </section>

  <section class="mag-section">
    <h2>In sviluppo</h2>
    <div class="mag-grid">
      <div class="mag-card">
        <p class="mag-kicker">Roadmap</p>
        <h3 class="mag-title">Prossimi strumenti e prototipi</h3>
        <div class="mag-excerpt">
          Questa sezione raccoglierà i software in sviluppo (beta, prototipi, tool interni e ambienti di test) con link a demo e repository non appena disponibili.
        </div>
      </div>
    </div>
  </section>
</div>
