class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_with_duplicate_content = defaultdict(list)

        # Process the input to separate the paths and content.
        for path in paths:
            split_result = path.split(" ")
            path = split_result[0]
            for file in split_result[1:]:
                split_result = file.split("(")
                file_name, content = split_result[0], split_result[1].encode()
                # Use a dict to organize the input where the key is the content and value is a list of paths
                # The content can be encoded for efficiency and remove possible unhashable characters
                paths_with_duplicate_content[content].append(
                    f"{path}/{file_name}")

        return [val for val in paths_with_duplicate_content.values() if len(val) > 1]
