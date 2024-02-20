#!/usr/bin/env python
# coding: utf-8

# In[4]:


import subprocess

def play_sound(file_path):
    try:
        # 'aplay' 명령어를 사용하여 오디오 파일 재생
        subprocess.run(['aplay', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    # 재생할 오디오 파일 경로
    audio_file_path = 'sound.wav'
    play_sound(audio_file_path)
    


# In[ ]:




