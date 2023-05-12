from PIL import Image
import os
def path_to_dict(path, execute_func=None):
    path = os.path.abspath(path)
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x), execute_func) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        if execute_func is not None:
            execute_func(path)
    return d

def img_to_webp(path):
    path_w = path.lower()
    if path_w.endswith('.jpg') or path_w.endswith('.png'):
        print(path)
        name,_ = path.split('.')
        image = Image.open(path).convert('RGB')
        image.save(f"{name}.webp", 'webp')
        os.remove(path)
    
path_to_dict('./static/img', img_to_webp)