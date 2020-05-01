import operator
import indicoio
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import colorgram
import urllib.request
# from aylienapiclient import textapi
# client = textapi.Client("421c4a8f", "ea6700bf887522bd690449d429940202")
# url = "https://en.wikipedia.org/wiki/Alprazolam"
# classifications = client.ClassifyByTaxonomy({"url": url, "taxonomy": "iab-qag"})
# for category in classifications['categories']:
#   print(category)
    # sentiments = indicoio.sentiment(example_sentence)
    # text_tags = indicoio.text_tags(example_sentence)

    # print(sentiments)
    # print(text_tags)
    # print('++++')
    # print(max(text_tags.items(), key=operator.itemgetter(1))[0])

indicoio.config.api_key = 'a16db89429526f77420d066cb39b4d3c'
def indicoio_classify(sentence):
    text_tags = indicoio.text_tags(sentence)
    text_tags_filtered = {}
    text_tags_filtered['relationships'], text_tags_filtered['depression'], text_tags_filtered['substance_abuse'] = {}, {}, {}

    for catogory, score in text_tags.items():
        if (catogory in ['relationships', 'wedding', 'gender_issues', 'lgbt', 'romance']) and (score >= 0.05):
            text_tags_filtered['relationships'][catogory] = score
    for catogory, score in text_tags.items():
        if (catogory in ['personal', 'nostalgia', 'personal_care_and_beauty']) and (score >= 0.03):
            text_tags_filtered['depression'][catogory] = score
    for catogory, score in text_tags.items():
        if (catogory in ['drugs', 'wine', 'poker']) and (score >= 0.03):
            text_tags_filtered['substance_abuse'][catogory] = score
    values = []
    print(text_tags_filtered)
    for _, value in text_tags_filtered.items():
        if value == {}:
            values.append(0)
        else:
            values.append(max(value.items(), key=operator.itemgetter(1))[1])
    print(values)
    names = ['relationship', 'personal issues', 'addiction']


    plt.bar(range(len(names)),values,tick_label=names)
    plt.show()
    print(text_tags_filtered)
    
# indicoio_classify('I hate all men')
def indicoio_analyze_emotions(sentence, **kwargs):

    emotions = indicoio.emotion(sentence)
    print(emotions)
    try: 
        key_emotions = kwargs['key_emotions']
    except KeyError:
        key_emotions = {}
        
    for emotion, score in emotions.items():
        if (emotion != 'joy') and (score >= 0.4):
            key_emotions[emotion] =  score

    names = list(emotions.keys())
    values = list(emotions.values())
    print('significant stuf:')
    print(key_emotions)

    plt.bar(range(len(emotions)),values,tick_label=names)
    plt.show()
# indicoio_analyze_emotions('I hate all men') 



def analyze_color(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    name = url.replace('.', '').replace('/', '')
    img_png = img.save(f'imgs/color/{name}', 'png')
    colors = colorgram.extract(f'imgs/color/{name}.png', 5)
    prominent_colors = []
    for i in range(5):
        try:
            if colors[i].proportion >= 0.3:
                prominent_colors.append(colors[i])
        except:
            IndexError
    for i in prominent_colors:
        if (i.rgb.r > 130) or (i.rgb.g > 90) or (i.rgb.b > 110):
            del prominent_colors[i]
    print(prominent_colors)


def indicoio_analyze_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    name = url.replace('.', '').replace('/', '')
    img_png = img.save(f'imgs/object/{name}.png', 'png')
    detection = indicoio.image_recognition(f'imgs/object/{name}.png', hq=True)
    return detection









URL = 'https://scontent.xx.fbcdn.net/v/t1.0-9/s720x720/41922873_122239752068203_589814050439823360_o.jpg?_nc_cat=0&oh=932112665541cb9f95766fb5fcfcddd9&oe=5C32AAF4'
# indicoio_analyze_image(URL)
res = indicoio_analyze_image(URL)

resi = {}
for x, y in res.items():

    if y >= 0.02:
        resi[x] = y
print(resi)