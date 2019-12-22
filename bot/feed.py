class Feed:

    def __init__(self, title, link, source, time, summary, category):	
        self.title = title
        self.link = link
        self.source = source
        self.time = time.strftime("%Y/%m/%d %H:%M:%S") 
        self.summary = summary
        self.category = category

    def __repr__(self):
        return "title: %s\nlink: %s\nsource: %s\ntime: %s\nsummary: %s\ncategory: %s" % (self.title, self.link, self.source, self.time, self.summary, self.category)

