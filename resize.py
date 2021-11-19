import subprocess


def resized():
    subprocess.run('ffmpeg -i output.mp4 -vf scale=1280:720 resized_720p.mp4', shell=True)
    subprocess.run('ffmpeg -i output.mp4 -vf scale=720:480 resized_480p.mp4', shell=True)
    subprocess.run('ffmpeg -i output.mp4 -vf scale=360:240 resized_360x240.mp4', shell=True)
    subprocess.run('ffmpeg -i output.mp4 -vf scale=160:120 resized_160x120.mp4', shell=True)
