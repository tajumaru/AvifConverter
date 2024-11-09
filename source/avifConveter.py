import TkEasyGUI as eg
import os
import pillow_avif
from PIL import Image


# define layout
layout = [
[eg.Text("変換前フォルダ")], 
[eg.Input("", key="-input1-", enable_events=True, width=120)],
[eg.Text("出力フォルダ")], 
[eg.Input("", key="-input2-", enable_events=True, width=120)],
[eg.Button("変換開始")],
[eg.Button("閉じる")]]

def convertAvif(dir_name,new_dir_name):
    files = os.listdir(dir_name)
    new_width = 500 # リサイズ後の幅
    for file in files:
     file_name = os.path.splitext(os.path.basename(file))[0]
     img = Image.open(os.path.join(dir_name, file))
     width, height = img.size
     #元のサイズ
     new_width = width
    
     # アスペクト比を固定してリサイズ
     new_height = int((new_width / width) * height)
     img_resize = img.resize((new_width, new_height), resample=Image.LANCZOS)
     #image = img_resize.convert("RGB")
     img_resize.save(os.path.join(new_dir_name, file_name + ".avif"), format="avif")
    return ''
 

# create a window
window = eg.Window("AVIF変換", layout, resizable=True)
# event loop
while True:
    event, values = window.read()
    #print("#", event, values)
    old_dir = values['-input1-']
    new_dir = values['-input2-']
    
    if event in ["変換開始"]:
        convertAvif(old_dir,new_dir)
        convertAvif(old_dir,new_dir)
        eg.popup("変換しました。")
    if event in ["閉じる", eg.WINDOW_CLOSED]:
        break
# close window
window.close()