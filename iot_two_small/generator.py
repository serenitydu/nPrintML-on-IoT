import subprocess as sb
import os

generate_folder = "pcaps"
if not os.path.exists(generate_folder):
    os.mkdir(generate_folder)

current_dir = os.path.dirname(os.path.abspath(__file__))
folder = ['echodot_voice', 'googlehome_voice']

with open(os.path.join(current_dir, 'labels.txt'), 'a') as f:
    f.write('Item,Label\n')
    for fn in folder:
        folder_name = os.path.join(current_dir, fn)
        for i, filename in enumerate(os.listdir(folder_name)):
            new_name = fn + '_' + str(i) + '.pcap'
            f.write(f'{new_name},{fn}\n')
            sb.call(['copy', os.path.join(folder_name, filename), os.path.join(current_dir, generate_folder, new_name)], shell=True)
        