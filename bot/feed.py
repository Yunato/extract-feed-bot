class Feed:

    def __init__(self, title, link, source, time, summary, category):	
        self._title = title
        self._link = link
        self._source = source
        self._time = time.strftime("%Y/%m/%d %H:%M:%S")
        self._summary = summary
        self._category = category

    def __repr__(self):
        return "title: %s\nlink: %s\nsource: %s\ntime: %s\nsummary: %s\ncategory: %s" % (self._title, self._link, self._source, self._time, self._summary, self._category)

