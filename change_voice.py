import soundfile as sf
import sounddevice as sd
from asyncio import get_event_loop_policy, new_event_loop, set_event_loop
from edge_tts import Communicate
from initialize_file import initialize_dir

async def amain(text, voice, file) -> None:
    communicate = Communicate(text, voice)
    await communicate.save(file)

def change_voice(text, voice, file):
    initialize_dir(file[: file.find('/')])
    loop = new_event_loop()
    set_event_loop(loop)
    try:
        loop.run_until_complete(amain(text, voice, file))
    finally:
        loop.close()

def print_voice(file):
    data, fs = sf.read(file)
    sd.play(data, fs)
    sd.wait()