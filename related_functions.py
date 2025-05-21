import re

def extract_video_id(url: str) -> str:
    """
    Извлекает ID видео из URL YouTube.
    Поддерживает форматы:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - и другие похожие

    :param url: URL видео на YouTube
    :return: ID видео или None, если не найден
    """
    # Паттерны для поиска ID
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11})',  # v=VIDEO_ID или /VIDEO_ID
        r'youtu\.be\/([0-9A-Za-z_-]{11})',  # короткий URL
        r'embed\/([0-9A-Za-z_-]{11})'  # embed URL
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None