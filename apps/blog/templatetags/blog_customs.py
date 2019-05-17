from django import template


register = template.Library()


@register.filter(is_safe=True)
def parse_keyword(querydict):
    """GETのクエリパラメタを渡してkeyword(検索語句)を取り出す"""
    keyword = querydict.get('keyword')
    return keyword if keyword else ''
