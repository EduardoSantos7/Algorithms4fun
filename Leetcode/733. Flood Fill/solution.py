class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.floodFillHelper(image,sr, sc, color, image[sr][sc])
        return image

    def floodFillHelper(self, image: List[List[int]], sr: int, sc: int, color: int, start_color: int) -> List[List[int]]:
        # Check if the point sent is valid in the matrix
        if sr < 0 or sr >= len(image):
            return
        if sc < 0 or sc >= len(image[0]):
            return

        # Update the color if needed, if so, make recursive calls sending neighboor points, else return
        if image[sr][sc] == color:
            return

        if image[sr][sc] != start_color:
            return

        image[sr][sc] = color

        self.floodFillHelper(image,sr-1, sc, color, start_color)
        self.floodFillHelper(image,sr+1, sc, color, start_color)
        self.floodFillHelper(image,sr, sc-1, color, start_color)
        self.floodFillHelper(image,sr, sc+1, color, start_color)