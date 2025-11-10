"""
News Library for JARVIS Voice Assistant
"""

import feedparser

NEWS_SOURCES = {
    "dawn": {
        "name": "Dawn",
        "url": "https://www.dawn.com/feeds/home"
    },
    "express": {
        "name": "Express Tribune", 
        "url": "https://tribune.com.pk/feeds/home"
    },
    "geo": {
        "name": "Geo News",
        "url": "https://www.geo.tv/rss/1/1"
    }
}

def get_news(source="all", limit=5, speak_func=None):
    """Get news from Pakistani sources"""
    
    all_news = []
    
    # Determine sources
    if source == "all":
        sources_to_fetch = NEWS_SOURCES.values()
        intro = "Here are the latest headlines from Pakistan"
    elif source in NEWS_SOURCES:
        sources_to_fetch = [NEWS_SOURCES[source]]
        intro = f"Here are the latest headlines from {NEWS_SOURCES[source]['name']}"
    else:
        if speak_func:
            speak_func("Invalid news source")
        return []
    
    # Fetch news
    for src in sources_to_fetch:
        try:
            feed = feedparser.parse(src['url'])
            items = 2 if source == "all" else limit
            
            for entry in feed.entries[:items]:
                all_news.append({
                    'title': entry.title.strip(),
                    'source': src['name'],
                    'link': entry.link
                })
        except Exception as e:
            print(f"Error fetching from {src['name']}: {e}")
    
    if not all_news:
        if speak_func:
            speak_func("Could not fetch news")
        return []
    
    all_news = all_news[:limit]
    
    # Display
    print("\n" + "="*60)
    print(f"🗞️  NEWS HEADLINES".center(60))
    print("="*60 + "\n")
    
    if speak_func:
        speak_func(intro)
    
    for i, news in enumerate(all_news, 1):
        print(f"📌 {i}. [{news['source']}]")
        print(f"   {news['title']}")
        print(f"   🔗 {news['link']}\n")
        
        if speak_func:
            if source == "all":
                speak_func(f"Headline {i} from {news['source']}. {news['title']}")
            else:
                speak_func(f"Headline {i}. {news['title']}")
    
    print("="*60 + "\n")
    
    if speak_func:
        speak_func("That's all for now")
    
    return all_news


def get_news_summary(source="all", limit=3, speak_func=None):
    """Get brief news summary without speaking each headline"""
    
    all_news = []
    
    if source == "all":
        sources_to_fetch = NEWS_SOURCES.values()
    elif source in NEWS_SOURCES:
        sources_to_fetch = [NEWS_SOURCES[source]]
    else:
        if speak_func:
            speak_func("Invalid news source")
        return []
    
    for src in sources_to_fetch:
        try:
            feed = feedparser.parse(src['url'])
            items = 2 if source == "all" else limit
            
            for entry in feed.entries[:items]:
                all_news.append({
                    'title': entry.title.strip(),
                    'source': src['name'],
                    'link': entry.link
                })
        except:
            continue
    
    if not all_news:
        if speak_func:
            speak_func("Could not fetch news")
        return []
    
    all_news = all_news[:limit]
    
    print("\n" + "="*60)
    print("🗞️  NEWS SUMMARY".center(60))
    print("="*60 + "\n")
    
    for i, news in enumerate(all_news, 1):
        print(f"📌 {i}. [{news['source']}] {news['title']}")
        print(f"   🔗 {news['link']}\n")
    
    print("="*60 + "\n")
    
    if speak_func:
        speak_func(f"I've displayed {len(all_news)} news headlines on screen")
    
    return all_news