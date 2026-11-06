# Blog

My portfolio: projects, challenges I wrote, and writeups of challenges I solved.

## Build and preview

```sh
python3 build.py
python3 -m http.server -d dist
```

Then open http://localhost:8000. On a machine without the dependencies, run `pip install -r requirements.txt` first.

## Edit the home page

The about text is in `content/about.md`. The tagline and contact links are in `site.yml`.

## Add content

Add a Markdown file, and its name becomes the URL. Images go in `static/images/` and are referenced as `/images/...`.

`content/writeups/my-challenge.md`:

```markdown
---
title: My Challenge
ctf: Some CTF 2026
type: Side Channel
difficulty: Medium
date: '2026-11-06'
category: hardware
author: challenge author
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/SomeCTF/MyChallenge
---

## Description
...
```

`type` and `difficulty` feed the filters on the writeups page. `category` and `author` are optional.

`content/challenges/` takes the same fields except `type`, with `category` required and `difficulty` optional. `content/projects/` takes `title`, `summary`, `date` and `repo`, plus the optional `language`, `requires` and `license`.

## Publish

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and deploys it to GitHub Pages. In the repository settings, Pages must have its source set to "GitHub Actions".
