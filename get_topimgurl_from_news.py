from newspaper import Article

# get_topimgurl_from_news.get_topimgurl_from_news(url)

def get_topimgurl_from_news(url):
    article = Article(url)
    article.download()
    article.parse()
    
    image_url = article.top_image
    
    return image_url
