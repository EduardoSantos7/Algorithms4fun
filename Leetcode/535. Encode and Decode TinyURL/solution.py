class Codec:
    counter = 0
    database = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter += 1
        self.database[f"https://es7service.com/{self.counter}"] = longUrl
        return f"https://es7service.com/{self.counter}"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.database.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))