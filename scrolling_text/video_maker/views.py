from django.http import FileResponse
from moviepy.config import change_settings
from moviepy.editor import ColorClip, CompositeVideoClip, TextClip
import numpy as np

from .conf import IMAGEMAGICK_BINARY
from .models import TextRequest


change_settings({"IMAGEMAGICK_BINARY": IMAGEMAGICK_BINARY})


def video_maker(request):
    FONT_SIZE = 40

    # Получаем текст из GET параметра
    text = request.GET.get('text', 'Default text')

    # Создание и сохранение нового объекта TextRequest
    text_request = TextRequest(text=text)
    text_request.save()

    # Определение размера и цвета фона
    background = ColorClip(
        (100, 100), col=np.array([255, 105, 180])
    ).set_duration(3)

    # Создание текстового клипа
    txt_clip = TextClip(
        text, fontsize=FONT_SIZE, color='white')

    # Создание бегущей строки (изменяя позицию по горизонтали)
    txt_mov = txt_clip.set_pos(
        lambda t: (-t * (len(text) * (FONT_SIZE / 2) / 3), 30)
    ).set_duration(3)

    # Задаем имя файлу
    filename = 'scrolling_text.mp4'

    # Объединение текстового клипа и фона в одно видео
    final = CompositeVideoClip([background, txt_mov])

    # Преобразование исходного видеоклипа в 3s клип и сохранение его в файл
    final.set_duration(3).write_videofile(
        filename, fps=24, codec='libx264'
    )

    # Отправление видео в качестве HTTP-ответа
    response = FileResponse(open(filename, 'rb'))
    content_disposition = 'attachment; filename="{}"'.format(filename)
    response['Content-Disposition'] = content_disposition
    return response
