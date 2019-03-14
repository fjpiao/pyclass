import re
p=r'\b[1-9]\d{5}(18|19|20|21|22)\d{2}(0[1-9]|10|11|12)(0[1-9]|[1-2]\d|30|31)\d{4}\b'
regex=re.compile(p)
s='shenfeng: 120104199309247618 120104199309017618 123 125 325235 '
l=regex.search(s).group()
print(l)