# SZE-FordProg-2020-Liquid

Liquid accepter.

Python Lex - Yacc parser.

A liquid nyelvet fogadja el a parser (nem minden elemét a nyelvnek.)

Tokenek amiket elfogad:
    'OR',
    'AND',
    'NAME',
    'INT',
    'STRING',
    'EQUALS',
    'DECLARE',
    'NOTEQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_OR_EQUAL',
    'LESS_OR_EQUAL',
    'L_BRACKET',
    'R_BRACKET',
    'PERCENT',
    'FILTER',
    'SEMICOLON',
    'DOT',

Példa bemenetek, amiket elfogad:

{{ page.title }}

{{ "/my/fancy/url" | append: ".html" }}

{{ "adam!" | capitalize | prepend: "Hello " }}

{% if product.title == "Awesome Shoes" %}

{% if product.title contains "Pack" %}

Számolni nem számol, a parser csak eldönti, hogy elfogadja-e az inputot helyes nyelvtanként.
