---
layout: blog
title: jeffrin.com Stack
subtitle: Build and host a SSL-protected Hugo site for free with GitHub and Netlify
date: 2020-06-17T05:12:10.812Z
lastmod: 2020-06-17T05:12:10.823Z
draft: false
---
# Previously on jeffrin.com

It started with Leo Laporte recommending Hugo on one of the various TWiT shows. Hugo is an open-source static site generator written in Go, touted for its speed and efficiency. 

I'd been using carrrd.co as a low-cost, low-maintenance landing page for jeffrin.com for about a year. While it did a fine job and looked decent, it wasn't very gratifying to get it up and running. I had no desire to tinker with it once it was in a finished state. That said, if you're looking for a simpler, lighter, more affordable site builder, consider carrrd.co before you jump to Squarespace and Wix.

So about a week ago I challenged myself to create a Hugo site, to see if it would be a suitable destination for jeffrin.com in 2020. 

# Hugo FOSS

Hugo is my second go-round on the open source site generator train. Prior to settling for carrrd.co, I sunk a couple weekends into getting GravCMS up and running after discovering it on the Nova Launcher website. I hosted it on Digital Ocean and had it live for a bit, but couldn't justify the monthly cost for a not so glorified landing page. The experience gained from that experiment ended up serving me well with the launching the new site. 

There's a lot I like about Hugo, easily one of my favorite aspects of this new stack is that it's a secure site hosted for free. I host the code on GitHub, which automatically deploys to Netlify, which handles the DNS and SSL cert. 

As a member of dark mode nation, I was pleased to find many of the community-created themes included a built in light/dark mode toggle. The [LoveIt](https://github.com/dillonzq/LoveIt) theme by dillonzq ticked all the boxes of my requirements, and had a clean aesthetic I was looking for. Bonus points for the math equation shortcodes, which I'll likely never use, but I have a soft spot for math. 

# Move slow, still break things