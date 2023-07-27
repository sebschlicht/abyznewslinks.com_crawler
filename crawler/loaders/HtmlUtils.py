# -*- coding: utf-8 -*-
import re
from w3lib.html import remove_tags

pattern_consecutive_whitespace = re.compile(r'\s{2,}')
pattern_escaped_newlines = re.compile(r'(\\r)?\\n')
pattern_newlines = re.compile(r'\r?\n')

def extract_clean_text_from_html(html):
    if html:
        relevant_characters = remove_consecutive_whitespace(remove_tags(html))
        return implode_text(remove_escaped_newlines(relevant_characters)).strip()
    else:
        return None

def remove_consecutive_whitespace(text):
    return pattern_consecutive_whitespace.sub(' ', text)

def remove_escaped_newlines(text):
    return pattern_escaped_newlines.sub('', text)

def implode_text(text):
    return pattern_newlines.sub(' ', text)
