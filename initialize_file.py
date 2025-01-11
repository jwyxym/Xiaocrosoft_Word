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
    default_config = {
        "voice": "zh-CN-XiaoxiaoNeural",
        "file": "audio/audio.mp3"
    }

    if not path.exists(config_file_path):
        with open(config_file_path, 'w', encoding='utf-8') as config_file:
            dump(default_config, config_file, ensure_ascii=False, indent=4)

def initialize_list():
    url = 'http://example.com/file.txt'
    response = get(url)

    if response.status_code == 200:
        file_content = response.text