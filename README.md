# Smart Screen

![alt text](https://avatars3.githubusercontent.com/u/5009934?s=400&v=4)

This little script will detect your face and if there is no face detected then it will bring up screen saver, and again if your face is detected it will show you screen.

## How do I use it?

Run below script to install required libraries:

     pip install -r requirements.txt
    
To run the script:

    python opencv.py
     
## What's it doing?

The script is using OpenCV's haarcascade_frontalface to detect face and if it doesn’t find any face it will show screensaver using applescript, during screensaver script will be still running and will wait for face to detect. After detecting script will press space key by using Pynput library.
