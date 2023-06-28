import numpy as np
from PIL import ImageFont

from django.http import FileResponse
from moviepy.editor import ColorClip, CompositeVideoClip, TextClip

from .models import TextRequest


def get_text_size(text, font_path, font_size):
    font = ImageFont.truetype(font_path, font_size)
    return font.getsize(text)


def video_maker(request):
    FONT_SIZE = 40

    # Получаем текст из GET параметра
    text = request.GET.get('text', 'Default text')

    # Создание и сохранение нового объекта TextRequest
    text_request = TextRequest(text=text)
    text_request.save()

    font_path = '/content/testproject/scrolling_text/video_maker/cour.ttf'
    font_size = FONT_SIZE
    text_width, text_height = get_text_size(text, font_path, font_size)

    # Определение размера и цвета фона
    background = ColorClip(
        (100, 100), col=np.array([255, 105, 180])
    ).set_duration(3)

    # Создание текстового клипа
    txt_clip = TextClip(
        text, fontsize=FONT_SIZE, color='white')

    # Создание бегущей строки (изменяя позицию по горизонтали)
    txt_mov = txt_clip.set_pos(
        lambda t: (50-t * (text_width / 3), 30)
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
