# -*- coding: utf-8-unix; mode: python -*-
"""Module to assist to make HTML for Python 3.

This module provides class that assist to make HTML.

Author: 2011, 2017 IMAI Toshiyuki

Copyright (c) 2011, 2017 IMAI Toshiyuki

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php

Class:
    HTML -- Assist to make HTML.
"""
__author__ = 'IMAI Toshiyuki'
__version__ = '1.0'

import os
from http import cookies
import cgi
import html

class HTML:

    """Assist to make HTML.

    Attributes:
        encode -- encoding
        lang -- lang attribute of html element
        sitetitle -- site title
        pagetitle -- default page title
        titledelimiter -- delimiter of site title and page title
        cssfiles -- list object that contains path strings to css files
        jsfiles -- list object that contains path string to JavaScript files
        jstext -- text of JavaScript code
        cookie -- http cookie
        nocache -- if it is True then do not make user agents create cache

    Methodes:
        set_encode(encode) -- Set attribute encode.
        set_lang(lang) -- Set attribute lang.
        set_site_title(sitetitle) -- Set attribute sitetitle.
        set_page_title(pagetitle) -- Set attribute pagetitle.
        set_titledelimiter(titledelimiter) -- Set attribute titledelimiter.
        set_cookie(cookie) -- Set attribute cookie.
        set_nocache(nocache) -- Set attribute nocache.
        print_resp_header() -- Print HTTP Response Header.
        print_html_header() -- Print xhtml DTD, html start tag, head element
                               and body start tag.
        print_html_close() -- Print end tags of body element and html element.
        h1(content, [attrs]) -- Create h1 element.
        h2(content, [attrs]) -- Create h2 element.
        h3(content, [attrs]) -- Create h3 element.
        h4(content, [attrs]) -- Create h4 element.
        h5(content, [attrs]) -- Create h5 element.
        h6(content, [attrs]) -- Create h6 element.
        p(content, [attrs]) -- Create p element.
        start_p([attrs]) -- Create start tag of p element.
        end_p() -- Create end tag of p element.
        div(content, [attrs]) -- Create div element.
        start_div([attrs]) -- Create start tag of div element.
        end_div() -- Create end tag of div element.
        blockquote(content, [cite], [attrs]) -- Create blockquote element.
        start_blockquote([cite], [attrs]) -- Create start tag of blockquote
                                             element.
        end_blockquote() -- Create end tag of blockquote element.
        pre(content, [attrs]) -- Create pre element.
        start_pre([attrs]) -- Create start tag of pre element.
        end_pre() -- Create end tag of pre element.
        address(content, [attrs]) -- Create address element.
        Del(content, [attrs]) -- Create del element.
        ins(content, [attrs]) -- Create ins element.
        a(content, [attrs]) -- Create a element.
        em(content, [attrs]) -- Create em element.
        strong(content, [attrs]) -- Create strong element.
        abbr(content, [attrs]) -- Create abbr element.
        acronym(content, [attrs]) -- Create acronym element.
        bdo(content, [attrs]) -- Create bdo element.
        cite(content, [attrs]) -- Create cite element.
        code(content, [attrs]) -- Create code element.
        dfn(content, [attrs]) -- Create dfn element.
        kbd(content, [attrs]) -- Create kbd element.
        q(content, [attrs]) -- Create q element.
        samp(content, [attrs]) -- Create samp element.
        span(content, [attrs]) -- Create span element.
        sub(content, [attrs]) -- Create sub element.
        sup(content, [attrs]) -- Create sup element.
        var(content, [attrs]) -- Create var element.
        ruby(content, title, [attrs]) -- Create ruby element.
        ol(content, [attrs]) -- Create ol element.
        start_ol([attrs]) -- Create start tag of ol element.
        end_ol() -- Create end tag of ol element.
        ul(content, [attrs]) -- Create ul element.
        start_ul([attrs]) -- Create start tag of ul element.
        end_ul() -- Create end tag of ul element.
        li(content, [attrs]) -- Create li element.
        dl(content, [attrs]) -- Create dl element.
        start_dl([attrs]) -- Create start tag of dl element.
        end_dl() -- Create end tag of p element.
        dt(content, [attrs]) -- Create dt element.
        dd(content, [attrs]) -- Create dd element.
        br([attrs]) -- Create br element.
        hr([attrs]) -- Create hr element.
        start_form([method], [action], [enctype], [attrs]) -- Create start tag
                                                              of form element.
        start_multipart_form([method], [action], [enctype], [attrs]) -- Create
                                       start tag of form element for multipart.
        end_form() -- Create end tag of form element.
        textfield([name], [value], [size], [maxlength], [attrs]) -- Create
                                          input element as form item text field.
        textarea([name], [value], [rows], [columns], [attrs]) -- Create textarea
                                                                 element.
        password_field([name], [value], [size], [maxlength], [attrs]) -- Create
                                      input element as form item password field.
        filefield([name], [value], [size], [maxlength], [attrs]) -- Create input
                                                element as form item file field.
        popup_menu([name], [values], [default], [labels], [attributes], [attrs])
            -- Create select element as form item popup menu.
        scrolling_list([name], [values], [default], [size], [multiple],
                       [labels], [attributes], [attrs]) -- Create select element
                                                    as form item scrolling list.
        select_list([name], [values], [default], [labels], [attributes], [size],
                    [multiple], [attrs]) -- Create select element.
        checkbox_group([name], [values], [default], [delimiter], [labels],
                       [attributes], [attrs]) -- Create input elements as form
                                                 item check box group.
        checkbox([name], [checked], [value], [label], [attrs]) -- Create input
                                           element as form item check box group.
        radio_group([name], [values], [default], [delimiter], [labels],
                    [attributes], [attrs]) -- Create input elements as form item
                                              radio button group.
        button_group([type], [name], [values], [default], [delimiter], [labels],
                     [attributes], [attrs]) -- Create input elements.
        submit([name], [value], [attrs]) -- Create input element as form item
                                            submit button.
        reset([name], [value], [attrs]) -- Create input element as form item
                                           reset button.
        button([name], [value], [attrs]) -- Create input element as form item
                                            button.
        hidden([name], [value], [attrs]) -- Create input element as form item
                                            hidden.
        input(type, [attrs]) -- Create input element.

    Useage:
        import htmldocument

        ht = htmldocument.HTML(
            encode='utf-8',
            lang='ja',
            sitetitle='Site Name',
            cssfiles=['./css/main.css'],
            jsfiles=['./js/main.js'])
        html.print_resp_header()
        html.print_html_header()
        print(ht.h1('Header Level 1'))
        print(ht.p('Text body.'))
        html.print_html_close()
    """

    def __init__(self, encode='utf-8', lang='en', sitetitle='Untitled Site',
                 pagetitle='Untitled', titledelimiter=' :: ',
                 cssfiles=None, jsfiles=None, jstext=None, cookie=None,
                 nocache=False):

        """Constructor of class HTML.

        Keyword arguments:
            encode -- encoding (default 'utf-8')
            lang -- lang attribute of html element (default 'en')
            sitetitle -- site title (default 'Untitled Site')
            pagetitle -- default page title (default 'Untitled')
            titledelimiter -- delimiter of site title and page title
                              (default ' :: ')
            cssfiles -- list object that contains path strings to css files
                        (default None)
            jsfiles -- list object that contains path string to JavaScript files
                       (default None)
            jstext -- text of JavaScript code (default None)
            cookie -- http cookie (default None)
            nocache -- if it is True then do not make user agents create cache
                       (default False)
        """

        self.encode = encode
        self.lang = lang
        self.sitetitle = sitetitle
        self.pagetitle = pagetitle
        self.titledelimiter = titledelimiter
        self.cssfiles = cssfiles
        self.jsfiles = jsfiles
        self.jstext = jstext
        self.cookie = cookie
        self.nocache = nocache


    # setters

    def set_encode(self, encode):
        """Set attribute encode."""
        self.encode = encode

    def set_lang(self, lang):
        """Set attribute lang."""
        self.lang = lang

    def set_site_title(self, sitetitle):
        """Set attribute sitetitle."""
        self.sitetitle = sitetitle

    def set_page_title(self, pagetitle):
        """Set attribute pagetitle."""
        self.pagetitle = pagetitle

    def set_titledelimiter(self, titledelimiter):
        """Set attribute titledelimiter."""
        self.titledelimiter = titledelimiter

    def set_cookie(self, cookie):
        """Set attribute cookie."""
        self.cookie = cookie

    def set_nocache(self, nocache):
        """Set attribute nocache."""
        self.nocache = nocache

    # printers

    def print_resp_header(self):

        """Print HTTP Response Header."""

        if self.encode == '' or not isinstance(self.encode, str):
            print('Content-Type: text/html')
        else:
            print('Content-Type: text/html; charset={0}'.format(
                self.encode))

        if isinstance(self.cookie, cookies.SimpleCookie):
            print(self.cookie.output())

        if self.nocache:
            print('Pragma: no-cache')
            print('Cache-Control: no-cache')
            print('Expires: Thu, 01 Dec 1994 16:00:00 GMT')

        print('')

    def print_html_header(self):

        """Print html start tag, head element and body start tag."""

        dtd = '<!DOCTYPE html>'
        print(dtd)
        print('<html lang="{0}">'.format(self.lang))
        print('<head>')
        print('<title>{0} {1} {2}</title>'.format(
            html.escape(self.pagetitle),
            html.escape(self.titledelimiter),
            html.escape(self.sitetitle)))

        if isinstance(self.cssfiles, list):
            for cssfile in self.cssfiles:
                print('<link rel="stylesheet" type="text/css" href="{0}" />'.format(cssfile))
        elif isinstance(self.cssfiles, str):
            print('<link rel="stylesheet" type="text/css" href="{0}" />'.format(self.cssfiles))

        if isinstance(self.jsfiles, list):
            for jsfile in self.jsfiles:
                print('<script type="text/javascript" src="{0}"></script>'.format(jsfile))
        elif isinstance(self.jsfiles, str):
            print('<script type="text/javascript" src="{0}"></script>'.format(self.jsfiles))

        if isinstance(self.jstext, str):
            print('<script type="text/javascript">{0}</script>'.format(
                self.jstext))

        print('</head>')
        print()
        print('<body>')

    def print_html_close(self):
        """Print end tags of body element and html element."""
        print('</body>\n</html>')

    # elements

    # block

    def h1(self, content, attrs=None):
        """Create h1 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h1', content, attrs)

    def h2(self, content, attrs=None):
        """Create h2 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h2', content, attrs)

    def h3(self, content, attrs=None):
        """Create h3 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h3', content, attrs)

    def h4(self, content, attrs=None):
        """Create h4 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h4', content, attrs)

    def h5(self, content, attrs=None):
        """Create h5 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h5', content, attrs)

    def h6(self, content, attrs=None):
        """Create h6 element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('h6', content, attrs)

    def p(self, content, attrs=None):
        """Create p element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('p', content, attrs)

    def start_p(self, attrs=None):
        """Create start tag of p element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('p', attrs)

    def end_p(self):
        """Create end tag of p element."""
        return self._create_end_tag('p')
    
    def div(self, content, attrs=None):
        """Create div element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('div', content, attrs)

    def start_div(self, attrs=None):
        """Create start tag of div element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('div', attrs)

    def end_div(self):
        """Create end tag of div element."""
        return self._create_end_tag('div')

    def blockquote(self, content, cite=None, attrs=None):
        """Create blockquote element.

        Keyword arguments:
            content -- some text
            cite -- cite attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = dict()
        if cite is not None:
            attrs['cite'] = cite
        return self._create_element('blockquote', content, attrs)

    def start_blockquote(self, cite=None, attrs=None):
        """Create start tag of blockquote element.

        Keyword arguments:
            cite -- cite attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = dict()
        if cite is not None:
            attrs['cite'] = cite
        return self._create_start_tag('blockquote', attrs)

    def end_blockquote(self):
        """Create end tag of blockquote element."""
        return self._create_end_tag('blockqute')

    def pre(self, content, attrs=None):
        """Create pre element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('pre', content, attrs)

    def start_pre(self, attrs=None):
        """Create start tag of pre element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('pre', attrs)

    def end_pre(self):
        """Create end tag of pre element."""
        return self._create_end_tag('pre')

    def address(self, content, attrs=None):
        """Create address element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('address', content, attrs)

    def fieldset(self):
        pass

    def Del(self, content, attrs=None):
        """Create del element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('del', content, attrs)

    def ins(self, content, attrs=None):
        """Create ins element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('ins', content, attrs)

    # inline

    def a(self, content, attrs=None):
        """Create a element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('a', content, attrs)

    def em(self, content, attrs=None):
        """Create em element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('em', content, attrs)

    def strong(self, content, attrs=None):
        """Create strong element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('strong', content, attrs)

    def abbr(self, content, attrs=None):
        """Create abbr element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('abbr', content, attrs)

    def acronym(self, content, attrs=None):
        """Create acronym element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('acronym', content, attrs)

    def bdo(self, content, attrs=None):
        """Create bdo element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('bdo', content, attrs)

    def cite(self, content, attrs=None):
        """Create cite element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('cite', content, attrs)

    def code(self, content, attrs=None):
        """Create code element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('code', content, attrs)

    def dfn(self, content, attrs=None):
        """Create dfn element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('dfn', content, attrs)

    def kbd(self, content, attrs=None):
        """Create kbd element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('kbd', content, attrs)

    def q(self, content, attrs=None):
        """Create q element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('q', content, attrs)

    def samp(self, content, attrs=None):
        """Create samp element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('samp', content, attrs)

    def span(self, content, attrs=None):
        """Create span element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('span', content, attrs)

    def sub(self, content, attrs=None):
        """Create sub element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('sub', content, attrs)

    def sup(self, content, attrs=None):
        """Create sup element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('sup', content, attrs)

    def var(self, content, attrs=None):
        """Create var element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('var', content, attrs)

    def ruby(self, content, title, attrs=None):
        """Create ruby element.

        Keyword arguments:
            content -- some text
            title -- ruby title text
            attrs -- dict object that contains attributes (default None)
        """
        return '<ruby><rp>（</rp><rb>{0}</rb><rt>{1}</rb><rp>）</rp></ruby>'.format(content, title)
        

    # list

    def ol(self, content, attrs=None):
        """Create ol element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('ol', content, attrs)

    def start_ol(self, attrs=None):
        """Create start tag of ol element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('ol', attrs)

    def end_ol(self):
        """Create end tag of ol element."""
        return self._create_end_tag('ol')

    def ul(self, content, attrs=None):
        """Create ul element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('ul', content, attrs)

    def start_ul(self, attrs=None):
        """Create start tag of ul element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('ul', attrs)

    def end_ul(self):
        """Create end tag of ul element."""
        return self._create_end_tag('ul')

    def li(self, content, attrs=None):
        """Create li element.

        Keyword arguments:
            content -- some text or list contains some texts
            attrs -- dict object that contains attributes (default None)
        """
        if isinstance(content, list) or isinstance(content, tuple):
            result = list()
            for li in content:
                result.append(self._create_element('li', li, attrs))
            return ''.join(result)
        else:
            return self._create_element('li', content, attrs)

    def dl(self, content, attrs=None):
        """Create dl element.

        Keyword arguments:
            content -- some text or dict contains some texts
            attrs -- dict object that contains attributes (default None)
        """
        if isinstance(content, dict):
            result = list()
            result.append(self.start_dl(attrs))
            for di in content.keys():
                result.append(self.dt(di))
                result.append(self.dd(content[di]))
            result.append(self.end_dl())
            return ''.join(result)
        else:
            return self._create_element('dl', content, attrs)

    def start_dl(self, attrs=None):
        """Create start tag of dl element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_start_tag('dl', attrs)

    def end_dl(self):
        """Create end tag of p element."""
        return self._create_end_tag('dl')

    def dt(self, content, attrs=None):
        """Create dt element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('dt', content, attrs)

    def dd(self, content, attrs=None):
        """Create dd element.

        Keyword arguments:
            content -- some text
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_element('dd', content, attrs)

    # empty

    def br(self, attrs=None):
        """Create br element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_empty_element('br', attrs)

    def hr(self, attrs=None):
        """Create hr element.

        Keyword arguments:
            attrs -- dict object that contains attributes (default None)
        """
        return self._create_empty_element('hr', attrs)

    # form elements

    def start_form(self, method=None, action=None, enctype=None, attrs=None):
        """Create start tag of form element.

        Keyword arguments:
            method -- method attribute (default None)
            action -- action attribute (default None)
            enctype -- enctype attirbute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        if method is None:
            attrs['method'] = 'POST'
        else:
            attrs['method'] = method
        if action is None:
            attrs['action'] = os.environ.get('SCRIPT_NAME', '')
        else:
            attrs['action'] = action
        if enctype is not None:
            attrs['enctype'] = enctype
        return self._create_start_tag('form', attrs)

    def start_multipart_form(self, method=None, action=None,
                             enctype='multipart/form-data', attrs=None):
        """Create start tag of form element for multipart.

        Keyword arguments:
            method -- method attribute (default None)
            action -- action attribute (default None)
            enctype -- enctype attirbute (default 'multipart/form-data')
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        if method is None:
            attrs['method'] = 'POST'
        else:
            attrs['method'] = method
        if action is None:
            attrs['action'] = os.environ.get('SCRIPT_NAME', '')
        else:
            attrs['action'] = action
        if enctype is not None:
            attrs['enctype'] = enctype
        return self._create_start_tag('form', attrs)

    def end_form(self):
        """Create end tag of form element."""
        return self._create_end_tag('form')

    def textfield(self, name=None, value=None, size=None, maxlength=None,
                  attrs=None):
        """Create input element as form item text field.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            size -- size attribute (default None)
            maxlength -- maxlength attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        attrs['size'] = size
        attrs['maxlength'] = maxlength
        return self.input('text', attrs)

    def textarea(self, name=None, value=None, rows=None, columns=None,
                 attrs=None):
        """Create textarea element.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            rows -- rows attribute (default None)
            columns -- cols attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['rows'] = rows
        attrs['cols'] = columns
        if value is None:
            value = ''
        return self._create_element('textarea', value, attrs)

    def password_field(self, name=None, value=None, size=None,
                       maxlength=None, attrs=None):
        """Create input element as form item password field.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            size -- size attribute (default None)
            maxlength -- maxlength attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        attrs['size'] = size
        attrs['maxlength'] = maxlength
        return self.input('password', attrs)

    def filefield(self, name=None, value=None, size=None, maxlength=None,
                  attrs=None):
        """Create input element as form item file field.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            size -- size attribute (default None)
            maxlength -- maxlength attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        attrs['size'] = size
        attrs['maxlength'] = maxlength
        return self.input('file', attrs)

    def popup_menu(self, name=None, values=None, default=None,
                   labels=None, attributes=None, attrs=None):
        """Create select element as form item popup menu.

        Keyword arguments:
            name -- name attribute (default None)
            values -- list object that contains values (default None)
            default -- default value (default None)
            labels -- dict object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            attrs -- dict object that contains attributes (default None)
        """
        return self.select_list(name=name, values=values, default=default,
                                labels=labels, attributes=attributes,
                                attrs=attrs)

    def scrolling_list(self, name=None, values=None, default=None,
                       size=4, multiple=False,
                       labels=None, attributes=None, attrs=None):
        """Create select element as form item scrolling list.

        Keyword arguments:
            name -- name attribute (default None)
            value -- list object that contains values (default None)
            default -- default value (default None)
            size -- size attribute (default 4)
            multiple -- multiple attribute (default False)
            labels -- dict object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            attrs -- dict object that contains attributes (default None)
        """
        return self.select_list(name=name, values=values, default=default,
                                labels=labels, attributes=attributes,
                                size=size, multiple=multiple, attrs=attrs)
        
    def select_list(self, name=None, values=None, default=None,
                    labels=None, attributes=None, size=None, multiple=False,
                    attrs=None):

        """Create select element.

        Keyword arguments:
            name -- name attribute (default None)
            values -- list object that contains values (default None)
            default -- default value (default None)
            labels -- dict object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            size -- size attribute (default None)
            multiple -- multiple attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """

        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError('need list, got %r' % type(values))
        if labels is not None and not isinstance(labels, dict):
            raise TypeError('need dict, got %r' % type(labels))
        if attributes is not None and not isinstance(attributes, dict):
            raise TypeError('need dict, got %r' % type(attributes))
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        if isinstance(size, int):
            attrs['size'] = size
        if multiple:
            attrs['multiple'] = 'multiple'
        result = self._create_start_tag('select', attrs)
        for li in values:
            attrs = {}
            if attributes is not None:
                if li in attributes:
                    if isinstance(attributes[li], dict):
                        attrs = attributes[li]
            attrs['value'] = li

            if isinstance(default, list) or isinstance(default, tuple):
                for item in default:
                    if item == li:
                        attrs['selected'] = 'selected'
            else:
                if default == li:
                    attrs['selected'] = 'selected'

            content = li
            if labels is not None:
                if li in labels:
                    if labels[li] is not None:
                        content = labels[li]
            result += self._create_element('option', content, attrs)
        result += self._create_end_tag('select')
        return result

    def checkbox_group(self, name=None, values=None, default=None,
                       delimiter=None,labels=None, attributes=None,
                       attrs=None):
        """Create input elements as form item check box group.

        Keyword arguments:
            name -- name attribute (default None)
            values -- list object that contains values (default None)
            default -- default value (default None)
            delimiter -- delimiter for input elements. if it is None,
                         return list object contains input elements
                         (default None)
            labels -- list object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            attrs -- dict object that contains attributes (default None)
        """
        return self.button_group(type='checkbox', name=name,values=values,
                                 default=default, delimiter=delimiter,
                                 labels=labels, attributes=attributes,
                                 attrs=attrs)

    def checkbox(self, name=None, checked=False, value=None, label='',
                 attrs=None):
        """Create input element as form item check box group.

        Keyword arguments:
            name -- name attribute (default None)
            checked -- checked attribute (default False)
            value -- value attribute (default None)
            label -- label text (default '')
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        if checked:
            attrs['checked'] = checked
        attrs['value'] = value
        result = []
        result.append(self.input('checkbox', attrs))
        if len(label) == 0:
            label = value
        if isinstance(label, int):
            label = str(int)
        if label is not None:
            result.append(label)
        return ' '.join(result)

    def radio_group(self, name=None, values=None, default=None,
                     delimiter=None,labels=None, attributes=None, attrs=None):
        """Create input elements as form item radio button group.

        Keyword arguments:
            name -- name attribute (default None)
            values -- list object that contains values (default None)
            default -- default value (default None)
            delimiter -- delimiter for input elements. if it is None,
                         return list object contains input elements
                         (default None)
            labels -- list object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if isinstance(default, list) or isinstance(default, tuple):
            default = default[0]
        return self.button_group(type='radio', name=name,values=values,
                                 default=default, delimiter=delimiter,
                                 labels=labels, attributes=attributes,
                                 attrs=attrs)

    def button_group(self, type='radio', name=None, values=None,
                     default=None, delimiter=None,labels=None,
                     attributes=None, attrs=None):

        """Create input elements.

        Keyword arguments:
            type -- type attribute (default 'radio')
            name -- name attribute (default None)
            values -- list object that contains values (default None)
            default -- default value (default None)
            delimiter -- delimiter for button elements. if it is None,
                         return list object contains button elements
                         (default None)
            labels -- list object that contains label text (default None)
            attributes -- dict object that contains attributes for each item
                          (default None)
            attrs -- dict object that contains attributes (default None)
        """

        if not isinstance(values, list):
            raise TypeError('need list, got %r' % type(values))
        if labels is not None and not isinstance(labels, dict):
            raise TypeError('need dict, got %r' % type(labels))
        if attributes is not None and not isinstance(attributes, dict):
            raise TypeError('need dict, got %r' % type(attributes))

        result = []
        for li in values:
            iattrs = {}
            if attrs is not None or isinstance(attrs, dict):
                iattrs.update(attrs)
            if attributes is not None:
                if li in attributes:
                    if isinstance(attributes[li], dict):
                        iattrs.update(attributes[li])
            iattrs['name'] = name
            iattrs['value'] = li

            if isinstance(default, list):
                for item in default:
                    if item == li:
                        iattrs['checked'] = 'checked'
            else:
                if default == li:
                    iattrs['checked'] = 'checked'

            content = li
            if labels is not None:
                if li in labels:
                    if labels[li] is not None:
                        content = labels[li]
            if isinstance(content, int):
                content = str(content)
            result.append('{0} {1}'.format(self.input(type, iattrs), content))
        if delimiter is not None and isinstance(delimiter, str):
            result = delimiter.join(result)
        return result
        

    def submit(self, name=None, value=None, attrs=None):
        """Create input element as form item submit button.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        return self.input('submit', attrs)

    def reset(self, name=None, value=None, attrs=None):
        """Create input element as form item reset button.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        return self.input('reset', attrs)

    def button(self, name=None, value=None, attrs=None):
        """Create input element as form item button.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        return self.input('button', attrs)

    def hidden(self, name=None, value=None, attrs=None):
        """Create input element as form item hidden.

        Keyword arguments:
            name -- name attribute (default None)
            value -- value attribute (default None)
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['name'] = name
        attrs['value'] = value
        return self.input('hidden', attrs)

    def input(self, type, attrs=None):
        """Create input element.

        Keyword arguments:
            type -- type attribute
            attrs -- dict object that contains attributes (default None)
        """
        if attrs is None or not isinstance(attrs, dict):
            attrs = {}
        attrs['type'] = type
        return self._create_empty_element('input', attrs)


    def formitem(self, value, attrs=None):
        return self._create_element('input', value, attrs)

    # internal methods

    def _create_start_tag(self, elemname, attrs=None):
        return '<{0}{1}>'.format(elemname, self._create_attr_string(attrs))

    def _create_end_tag(self, elemname):
        return '</{0}>'.format(elemname)

    def _create_attr_string(self, attrs):
        attrstr = ''
        if isinstance(attrs, dict):
            for attrname in (attrs.keys()):
                if attrs[attrname] is not None:
                    attrvalue = attrs[attrname]
                    if isinstance(attrvalue, int):
                        attrvalue = str(attrvalue)
                    attrstr = '{0} {1}="{2}"'.format(
                        attrstr,
                        html.escape(attrname, True),
                        html.escape(attrvalue, True))
        return attrstr

    def _create_element(self, elemname, content, attrs=None):
        starttag = self._create_start_tag(elemname, attrs)
        endtag = self._create_end_tag(elemname)
        if isinstance(content, int):
            content = str(content)
        if isinstance(content, str):
            return '{0}{1}{2}'.format(starttag, content, endtag)
        else:
            raise TypeError('need string or int, got %r' % type(content))
        
    def _create_empty_element(self, elemname, attrs=None):
        return '<{0}{1} />'.format(elemname, self._create_attr_string(attrs))
