class Article:
    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
     if not hasattr(self, "_title"):  # Set only if not already set
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")


class Author:
   def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
     if not hasattr(self, "_name"):  # Allow setting only once
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

             def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list({magazine.category for magazine in self.magazines()})
        return categories if categories else None


class Magazine:
     def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
     if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
        self._name = new_name
     else:
        pass  # Silently ignore invalid changes

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
     if isinstance(new_category, str) and len(new_category) > 0:
        self._category = new_category
     else:
        pass  # Silently ignore invalid changes


    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1

        frequent_authors = [author for author, count in author_count.items() if count > 1]
        return frequent_authors if frequent_authors else None