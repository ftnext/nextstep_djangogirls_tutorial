from django import template


register = template.Library()


@register.filter(is_safe=True)
def parse_keyword(querydict):
    """GETのクエリパラメタを渡してkeyword(検索語句)を取り出す"""
    keyword = querydict.get('keyword')
    return keyword if keyword else ''


@register.simple_tag
def query_replace(request, field, value):
    """GETのクエリ文字列にパラメタfieldと値valueを追加する"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
