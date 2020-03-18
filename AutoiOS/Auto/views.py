from django.shortcuts import render,HttpResponse
from Auto import models
import cv2,os
import numpy as np
# Create your views here.
import uuid
def peras(r,uid):
    # img=cv2.imread(r)[970+1:1474-1,100+1:977-1]
    
    img = cv2.imdecode(np.frombuffer(r, np.uint8), cv2.IMREAD_COLOR)[970+1:1474-1,100+1:977-1]
    edge_output = cv2.Canny(img, 0,700)
    #print(edge_output.shape)
    nt=edge_output[180][661]
    #print(nt)
    #print(type(nt))
    flg=0
    for y in range(edge_output.shape[0]):
        if flg==1:break
        for x in range(300,edge_output.shape[1]):
            #print(x,y)
            #img[y][x]=np.array([0,0,255])
            if edge_output[y][x]==255:#找到黑色像素点
                n=0
                for o in range(112):#向下直线寻找
                    if edge_output[y+o][x]==255:
                        n+=1
                        #cv2.circle(img, (x,y+o),5,(0, 255,0), 3)
                if n>40:#大概是直线
                    print(n)
                    if x-96 <600:
                        print(f"距离：{x-96}")
                        
                        
                        cv2.imwrite(f"upload\icons\{uid}0.jpg",img)

                        cv2.circle(img, (x+56,y+56),20,(255, 0,0),20)#红点
                        cv2.circle(img, (96+56,y+56),20,(0, 0,255), 20)#蓝点
                        cv2.imwrite(f"upload\icons\{uid}1.jpg",img)
                        #print(x,y)
                        flg=1
                        break
    return x-96                 




def index(request):
    if request.method == 'GET':
        return render(request,'Auto/index.html')
    
    if request.method == 'POST':
        COM = request.POST.get('COM')
        file_obj = request.FILES.get('file')
        #print(file_obj.read())
        uid = str(uuid.uuid4())
        len=peras(file_obj.read(),uid)
        models.AutoiOS.objects.create(
            COM = COM,
            photo = f"icons\{uid}0.jpg",
            Conphoto =f"icons\{uid}1.jpg",
            ConLen=len,
        )


        return HttpResponse(str(len))

        