#!/usr/bin/env python
"""kevin_lizarazo_2-3.py -- find and replace text"""

sample_text = """And since you know you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of."""
print sample_text; print

search_query = raw_input('please enter the text you wish to find: ')
search_hits = sample_text.count(search_query)
text_to_insert = raw_input('please enter the text you want to insert: ')
replaced_text = sample_text.replace(search_query, text_to_insert)

print; print replaced_text

print; print "'{}' search hits: {}".format(search_query, search_hits)