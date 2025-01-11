from os import path, remove, makedirs
from json import dump, load
from requests import get

def get_setting():
    initialize_json()
    with open('setting/config.json', 'r', encoding='utf-8') as config_file:
        config = load(config_file)
        voice = config['voice']
        file = config['file']
        return voice, file

def initialize_voice(file):
    initialize_dir('setting')
    if path.exists(file):
        remove(file)

def initialize_dir(file):
    if not path.exists(file):
        makedirs(file)

def initialize_json():
    initialize_dir('setting')
    config_file_path = 'setting/config.json'

    if not path.exists(config_file_path):
        with open(config_file_path, 'w', encoding='utf-8') as file:
            text = get_url('https://gh.llkk.cc/https://github.com/jwyxym/Xiaocrosoft_Word/blob/main/setting/config.json')
            if text == '':
                text = {
                    "voice": "zh-CN-XiaoxiaoNeural",
                    "file": "audio/audio.mp3"
                }
                dump(text, file, ensure_ascii=False, indent=4)
            else:
                file.write(text)

def initialize_list():
    text = get_url('https://gh.llkk.cc/https://github.com/jwyxym/Xiaocrosoft_Word/blob/main/setting/voice_list.txt')
    with open('setting/voice_list.txt', 'w', encoding='utf-8') as file:
        file.write(text)

def get_url(url):
    response = get(url)
    file_content = ''

    if response.status_code == 200:
        file_content = response.text
    return file_content