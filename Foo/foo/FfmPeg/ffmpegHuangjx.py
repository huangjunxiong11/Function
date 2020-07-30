import os


class HjxFfmpeg(object):
    """
    这个类需要系统提前安装好ffmpeg，具体安装方法可以参见：https://blog.csdn.net/my_name_is_learn/article/details/107408551
    """

    def __init__(self):
        pass

    def img_become_mp4(self, img, mp4, fps=24, duration=5):
        """
        将一张图片变成一个视频
        :param img: 图片路径
        :param mp4: 输出视频路径
        :param fps: 输出视频帧数
        :param duration: 输出视频时间
        :return: 成功返回True, 失败返回False
        """
        try:
            cmd = 'ffmpeg -r {} -f image2 -loop 1 -i {} -pix_fmt yuvj420p -t {} -vcodec mpeg4 {} -y'.format(fps, img,
                                                                                                            duration,
                                                                                                            mp4)
            os.system(cmd)
            return True
        except:
            return False

    def transitions(self, input1, input2, offset, duration, output, classnumble=0):
        """
        :param input1: 第一个输入视频
        :param input2: 第二个输入视频
        :param classnumble: 转场特效编号，0～31
        :param offset: 转场效果起始时间，时间必须小于第一个视频的持续时间
        :param duration: 转场效果持续时间
        :param output: 输出视频
        :return:  成功返回True, 失败返回False
        """
        # 种类效果可在这里查看：http://trac.ffmpeg.org/wiki/Xfade?version=5
        classtransitions = ['fade', 'fadeblack', 'fadewhite', 'distance', 'wipeleft', 'wiperight', 'wipeup', 'wipedown',
                            'slideleft', 'slideright', 'slideup', 'slidedown', 'smoothleft', 'smoothright', 'smoothup',
                            'smoothdown', 'rectcrop', 'circlecrop', 'circleclose', 'circleopen', 'horzclose',
                            'horzopen',
                            'vertclose', 'vertopen', 'diagbl', 'diagbr', 'diagtl', 'diagtr', 'dissolve',
                            'pixelize', 'radial'
                            ]
        classtransition = classtransitions[classnumble]

        try:
            cmd = 'ffmpeg -i {} -i {} -filter_complex xfade=transition={}:duration={}:offset={} {} -y'.format(
                input1, input2, classtransition, duration, offset, output
            )
            os.system(cmd)
            return True
        except:
            return False

    def cut_duration(self, input, output, start, end):
        """
        裁剪视频时间
        :param input: 输入视频
        :param output: 输出视频
        :param start: 开始时间，例如：00:00:00
        :param end: 结束时间， 例如：00:00:05， 五秒
        :return: 成功返回True, 失败返回False
        """
        try:
            cmd = 'ffmpeg -ss {} -t {} -i {} -vcodec copy -acodec copy  {} -y'.format(
                start, end, input, output
            )
            os.system(cmd)
            return True
        except:
            return False

    def get_audio(self, mp4, wav):
        """
        提取📛mp4中的音频
        :param mp4: 视频，例如：input.mp4
        :param wav: 音频， 例如：out.wav
        :return: 成功返回True, 失败返回False
        """
        try:
            cmd = 'ffmpeg -i {} -vn -y -acodec pcm_s16le {}'.format(
                mp4, wav
            )
            os.system(cmd)
            return True
        except:
            return False

    def add_audio(self, wav, imp4, omp4):
        """
        给视频增加音频
        :param wav: 音频
        :param imp4: 输入视频
        :param omp4: 输出视频
        :return: 成功返回True, 失败返回False
        """
        try:
            cmd = "ffmpeg -i {} -i {} -y {} ".format(wav, imp4, omp4)
            os.system(cmd)
            return True
        except:
            return False


if __name__ == '__main__':
    hjxffmpeg = HjxFfmpeg()
    hjxffmpeg.cut_duration('/home/huangjx/Share/5miao1.mp4', "/home/huangjx/Share/2miao.mp4", "00:00:00", "00:00:02")
