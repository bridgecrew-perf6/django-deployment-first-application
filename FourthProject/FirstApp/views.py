from django.shortcuts import render

# Create your views here.
import datetime
def wishes(request):
    date1=datetime.datetime.now()
    msg1: "Hello user /client....GOOD"
    hr= int(date1.strftime('%H'))
    imgs= "image1.jpg"
    if hr<12:
        msg1+="Morning"
        imgs= "image1.jpg"
    elif hr<16:
        msg1+= "Afternoon"
        imgs = "image2.jpg"
    elif hr<20:
        msg1+= "evening"
        imgs="image3.jpg"
    else:
        msg1="Hello user/client.... very good night"
        imgs= "image4.jpg"
    dict1={"date1":date1,"msg1":msg1,"imgs":imgs}
    return render(request,"FirstApp/wishes.html",context=dict1)

def imagegallery(request):
    date1 = datetime.datetime.now()
    msg1 = '**DJango-Image-Gallery**';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imgsgallery.html',context=dict1)

def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '**DJango-Image-Gallery(Product)**';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imgsgallery2.html', context=dict1);
def wishes4(request):
    date1=datetime.datetime.now()
    msg1='**django tempates using css styles**'
    dict1={'date1':date1,"msg1":msg1}
    return render(request, 'FirstApp/wishes4.html', context=dict1);


def index(request):
    return render(request,'FirstApp/index.html')

def indianews(request):
    dict1 = {'mainmsg': 'India News Page',
             'submsg1': '100+ crores vaccines successfully done!!!',
             'submsg2': 'India is super-power in the world',
             'submsg3': 'Agni-5 long-range missile(20,000 kms) successfully tested!!!',
             'photo': 'images/image1.jpg'};
    return render(request, 'FirstApp/news.html', context=dict1);


def sportsnews(request):
    dict1 = {'mainmsg': 'Sports News Page',
             'submsg1': 'India won Cricket World Cup 2023',
             'submsg2': 'World Olympic India Gold Count 500(Tops-List)',
             'submsg3': 'India to host next Olympics for 5-times',
             'photo': 'images/image2.jpg'};
    return render(request, 'FirstApp/news.html', context=dict1);


def technews(request):
    dict1 = {'mainmsg': 'Technology News Page',
             'submsg1': 'Apple to release Apple-14 in 4-models(mini,basic,pro,pro-max',
             'submsg2': 'India starts Semi-conductor chips to World Smartphones',
             'submsg3': 'Tech-jobs more in India than elsewhere in the world',
             'photo': 'images/image3.jpg'};
    return render(request, 'FirstApp/news.html', context=dict1);