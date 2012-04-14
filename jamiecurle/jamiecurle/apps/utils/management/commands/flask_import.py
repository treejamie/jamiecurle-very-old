# -*- coding: utf-8 -*-
import yaml
import os
import codecs
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from omblog.models import Post, Tag

MDFILES = '/Users/jcurle/Sites/jamiecurle/jamiecurle_flask/content/blog'
class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        #
        #
        # kill all
        Post.objects.all().delete()
        Tag.objects.all().delete()
        #
        #
        # now import
        for mdfile in os.listdir(MDFILES):
            if mdfile == '.DS_Store':
                continue
            f = '%s/%s' % (MDFILES, mdfile)
            with codecs.open(f, encoding='UTF-8') as md:
                contents = md.read()
                parts = contents.split('---')
                header = yaml.load(parts[0])
            # build the post
            try:
                # make post
                p = Post()
                # created
                p.created = header['created']
                # title
                p.title = header['title']
                # url
                slug = mdfile.split('/').pop().split('.')[0]
                if slug.startswith('201'):
                    slug = slug[11:]
                p.slug = slug
                # description
                p.description = header['description']
                # contents
                p.source_content = parts[1]
                # status
                p.status = p.PUBLISHED
                # save it
                p.save()
                # tags
                try:
                    for tag in header['tags']:
                        tag, created = Tag.objects.get_or_create(tag=tag)
                        if created:
                            tag.slug = slugify(tag)
                            tag.save()
                        p.tags.add(tag)
                except KeyError:
                    pass
            except TypeError:
                # is an scrappy idea
                # make post
                if mdfile == 'index.html':
                    continue
                p = Post()
                p.title = mdfile[11:]
                p.slug = slugify(p.title)
                p.contents = contents
                p.save()