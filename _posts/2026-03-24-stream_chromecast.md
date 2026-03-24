---
layout: post
title:  "Guida per fare lo Streaming da linux su Chromecast"
date:   2026-03-24
tags: programming
category: [Programming] #One, more categories or no at all.
author: jpo85 #Author's nick.
nextPart: #Next part.
prevPart: #Previous part.
og_image: #Open Graph preview image.
og_description: "descrizione." #Open Graph description.
fb_app_id: example
---
Per fare lo streaming su chromecast di un video direttamente da linux, va installato un pacchetto chiamato  **mkchromecast**.   

Al posto delle virgolette inserire il path del video da riprodurre su crhomecast.
```bash
sudo mkchromecast --control --video -i "/media/file.avi"
```