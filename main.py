from urllib.parse import parse_qsl, urlparse

def parse_cookie(query: str) -> dict:
    query_split = query.split(";")
    if len(query_split) <= 1:
        return query
    query_dict = {}
    for i in query_split:
        split_item = i.strip()
        split_item = split_item.split('=', 1)
        if len(split_item) == 2:
            k, v = split_item
            query_dict[k] = v
    print(query_dict)
    return query_dict

if __name__ == '__main__':
    assert parse_cookie('') == ('')
    assert parse_cookie('=') == ('=')
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
    assert parse_cookie('name=John; city=Dnipro?') == {'name': 'John', 'city': 'Dnipro?'}
    assert parse_cookie('name=John;age=?8;') == {'name': 'John', 'age': '?8'}
    assert parse_cookie('name!=John=User;age=28;') == {'name!': 'John=User', 'age': '28'}
    assert parse_cookie('name=John;age= ') == {'name': 'John', 'age': ''}
    assert parse_cookie('1213=;') == {'1213': ''}
    assert parse_cookie('name=John=age=28;') == {'name': 'John=age=28'}
    assert parse_cookie('name=; John=User; age=28;') == {'name': '', 'John': 'User', 'age': '28'}
    assert parse_cookie('=; name=John;') == {'': '', 'name': 'John'}

def parse(url: str) -> dict:
    parsed_url = urlparse(url)
    q = dict(parse_qsl(parsed_url.query))
    return q

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&sex=male') == {'name': 'ferret', 'color': 'purple', 'sex': 'male'}
    assert parse('https://example.com/path/to/page?name==ferret&color=purple&') == {'name': '=ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple!') == {'name': 'ferret', 'color': 'purple!'}
    assert parse('https://example.com/path/to/page?name==ferret&') == {'name': '=ferret'}
    assert parse('http://example.com/path/to/page?name=John&123==pp') == {'name': 'John', '123': '=pp'}
    assert parse('https://example.com/path/to/page?name=ferret&?=purple') == {'name': 'ferret', '?': 'purple'}
    assert parse('https://example.com/path/to/page?name=&color=&') == {}
    assert parse('https://example.com/path/to/page?name=ferret&&&&&&&&&?=purple') == {'name': 'ferret', '?': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&?color=purple') == {'name': 'ferret', '?color': 'purple'}
    assert parse('?name=ferret&color=purple?') == {'name': 'ferret', 'color': 'purple?'}







