# import pandas lib as pd
import pandas as pd
import glob
import os
import shutil

# read by default 1st sheet of an excel file
df = pd.read_excel(
    'Processed_HAM10000_metadata.xlsx', engine='openpyxl'
)

print(df["image_id"].index)
pictureid_label_correpsondence = {}
unique_class_label = []
for ind in df.index:
    if(df['dx'][ind] not in unique_class_label):
        unique_class_label.append(df['dx'][ind])
    pictureid_label_correpsondence[df['image_id'][ind]+'.jpg'] = df['dx'][ind]

print(unique_class_label, pictureid_label_correpsondence['ISIC_0031743.jpg'])

# place image into corresponding class label


def SortImageClass(path, img_dict):
    paths = glob.glob(f'{path}/*.jpg')
    for i, path in enumerate(paths):
        *_, folder, basename = path.split("\\")
        class_name = img_dict[basename]
        dst = f'./ProcessedData/{class_name}/{basename}'
        if not os.path.isdir(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        shutil.move(path, dst)


SortImageClass("./Data", pictureid_label_correpsondence)
