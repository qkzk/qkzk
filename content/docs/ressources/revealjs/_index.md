+++
title = "revealjs"
slug = "revealjs"
description = "present content as a reveal.js slide"
+++

This shortcode will format the enclosed markdow to render it with [reveal.js](http://lab.hakim.se/reveal-js/) at runtime (client-side)

Read more on [revealjs github repo](https://github.com/hakimel/reveal.js/#markdown).

## Usage

`revealjs` can use the following named parameters :

* theme
* transition
* controls
* progress
* history
* center


{{% hint warning %}}Even if the enclosed content is a mardown, use `<` shortcode notation instead of the `%` notation {{% /hint %}}

### Content formating and slide delimiters


## Demo


{{<revealjs theme="white" progress="true">}}

# In the morning

___


## Getting up

* Turn off alarm
* Get out of bed

___

## Breakfast

- Eat eggs
- Drink coffee

---

# In the evening

___

## Dinner

- Eat spaghetti
- Drink wine

___

## Going to sleep

- Get in bed
- Count sheep

{{</revealjs>}}

