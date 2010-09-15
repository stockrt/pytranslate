#!/usr/bin/env python
# -*- coding: utf-8 -*-

### GENERIC_SETUP_MARKER_START ###
__program_file__     = 'translate.py'
__program_name__     = '%s' % __program_file__.split('.py')[0]
__scripts__          = []
__data_files__       = []
__version__          = '0.1.2'
__date__             = '2010/09/14'
__author_email__     = 'stockrt@gmail.com'
__author__           = 'Rogério Carvalho Schneider <%s>' % __author_email__
__maintainer_email__ = __author_email__
__maintainer__       = __author__
__copyright__        = 'Copyright (C) 2010 Rogério Carvalho Schneider'
__license__          = 'GPLv3'
__url__              = 'http://stockrt.github.com'
__download_url__     = __url__
__py_modules__       = [__program_name__]
__platforms__        = ['any']
__keywords__         = 'google translate wrapper pytranslate'
__classifiers__      = ['Development Status :: 1 - Planning',
'Environment :: Web Environment',
'Intended Audience :: End Users/Desktop',
'License :: OSI Approved :: GNU General Public License (GPL)',
'Operating System :: OS Independent',
'Programming Language :: Python',
'Topic :: Utilities']
__description__      = 'Google Translate wrapper for Python.'
__long_description__ = '''%s
Google Translate wrapper for Python.
''' % __program_file__
__rpm_data__        = '''
%files
%defattr(-,root,root,-)
@@PYLIB_MARKER@@/%{name}-%{unmangled_version}-py@@PYVER_MARKER@@.egg-info
'''
### GENERIC_SETUP_MARKER_END ###

import urllib

lc = {'afrikaans':'af',
      'albanian':'sq',
      'arabic':'ar',
      'belarusian':'be',
      'bulgarian':'bg',
      'catalan':'ca',
      'chinese':'zh',
      'croatian':'hr',
      'czech':'cs',
      'danish':'da',
      'dutch':'nl',
      'english':'en',
      'estonian':'et',
      'filipino':'tl',
      'finnish':'fi',
      'french':'fr',
      'galician':'gl',
      'german':'de',
      'greek':'el',
      'hebrew':'iw',
      'hindi':'hi',
      'hungarian':'hu',
      'icelandic':'is',
      'indonesian':'id',
      'irish':'ga',
      'italian':'it',
      'japanese':'ja',
      'korean':'ko',
      'latvian':'lv',
      'lithuanian':'lt',
      'macedonian':'mk',
      'malay':'ms',
      'maltese':'mt',
      'norwegian':'no',
      'persian':'fa',
      'polish':'pl',
      'portuguese':'pt',
      'romanian':'ro',
      'russian':'ru',
      'serbian':'sr',
      'slovak':'sk',
      'slovenian':'sl',
      'spanish':'es',
      'swahili':'sw',
      'swedish':'sv',
      'thai':'th',
      'turkish':'tr',
      'ukrainian':'uk',
      'vietnamese':'vi',
      'welsh':'cy',
      'yiddish':'yi',
      'auto':'auto',
}

def translate(text, sl='auto', tl='portuguese'):
    '''
    Translates text and returns resulting sentences from Google Translate.

    print translate.translate('hello', sl='english', tl='portuguese')
    print translate.translate('hello', sl='auto', tl='portuguese')
    print translate.translate('hallo', sl='auto', tl='portuguese')
    print translate.translate('hallo', sl='auto', tl='french')
    print translate.translate('Bonjour', sl='auto', tl='dutch')
    '''

    urllib.FancyURLopener.version = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1'
    f = urllib.FancyURLopener()
    post_params = urllib.urlencode({'client':'t', 'text':text, 'sl':'%s' % (lc[sl.lower()]), 'tl':'%s' % (lc[tl.lower()])})
    content = f.open('http://translate.google.com/translate_a/t', post_params).read()
    try:
        return content[4:].split('"')[0]
    except:
        return text
