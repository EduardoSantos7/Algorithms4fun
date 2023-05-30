class Codec:
    counter = 0
    long_map = dict()
    short_map = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.long_map:
            self.counter += 1
            short_url = f"https://es7service.com/{self.counter}"
            self.short_map[short_url] = longUrl
            self.long_map[longUrl] = self.counter
            return short_url
        
        return f"https://es7service.com/{self.long_map[longUrl]}"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))