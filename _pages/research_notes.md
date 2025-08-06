---
layout: default
permalink: /research-notes/
title: research notes
nav: true
nav_order: 3
pagination:
  enabled: true
  collection: research_notes
  permalink: /research-notes/page/:num/
  per_page: 5
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
---

<div class="post">

{% assign research_notes_name_size = site.research_notes_name | size %}
{% assign research_notes_description_size = site.research_notes_description | size %}

{% if research_notes_name_size > 0 or research_notes_description_size > 0 %}
  <div class="header-bar">
    <h1>{{ site.research_notes_name | default: "Research Notes" }}</h1>
    <h2>{{ site.research_notes_description | default: "Notes and observations from ongoing research projects" }}</h2>
  </div>
{% else %}
  <div class="header-bar">
    <h1>Research Notes</h1>
    <h2>Notes and observations from ongoing research projects</h2>
  </div>
{% endif %}

{% if site.display_research_note_tags and site.display_research_note_tags.size > 0 or site.display_research_note_categories and site.display_research_note_categories.size > 0 %}
  <div class="tag-category-list">
    <ul class="p-0 m-0">
      {% for tag in site.display_research_note_tags %}
        <li>
          <i class="fa-solid fa-hashtag fa-sm"></i> <a href="{{ tag | slugify | prepend: '/research-notes/tag/' | relative_url }}">{{ tag }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
      {% if site.display_research_note_categories.size > 0 and site.display_research_note_tags.size > 0 %}
        <p>&bull;</p>
      {% endif %}
      {% for category in site.display_research_note_categories %}
        <li>
          <i class="fa-solid fa-tag fa-sm"></i> <a href="{{ category | slugify | prepend: '/research-notes/category/' | relative_url }}">{{ category }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
    </ul>
  </div>
{% endif %}

{% assign featured_notes = site.research_notes | where: "featured", "true" %}
{% if featured_notes.size > 0 %}
<br>

<div class="container featured-posts">
{% assign is_even = featured_notes.size | modulo: 2 %}
<div class="row row-cols-{% if featured_notes.size <= 2 or is_even == 0 %}2{% else %}3{% endif %}">
{% for note in featured_notes %}
<div class="col mb-4">
<a href="{{ note.url | relative_url }}">
<div class="card hoverable">
<div class="row g-0">
<div class="col-md-12">
<div class="card-body">
<div class="float-right">
<i class="fa-solid fa-thumbtack fa-xs"></i>
</div>
<h3 class="card-title text-lowercase">{{ note.title }}</h3>
<p class="card-text">{{ note.description }}</p>

                    {% if note.external_source == blank %}
                      {% assign read_time = note.content | number_of_words | divided_by: 180 | plus: 1 %}
                    {% else %}
                      {% assign read_time = note.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
                    {% endif %}
                    {% assign year = note.date | date: "%Y" %}

                    <p class="post-meta">
                      {{ read_time }} min read &nbsp; &middot; &nbsp;
                      <a href="{{ year | prepend: '/research-notes/' | relative_url }}">
                        <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>
                      {% if note.related_project %}
                        &nbsp; &middot; &nbsp;
                        {% assign project = site.projects | where: "title", note.related_project | first %}
                        {% if project %}
                          <a href="{{ project.url | relative_url }}">
                            <i class="fa-solid fa-project-diagram fa-sm"></i> {{ note.related_project }}
                          </a>
                        {% else %}
                          <i class="fa-solid fa-project-diagram fa-sm"></i> {{ note.related_project }}
                        {% endif %}
                      {% endif %}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
      {% endfor %}
      </div>
    </div>
    <hr>

{% endif %}

  <ul class="post-list">

    {% if page.pagination.enabled %}
      {% assign notelist = paginator.posts %}
    {% else %}
      {% assign notelist = site.research_notes %}
    {% endif %}

    {% for note in notelist %}

    {% if note.external_source == blank %}
      {% assign read_time = note.content | number_of_words | divided_by: 180 | plus: 1 %}
    {% else %}
      {% assign read_time = note.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
    {% endif %}
    {% assign year = note.date | date: "%Y" %}
    {% assign tags = note.tags | join: "" %}
    {% assign categories = note.categories | join: "" %}

    <li>

{% if note.thumbnail %}

<div class="row">
          <div class="col-sm-9">
{% endif %}
        <h3>
        {% if note.redirect == blank %}
          <a class="post-title" href="{{ note.url | relative_url }}">{{ note.title }}</a>
        {% elsif note.redirect contains '://' %}
          <a class="post-title" href="{{ note.redirect }}" target="_blank">{{ note.title }}</a>
          <svg width="2rem" height="2rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path>
          </svg>
        {% else %}
          <a class="post-title" href="{{ note.redirect | relative_url }}">{{ note.title }}</a>
        {% endif %}
      </h3>
      <p>{{ note.description }}</p>
      <p class="post-meta">
        {{ read_time }} min read &nbsp; &middot; &nbsp;
        {{ note.date | date: '%B %d, %Y' }}
        {% if note.external_source %}
        &nbsp; &middot; &nbsp; {{ note.external_source }}
        {% endif %}
        {% if note.related_project %}
          &nbsp; &middot; &nbsp;
          {% assign project = site.projects | where: "title", note.related_project | first %}
          {% if project %}
            <a href="{{ project.url | relative_url }}">
              <i class="fa-solid fa-project-diagram fa-sm"></i> {{ note.related_project }}
            </a>
          {% else %}
            <i class="fa-solid fa-project-diagram fa-sm"></i> {{ note.related_project }}
          {% endif %}
        {% endif %}
      </p>
      <p class="post-tags">
        <a href="{{ year | prepend: '/research-notes/' | relative_url }}">
          <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>

          {% if tags != "" %}
          &nbsp; &middot; &nbsp;
            {% for tag in note.tags %}
            <a href="{{ tag | slugify | prepend: '/research-notes/tag/' | relative_url }}">
              <i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</a>
              {% unless forloop.last %}
                &nbsp;
              {% endunless %}
              {% endfor %}
          {% endif %}

          {% if categories != "" %}
          &nbsp; &middot; &nbsp;
            {% for category in note.categories %}
            <a href="{{ category | slugify | prepend: '/research-notes/category/' | relative_url }}">
              <i class="fa-solid fa-tag fa-sm"></i> {{ category }}</a>
              {% unless forloop.last %}
                &nbsp;
              {% endunless %}
              {% endfor %}
          {% endif %}
    </p>

{% if note.thumbnail %}

</div>

  <div class="col-sm-3">
    <img class="card-img" src="{{ note.thumbnail | relative_url }}" style="object-fit: cover; height: 90%" alt="image">
  </div>
</div>
{% endif %}
    </li>

    {% endfor %}

  </ul>

{% if page.pagination.enabled %}
{% include pagination.liquid %}
{% endif %}

</div>
