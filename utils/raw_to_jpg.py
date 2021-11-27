"""
raw格式图像转jpg，大小会被压缩
"""
import rawpy
import imageio
import os


def __raw_to_jpg(raw_file_name, jpg_addr, jpg_name):
    with rawpy.imread(raw_file_name) as f:
        img = f.postprocess(
            use_camera_wb=True,  # 是否使用拍摄时的白平衡值
            use_auto_wb=False,
            exp_shift=2.5,  # 修改后光线会下降，所以需要手动提亮，线性比例的曝光偏移。可用范围从0.25（变暗2级）到8.0（变亮3级）。
        )
        imageio.imsave(f'{jpg_addr}/{jpg_name}.jpg', img)


def raw2jpg(raw_dir_addr, jpg_dir_addr):
    """
    raw格式图像转jpg，大小会被压缩
    :param raw_dir_addr: raw文件夹地址
    :param jpg_dir_addr: jpg文件夹地址
    :return:
    """
    raw_dir = os.listdir(raw_dir_addr)
    lenth = len(raw_dir)
    count = 0
    for raw_name in raw_dir:
        name, postfix = raw_name.split('.')
        __raw_to_jpg(f'{raw_dir_addr}/{raw_name}', jpg_dir_addr, name)
        count += 1
        print(f'{round(count/lenth,2)*100}%')


if __name__ == '__main__':
    raw2jpg('../ceshi_', '../ceshi3')
