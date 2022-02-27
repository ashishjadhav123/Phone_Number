import nltk
import re
from nltk.corpus import stopwords
import string
# nltk.download('stopwords')
stemmer = nltk.SnowballStemmer('english')
stopword = set(stopwords.words('english'))

def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub('https?://\S+ |www\. \S+','',text)
    text = re.sub('<.*?>+','',text)
    text = re.sub('[%S] %re.escape(string.punctuation)','',text)
    text = re.sub('\n','',text)
    text = re.sub('\w*\d\w*','',text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text

text = """Now that we’ve reviewed our face mask dataset, let’s learn how we can use Keras and TensorFlow to train a classifier to automatically detect whether a person is wearing a mask or not.

To accomplish this task, we’ll be fine-tuning the MobileNet V2 architecture, a highly efficient architecture that can be applied to embedded devices with limited computational capacity (ex., Raspberry Pi, Google Coral, NVIDIA Jetson Nano, etc.).

Note: If your interest is embedded computer vision, be sure to check out my Raspberry Pi for Computer Vision book which covers working with computationally limited devices for computer vision and deep learning.

Deploying our face mask detector to embedded devices could reduce the cost of manufacturing such face mask detection systems, hence why we choose to use this architecture.

Let’s get started!"""

data = clean(text)
print(data)
