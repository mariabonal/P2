import subprocess
from histogram import yuv_histogram
from resize import resized
from change_audio import stereo_mono


def questions():
    question = input("Would you like to run any other exercise (y/n)? ")
    if question == 'y':
        ex = input("Which exercise do you want to run? ")
        print("You entered:" + ex)
        ex = int(ex)
        c = 1
    else:
        c = 0
        ex = 0
    return ex, c


exercise_number = input("Which exercise do you want to run? ")
print("You entered:" + exercise_number)
exercise_number = int(exercise_number)
count = 1
while count != 0:
    # exercise 1
    if exercise_number == 1:
        def cut_video(n):
            subprocess.call(['ffmpeg', '-ss', '00:00:00.0', '-i', 'BBB.mp4', '-c', 'copy', '-t', n, 'output.mp4'])


        N = input("How many second do you want to cut the video? Please enter it such as 00:00:12 for 12 seconds: ")
        print("You entered: " + N)
        cut_video(N)
        exercise_number, count = questions()

    # exercise 2
    elif exercise_number == 2:
        yuv_histogram()
        exercise_number, count = questions()

    # exercise 3
    elif exercise_number == 3:
        resized()
        exercise_number, count = questions()

    # exercise 4
    elif exercise_number == 4:
        stereo_mono()
        exercise_number, count = questions()

    else:
        print("This number is not valid, try again")
        exercise_number = input("Which exercise do you want to run? ")
        print("You entered:" + exercise_number)
        exercise_number = int(exercise_number)
