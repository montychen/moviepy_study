from moviepy.editor import *
import moviepy.video.fx.all as vfx

def video_clip_add_subtitle():
    video = VideoFileClip("res/沙雕视频.mp4").subclip(5,20)  # 截取视频的 第5-20秒

    # 中文字幕需要指定中文字体
    txt_clip = ( TextClip("Hello world! 你好世界",fontsize=70,color='white', font="free_font/站酷仓耳渔阳体-W01.ttf")
                .set_position(lambda t: ("center", 100 + t*5)) # 会动的字幕， x轴固定center， Y轴变。 t是时间
                # .set_position('center')  # 居中、固定位置的字幕
                .set_duration(10) )

    result = CompositeVideoClip([video, txt_clip]) # 在视频上添加字幕
    result.write_videofile("output/add_subtitle.mp4",fps=25)


def overlay_img_or_video():
    video = VideoFileClip("res/沙雕视频.mp4")

    # 在指定位置 、 指定大小，加入字幕
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

def color_adjust():   # vfx 处理特效，  fx 处理音频特效
    video = VideoFileClip("res/沙雕视频.mp4")
    bright_color_video = video.fx(vfx.colorx, 1.5)   # 视频颜色调亮
    contrasted_color_video = video.fx(vfx.lum_contrast, 1.5)   # 提高对比度

    bright_color_video.write_videofile("output/bright_color.mp4")
    contrasted_color_video.write_videofile("output/contrasted_color.mp4")

def fadeout_fadein(): # 拼接的2个视频间的转场， 淡入、淡出
    video1 = VideoFileClip("res/沙雕视频.mp4").subclip(4,14) # 宽高 1280×720
    video2 = VideoFileClip("res/超时空交易.mp4").subclip(12,22) # 宽高是 768*576
    video1 = video1.resize((768, 576)) # 宽高调整成 

    video1 = video1.crossfadeout(1)  # 淡出
    video2 = video2.crossfadein(1)   # 淡入

    output_video = concatenate_videoclips([video1, video2], method='compose') # 拼接视频

    output_video.write_videofile("output/fadeout_fadein.mp4")

def mirror_x():  # 水平镜像翻转
    video = VideoFileClip("res/沙雕视频.mp4").subclip(5,15)
    mirror_x_video = video.fx(vfx.mirror_x)
    mirror_x_video.write_videofile("output/mirror_x.mp4")

def save_frame(): # 精准的截取视频画面（FFmepg无法做到的事）
    video = VideoFileClip("res/超时空交易.mp4")
    video.save_frame("output/截取第13秒的画面.png", t=13)  # t 是指定截取第几秒的画面

save_frame()
