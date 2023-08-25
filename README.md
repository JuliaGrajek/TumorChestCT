# TumorChestCT

The aim of this project was to classify lung cancer tumors (adenocarcinoma, large cell carcinoma, squamous cell carcinoma, cancer-free lung (normal)). The dataset was obtained from kaggle: https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images. I fine-tuned an Xception network obtaining a test set accuracy of 88% and class-specific f1-scores of:
adenocarcinoma: 0.86 large cell carcinoma: 0.88 squamous cell carcinoma: 0.85 normal: 0.99. The model training was performed on Google Collab and saved to a keras file(see TrainModel.ipynb).

In app.py, app-components.py and Model.py the classification results were turned into a fast api endpoint. Then, the model was deployed using javascript, see example screenshot of a classification:

![image](https://github.com/JuliaGrajek/TumorChestCT/assets/57350744/620b1efa-80bf-497e-8dc6-4344e27898b1)

