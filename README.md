# Vision-Transformer-Transfer-Learning

fileprocessing.py precoess the dataset and put the images into its corresponding folder based on their label.
Some pathing issue might exist. Change if you see fit


THe main program VITTransferLearning is seperated into 3 parts.


Note that you only need to run sections 1 and 3 for testing the models. Section 2 is for the fine tuning on HAM10000 dataset.

Sections 1 dataset preprocessing: download the process dataset from my google drive and split it into 90:10 training to testing sets

Section 2 Trasnfer Learning: import the relevant module and clone the google research's vision transformer repository, fine tune using the their pretrained model on HAM10000 Dataset

Section 3 checkpoint inferences: after section 2 it will output a checkpoint that reperesent the model after transfer learning. this section reloads this checkpoint and do inferences based on it.The checkpoint will be automatically downloaded from my google drive if you run this section 
