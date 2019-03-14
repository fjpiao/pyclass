#Frame程序的配置文件
from views import *
#配置框架地址
frame_ip='0.0.0.0'
frame_port=8080
frame_address=(frame_ip,frame_port)

#网页文件路径
STATIC_DIR='./static/'

urls=[
    ('/time',show_time),
    ('/hello',say_hello)
]