from moviepy.editor import *
import moviepy.video.fx.all as vfx

def video_clip_add_subtitle():
    video = VideoFileClip("res/沙雕视频.mp4").subclip(5,20)

    # 定义中文字幕， 中文需要指定中文字体
    txt_clip = ( TextClip("Hello world! 你好世界",fontsize=70,color='white', font="free_font/站酷仓耳渔阳体-W01.ttf")
                .set_position(lambda t: ("center", 100 + t*5)) # 会动的字幕， x轴固定center， Y轴变。 t是时间
                # .set_position('center')  # 居中、固定位置的字幕
                .set_duration(10) )

    result = CompositeVideoClip([video, txt_clip]) # 在视频上添加字幕
    result.write_videofile("output/add_subtitle.mp4",fps=25) 
    concatenate_videoclips

def overlay_img_or_video():
    video = VideoFileClip("res/沙雕视频.mp4")
    # img = ImageClip("girl.jpg").set_duration(5).set_position((10,50)).resize(newsize=(200,300)).set_start(2)
    img = VideoFileClip("yman2.mp4").subclip(10).set_duration(5).set_position((10,50)).resize(newsize=(200,300)).set_start(2)

    output = CompositeVideoClip([video, img])   # 在视频上叠加视频或者图片
    output.write_videofile("output/add_v.mp4")
                                
    
def change_or_get_audio():
    video = VideoFileClip("res/沙雕视频.mp4")
    audio_of_video = video.audio     # 提取mp4的音频
    audio_of_video.write_audiofile("output/提取mp4的音频.mp3")

    new_audio = AudioFileClip("res/听闻远方有你_刘德华.mp3")
    new_video = video.set_audio(new_audio)   # 修改视频的音频
    # new_video.volumex(2)
    new_video.write_videofile("output/new_audio.mp4")

def vfx_fx():   # vfx 处理视频特效，  fx 处理音频特效
    video = VideoFileClip("res/沙雕视频.mp4")
    color_adjust_video = video.fx(vfx.colorx, 1.5)   # 视频颜色调亮
    color_adjust_video.write_videofile("output/color_adjust.mp4")

change_or_get_audio()