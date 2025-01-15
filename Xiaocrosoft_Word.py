from change_voice import print_voice, change_voice
from initialize_file import initialize_voice, initialize_list, get_setting

def start_change(text):
    voice, file, chk = get_setting()
    initialize_voice(file)
    change_voice(text, voice, file, chk)
    print_voice(file)

if __name__ == '__main__':
    initialize_list()
    while True:
        text = input("请输入要转换的文字：")
        start_change(text)