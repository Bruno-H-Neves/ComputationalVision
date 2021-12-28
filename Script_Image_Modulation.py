import PySimpleGUI as sg
import cv2 as cv
import numpy as np

def FrameTitle(img,Title):
    return  cv.putText(img,Title,(1,10),cv.FONT_HERSHEY_COMPLEX,0.45,(255,255,255),1)


def main():
    filename = sg.popup_get_file('Search File   CANCEL FOR CHOSE WEBCAM ')
    if filename is None:
        vidFile = cv.VideoCapture(0)
        num_frames=0
    else:
        vidFile = cv.VideoCapture(filename)
        num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
        fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.theme('DarkGrey7’')

    menu_def = [['&File', ['E&xit',]],
                ['&Help',['&Help','&About Us']]]

    column1 = [ [ sg.Text('FILTER_TYPE', background_color='blue', justification='center', size=(20, 1))],
                [ sg.Spin(values=('Gaussian', 'Conv2D', 'Blur','Median','bilateral','sep2D','Sobel'), initial_value='LBF', size=(20, 1))],
                [ sg.Spin(values=('Laplacian', 'Edge'), initial_value='HBF', size=(20, 1))],
                [ sg.Spin(values=('Dilate', 'Erode'), initial_value='Morphologic', size=(20, 1))],
                [sg.Frame(layout=[
                [sg.Radio('RGB     ', "RADIO1", key='-rgb-', default=True, size=(5,1)), sg.Radio('GRAY', "RADIO1",key='-gray-', size=(5,1))],
                [sg.Radio('LBF     ', "RADIO1",key='-lbf-', size=(5,1)), sg.Radio('HBF', "RADIO1",key='-hbf-', size=(5,1))]
                ],title='Select Viewer',title_color='red', tooltip="left")]]

    layout = [[sg.Menu(menu_def, tearoff=True)],
              [ sg.Slider(range=(0, num_frames),size=(53, 10), orientation='h', key='-slider-'),
                sg.Button('Exit', size=(7, 1), font='Helvetica 14')],
              [ sg.Image(filename='', key='-image1-'),
                sg.Image(filename='', key='-image2-'),sg.Column(column1, background_color='lightblue')],
              [ sg.Image(filename='', key='-image3-'), 
                sg.Image(filename='',key='-image4-'),sg.Image(filename='', key='-image5-')]]


    ret, frame = vidFile.read()
    #print(frame.shape)
    scale=frame.shape[0]/frame.shape[1]
    nb=int(frame.shape[1]/2)
    frame = cv.resize(frame,(nb,int(nb*scale))) 
    nb2=nb*1.5
    cur_frame = 0
    size_row=int(3.2*nb)
    size_col=int(0.7*size_row)
#size=(1080,600)
    window = sg.Window('Frame', layout, no_titlebar=True, location=(40,40),size=(size_row,size_col))
    image_elem1 = window['-image1-']
    image_elem2 = window['-image2-']
    image_elem3 = window['-image3-']
    image_elem4 = window['-image4-']
    image_elem5 = window['-image5-']
    slider_elem = window['-slider-']

    ret, frame = vidFile.read()
    #print(frame.shape)
    scale=frame.shape[0]/frame.shape[1]
    nb=280
    frame = cv.resize(frame,(nb,int(nb*scale))) 
    nb2=nb*1.5
    cur_frame = 0
    while vidFile.isOpened():
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break
        ret, frame = vidFile.read()
        frame = cv.resize(frame,(nb,int(nb*scale))) 
        if not ret:  
            break
        if int(values['-slider-']) != cur_frame-1:
            cur_frame = int(values['-slider-'])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
        slider_elem.update(cur_frame)
        cur_frame += 1
        frameRGB=frame.copy()
        text_lbf=''
        frameRGB_Tl = FrameTitle(frameRGB,'RGB')
        frameGray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        frameLBF = cv.GaussianBlur(frameGray,(3,3),2)
        if values[1]== 'Gaussian':
            frameLBF = cv.GaussianBlur(frameGray,(3,3),2)
            text_lbf=" LBF: Gaussian Blur"
        if values[1]== 'Conv2D':
            frameLBF = cv.sepFilter2D(frameGray,ddepth=2,kernelX=15,kernelY=5)
            text_lbf=" LBF: SepFilter2D"
        if values[1]==  'Blur':
            frameLBF = cv.blur(frameGray,(5,5))
            text_lbf=" LBF: Blur"
        if values[1]== 'Median':
            frameLBF = cv.medianBlur(frameGray,5)
            text_lbf=" LBF: Median Blur"
        if values[1]== 'bilateral':
            frameLBF = cv.bilateralFilter(frameGray,9,75,75) 
            text_lbf=" LBF: Bilateral"
        if values[1]== 'sep2D':
            kernel = np.ones((5,5),np.float32)/25
            frameLBF = cv.filter2D(frameGray,-1,kernel)
            text_lbf=" LBF: Filter 2D"
        if values[1]== 'Sobel':
            frameLBF = cv.Sobel(frameGray,ksize=5,dx=3,dy=3,ddepth=-1)
            text_lbf=" LBF: Sobel"
        frameHBF = cv.Canny(frameGray,100,200) 
        frameGray_Tl = FrameTitle(frameGray,'Gray')
        frameLBF_Tl = FrameTitle( frameLBF,text_lbf)
        frameHBF_Tl = FrameTitle(frameHBF,'HBF')
        framezoom=frameRGB_Tl
        if values['-rgb-']== True:
            framezoom=frameRGB_Tl
        if values['-gray-']== True:
            framezoom=frameGray_Tl
        if values['-lbf-']== True:
            framezoom=frameLBF_Tl
        if values['-hbf-']== True:
            framezoom=frameHBF_Tl
        imgbytes = cv.imencode('.png', frameRGB_Tl)[1].tobytes()  
        imgbytes2 = cv.imencode('.png', frameGray_Tl)[1].tobytes() 
        imgbytes3 = cv.imencode('.png', frameLBF_Tl)[1].tobytes() 
        imgbytes4 = cv.imencode('.png', frameHBF_Tl)[1].tobytes() 
        imgbytes5 = cv.imencode('.png', cv.resize(framezoom,(int(nb2),int(nb2*scale))))[1].tobytes() 
        
        image_elem1.update(data=imgbytes)
        image_elem2.update(data=imgbytes2)
        image_elem3.update(data=imgbytes3)
        image_elem4.update(data=imgbytes4)   
        image_elem5.update(data=imgbytes5)   
    
#    sg.Popup('The button clicked was "{}"'.format(event),
#         'The values are', values)   

main()