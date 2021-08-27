import cv2 as cv

# rescalling frames
def rescale(frame, scale=1):
    heigth = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = ( width, heigth)

    return cv.resize(frame, dimension)

# Importing the video file
vid = cv.VideoCapture(r"../Video/sampleVideo.mp4")

# asking user if they want to scale file
wantToScale = input("Hit 1 if you want to scale the file otherwise 0 : ")

if wantToScale == '1':
    scale = float(input("Enter scale, if dont want to scale just hit 1 : "))
else:
    scale = 1

frame_width = int(vid.get(3)*scale)
frame_height = int(vid.get(4)*scale)
size = (frame_width, frame_height)
out = cv.VideoWriter('../Video/outputGrey.avi', cv.VideoWriter_fourcc(*"MJPG"), vid.get(cv.CAP_PROP_FPS), size, 0)
total = int(vid.get(cv.CAP_PROP_FRAME_COUNT))
print(total)
num = 1
one = int(total/100)

while(1):
    if num == one:
        num = 1
        print("#", end='')
    check, frame = vid.read()
    if not check:
        break
    frame = rescale(frame, scale)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    num += 1

vid.release()
out.release()

print("\nProcessing Complete!")