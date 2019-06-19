# day two
facebanging my head to the desk and just made enough progress to warrant a write down.

made 19 pictures of water bottle & a buch of pictures of can of coke.
then downloaded them from the cloud to my jupiter notebook server
stored all the good stuff in .fastai/data/coke
in addition to pictures created two folders split for training and validation
moved 4 to validation left 15 in training
created a CSV file that holds locations to the directory of each evaluated file(picture of water or coke)
filepath is name, if its coke or water 1/0 is the label
csv with two properties

setup completed.
lets go running some fastai

had to import paths and set up my own path because notebook only use fastai url download method
```python
import pathlib
path = pathlib.Path("/data/home/adminn/.fastai/data/cola")
```

in the notebook there is another command that display csv file list. i dont actually use it for anyhting 
```python
df = pd.read_csv(path/'labels.csv')
df.head(15)
```

then import stuff using imagedatabunch CSV option
also here i can adjust the size, this modifies the quality of my imported pictures, copied normalize from the main run
```python
data = ImageDataBunch.from_csv(path, ds_tfms=tfms, size=64).normalize(imagenet_stats)
```

because i only use 19 images & the default batch size is too large i reduce the batch size

```python
data.batch_size = 12
```

I can display my images, more rows for more rows more figsize for larger thumbnails, does not represet actual rumbers for some reason

```python
data.show_batch(rows=5, figsize=(12,12))
```

some reporting on what the data is before you start training
```python
print(data.classes)
len(data.classes),data.c
```

generic stuff, resnet 34
```python
learn = cnn_learner(data, models.resnet34, metrics=error_rate)
learn.model
```

do the actual learning please
```python
learn.fit_one_cycle(10)
```


interpreting results
```python
interp = ClassificationInterpretation.from_learner(learn)

losses,idxs = interp.top_losses()

len(data.valid_ds)==len(losses)==len(idxs)
```

confusion matrix - shows results where predictions were wrong
```python
interp.plot_confusion_matrix(figsize=(8,8), dpi=100)
```



scriptblock
```python

path = pathlib.Path("/home/adminn/notebooks/cola")
tfms = get_transforms(do_flip=False)


df = pd.read_csv(path/'labels.csv')
df.head(15)

data = ImageDataBunch.from_csv(path, ds_tfms=tfms, size=64)


data.batch_size = 12
data.show_batch(rows=5, figsize=(12,12))

print(data.classes)
len(data.classes),data.c

learn = cnn_learner(data, models.resnet34, metrics=error_rate)

learn.model

learn.fit_one_cycle(10)

learn.save('stage-1')


interp = ClassificationInterpretation.from_learner(learn)

losses,idxs = interp.top_losses()

len(data.valid_ds)==len(losses)==len(idxs)

interp.plot_confusion_matrix(figsize=(8,8), dpi=100)

learn.lr_find()
learn.recorder.plot()

```

%reload_ext autoreload
%autoreload 2
%matplotlib inline
from fastai.vision import *
from fastai.metrics import error_rate
bs = 16
# bs = 16   # uncomment this line if you run out of memory even after clicking Kernel->Restart