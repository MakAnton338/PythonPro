from urllib.parse import parse_qsl, urlparse

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


def parse_cookie(query: str) -> dict:
    return {}

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}








