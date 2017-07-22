#### Description
Multi labels text classification

#### Models
Models are `convolutional neural network` with a `word embedding layer` custom trained with domain specific corpus. models are individually trained per `y_`

Here is dataset sample
![DataSample](https://onevmw-my.sharepoint.com/personal/juhyeongy_vmware_com/_layouts/15/guestaccess.aspx?docid=021cebb8598ab43fd9c5f8c02db61073e&authkey=AeJ7G7-C8rfWSJujn25NLkM&expiration=2017-07-31T10%3a26%3a35.000Z)

Here is train/test validation report sample. Validation accuracy scores are bounded between 40~60%
```
Training Category-Classifier Now...
Train on 3288 samples, validate on 823 samples
Epoch 10/20
3288/3288 [==============================] - 91s - loss: 1.3141 - acc: 0.5289 - val_loss: 1.3562 - val_acc: 0.5431
Training Component-Classifier Now...
Train on 3288 samples, validate on 823 samples
Epoch 1/20
3288/3288 [==============================] - 101s - loss: 3.1712 - acc: 0.2205 - val_loss: 2.9410 - val_acc: 0.1324
```

### Repo Structure
- classifiers -> models + training / update
- crawler -> crawling runtime
- data-service -> api service
- web -> ui
