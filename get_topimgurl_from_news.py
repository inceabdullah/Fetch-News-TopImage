from newspaper import Article

# get_topimgurl_from_news.get_topimgurl_from_news(url)

# default haber resmi: http://haber.ozguruygulama.com/static/h_news.png

def get_topimgurl_from_news(url):
    article = Article(url)
    article.download()
    try:
        article.parse()
        image_url = article.top_image
    except:
        image_url = "http://haber.ozguruygulama.com/static/h_news.png"
    
    
    
    return image_url
