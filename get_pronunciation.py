from urllib import request, parse
from bs4 import BeautifulSoup

def is_polyphone(text, chk):
    if bool(chk):
        return text
    t = ''
    for v, char in enumerate(text):
        c = parse.quote(char)
        url = f'https://hanyu.baidu.com/zici/s?from=aladdin&query={c}&smp_names=&smpid=&srcid=51368&wd={c}'
        html = get_html(url)
        b_list = find_pinyin(html, 'pinyin')
        if len(b_list) > 1:
            a = -1
            while a >= len(b_list) or a < 0:
                p = f'第{v + 1}个字符“{char}”是多音字，请选择读音：\n'
                for i, b in enumerate(b_list):
                    p += f'{i + 1}. {b}\n'
                a = input(p)
                while not a.isdigit():
                    a = input('请输入正确的数字：')
                a = int(a)
                a -= 1
            t += b_list[a]
            t += ' '
        else:
            t += char
    return t

def get_html(url):
    try:
        response = request.urlopen(url)
        result = response.read().decode('utf-8')
        return result
    except Exception as e:
        return None

def find_pinyin(html, element_id):
    b_list = []
    soup = BeautifulSoup(html, 'html.parser')
    pinyin_div = soup.find(id = element_id)
    if pinyin_div:
        b_tags = pinyin_div.find_all('b')
        for b_tag in b_tags:
            b_list.append(b_tag.get_text())
    return b_list