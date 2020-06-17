---
layout: blog
title: jeffrin.com Stack
subtitle: How I built an SSL-protected Hugo site for free with GitHub and Netlify
date: 2020-06-17T05:12:10.812Z
lastmod: 2020-06-17T17:03:03.095Z
draft: false
---
## Previously on jeffrin.com

It started with [Leo Laporte](https://twitter.com/leolaporte) recommending Hugo on one of the various [TWiT](https://twit.tv/) shows. [Hugo](https://gohugo.io/) is an open-source static site generator written in Go, touted for its speed and efficiency. 

I'd been using [carrd.co](https://carrd.co/) as a low-cost, low-maintenance landing page for jeffrin.com for about a year. While it did a fine job and looked decent, it wasn't gratifying to get it up and running. I had no desire to tinker with it beyond the first draft. That said, if you're looking for an approachable, light, affordable site builder, consider carrd.co before you jump to Squarespace and Wix.

So about a week ago I challenged myself to create a Hugo site, to see if it would be a suitable destination for jeffrin.com in 2020. 

## Hugo FOSS

Hugo is my second go-round on the open source site generator train. Prior to settling for carrrd.co, I sunk a couple weekends into getting [GravCMS](https://getgrav.org/) up and running after discovering it on the [Nova Launcher website](http://novalauncher.com/). I hosted it on [Digital Ocean](https://www.digitalocean.com/) and had it live for a bit, but couldn't justify the monthly cost for a not so glorified landing page. The experience gained from that experiment ended up serving me well with the launching the new site. 

There's a lot I like about Hugo, easily one of my favorite aspects of this new stack is that it's a secure site hosted for free. I host the code on GitHub, which automatically deploys to [Netlify](http://netlify.com/), which handles the DNS and SSL certificate. 

As a member of dark mode nation, I was pleased to find many of the community-created themes included a built in light/dark mode toggle. The [LoveIt theme](https://hugoloveit.com/) by dillonzq ticked all the boxes of my requirements with a clean aesthetic. Bonus points for the equation shortcodes, which I'll likely never use, but touch my soft spot for maths. 

## Move slow, still break things

Building the version of the site on my Mac was remarkably easy. I flipped back and forth between the Hugo [Quick Start guide](https://gohugo.io/getting-started/quick-start/) and the documentation for my theme, and loaded it at localhost:1313 in the first hour. 

The first issue I ran into was that my avatar image would not load. I checked, then re-checked the configuration and put the file in a couple different folders, no luck. I thought it might be a limitation of hosting the site locally, so I put a pin in that issue and moved on to exploring hosting solutions.

## A place to call home

Hugo has a built-in deploy function that automatically generates your site pages and pushes them to the cloud storage bucket of your choosing. I chose Google Cloud Storage over Amazon S3 and Microsoft Azure. Because it was my first project on GCS, I was given a $100 credit so I wouldn't have to pay to play, at least up front.

After generating a bunch of API keys and service accounts, the site was live for the world to see, for all of 15 minutes. I restricted access with the intention of making it public once I arrived at a first version I was comfortable with.

But while tinkering away on my Mac, it donned on me that I'd want to edit and post to the site from my Windows machine, and possibly my phone. I looked at GCS FUSE, a product that lets you sync a bucket from the cloud to your local machine, but found it too complex for my needs.

## "deploy hugo site from multiple computers"

That was the Google search that led me to [Automating the deployment of your static site with Hugo and GitHub](https://gomakethings.com/automating-the-deployment-of-your-static-site-with-hugo-and-github/) by Chris Ferdinandi. And I had my roadmap.

I followed the "The easy way" and pushed my site to GitHub. There were stumbles, errors, Google searches for those errors, but eventually, I signed up for Netlify, connected it to GitHub, and the site was live again. I verified jeffrin.com, and had my second home for jeffrin.com in as many weeks.

The topper to this setup is NetlifyCMS an ultra lightweight CMS that I configured to work with my site, so I would have a simple interface to log into and post from any device.

## It takes a village

The sterilized retelling of building this site makes it sound a lot easier than it was. While I love the idea of free open-source software, I require a certain level of support as I'm no master coder by any measure. 

The Hugo site and community meet that requirement handily. What I couldn't solve by combing through the documentation, I was able to by consulting the [Hugo forums](https://discourse.gohugo.io/). 

This includes the avatar loading issue, which was easily solved by placing the image in the static/images folder. Duh.

## Where do we go

And here we are. jeffrin.com is now public to the internet. I'm proud enough of the build that I felt compelled to write this post, which is the longest piece I've written for personal reasons in an indeterminable amount of time. 

I've circled a few topics in my head that I'll address in future posts: my productivity stack, the mobile device landscape, remote working. I'll fight with all that I have and my Bullet Journal to avoid going years without posting. 

If you've read to this point, I'm grateful and hope you'll return.