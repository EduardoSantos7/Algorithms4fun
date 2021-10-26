class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create a dict where keys are restaurants and values index
        dict_list1 = {restaurant: index for index,
                      restaurant in enumerate(list1)}
        dict_list2 = {restaurant: index for index,
                      restaurant in enumerate(list2)}
        common_restaurants = {}

        # Check if a restaurant is in both lists and save the index sum
        dict_to_iter = dict_list1 if len(
            dict_list1) < len(dict_list2) else dict_list2

        for restaurant in dict_to_iter:
            if restaurant in dict_list1 and restaurant in dict_list2:
                common_restaurants[restaurant] = dict_list1.get(
                    restaurant) + dict_list2.get(restaurant)

        if not common_restaurants:
            return []

        # Get the min and all the restaurants where the sum is the same as min
        min_sum_index = min(common_restaurants.values())
        common_interest = list(filter(
            lambda restaurant: common_restaurants.get(restaurant) == min_sum_index, common_restaurants.keys()))

        return common_interest
