import base64
import os

import filetype

from res.icon import *


def get_icon_filetype(path: str):
    """获取路径对应的文件类型图标"""
    if not os.path.exists(path):
        return base64.b64decode(warning_base64)
    elif os.path.isdir(path):
        return base64.b64decode(folder_base64)
    elif filetype.is_image(path):
        return base64.b64decode(image_base64)
    elif filetype.is_document(path):
        return base64.b64decode(office_base64)
    elif filetype.is_archive(path):
        return base64.b64decode(archive_base64)
    elif filetype.is_video(path):
        return base64.b64decode(video_base64)
    elif filetype.is_audio(path):
        return base64.b64decode(audio_base64)
    else:
        return base64.b64decode(unknown_base64)


def get_filename(path: str):
    """获取路径对应的文件名"""
    return os.path.basename(path)
