from easy_thumbnails.files import get_thumbnailer

from ture.models import Image
from PIL import Image as IM

def convert_images():
    # Получение всех изображений, которые нужно конвертировать
    images = Image.objects.all()
    
    for instance in images:
        path = instance.img.path
        if instance.img.path[-4:] != 'webp':
            im = IM.open(path).convert('RGB')
            extention = instance.img.path.rsplit(".", 2)[1]
            file_name = path.replace(extention, "webp")
            im.save(file_name, 'webp')
            print(im, file_name, instance.img, instance.img.path)
            print(im.name)
            instance.img = file_name
            instance.save()
            print(instance)



