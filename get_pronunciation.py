from urllib import request, parse
from bs4 import BeautifulSoup

def is_polyphone(text, chk):
    if bool(chk):
        return text
    t = ''
    for v, char in enumerate(text):
        list_ = find_pinyin_by_char(char)
        if len(list_) > 1:
            a = -1
            while a >= len(list_) or a < 0:
                p = f'第{v + 1}个字符“{char}”是多音字，请选择读音：\n'
                for i, b in enumerate(list_):
                    p += f'{i + 1}. {b}\n'
                a = input(p)
                while not a.isdigit():
                    a = input('请输入正确的数字：')
                a = int(a)
                a -= 1
            t += only_four_tones(list_[a], char)
        else:
            t += char
    return t

def find_pinyin_by_char(char):
    c = parse.quote(char)
    list_ = []
    step = 0
    while len(list_) == 0:
        match step:
            case 0:
                url = f'https://hanyu.baidu.com/zici/s?from=aladdin&query={c}&smp_names=&smpid=&srcid=51368&wd={c}'
                html = get_html(url)
                list_ = find_pinyin_by_hanyu(html, 'pinyin')
            case 1:
                url = f'https://baike.baidu.com/item/{c}'
                html = get_html(url)
                list_ = find_pinyin_by_baike(html)
            case 2:
                break
        step += 1
    return list_

def get_html(url):
    try:
        response = request.urlopen(url)
        result = response.read().decode('utf-8')
        return result
    except Exception as e:
        return None

def find_pinyin_by_baike(html):
    html = str(html)
    list_ = []
    text = html[html.find('（拼音：') :]
    text = text[: text.find('）')]
    t = ''
    for i in text:
        if i.islower():
            t += i
        elif len(t) > 0:
            list_.append(t)
            t = ''
    return list_

def find_pinyin_by_hanyu(html, element_id):
    list_ = []
    soup = BeautifulSoup(html, 'html.parser')
    pinyin_div = soup.find(id = element_id)
    if pinyin_div:
        b_tags = pinyin_div.find_all('b')
        for b_tag in b_tags:
            list_.append(b_tag.get_text())
    return list_

def only_four_tones(pinyin, char):
    for c in pinyin:
        if not c in 'abcdefghijklmnopqrstuvwxyz':
            return f'{pinyin} '
    return char