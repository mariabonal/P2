import subprocess


def stereo_mono():
    subprocess.call(['ffmpeg', '-i', 'output.mp4', '-ac', '1', 'mono.wav'])


