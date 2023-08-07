from django.core.files import File
from ture.models import Image
from PIL import Image as IM
from django.db.models import QuerySet
def convert_images(upload='img/', model=None, attr=None):
    images = model.objects.all()
    
    for instance in images:
        path = instance.img.path
        if instance.img.path[-4:] != 'webp':
            im = IM.open(path).convert('RGB')
            extention = instance.img.path.rsplit(".", 2)[1]
            file_name = path.replace(extention, "webp")
            file = file_name.split(upload)[1]
            im.save(file_name, 'webp')
            instance.img.save(file,File(open(file_name,'rb')))
            instance.save()
            print(instance.img)
            


def test_get_attr(upload:str, model:QuerySet, attr:str):
    images = model.objects.all()
    
    for instance in images:
        image = getattr(instance,attr)
        
        path = image.path
        if image.path[-4:] != 'webp':
            im = IM.open(path).convert('RGB')
            extention = image.path.rsplit(".", 2)[1]
            file_name = path.replace(extention, "webp")
            file = file_name.split(upload)[1]
            im.save(file_name, 'webp')
            image.save(file,File(open(file_name,'rb')))
            instance.save()
            print(image)
            
