# build classes that will be used to define how articles and sources data looks like

# class for shapping articles data


class Articles:

    def __init__(self, ids, source, author, title, description, url, urlToImage, publishedAt):
        self.ids = ids
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

# class for shapping sources data


class Sources:

    def __init__(self, ids, name, description, url, category, language, country):
        self.id = ids
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
