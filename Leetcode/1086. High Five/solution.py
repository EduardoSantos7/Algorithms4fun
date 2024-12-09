class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Iterate the items and group the top 5 scores bi student id
        # For example [[1, 98], [1, 99], [2, 89]] -> {1: [98, 99], 2: [89]}
        scores_by_students = {}
        for student_id, score in items:
            self.update_top_student_scores(student_id, scores_by_students, score)

        # For each id process the top 5 scores to get their average and convert it to a list
        high_five_average_by_student = []
        for student_id in sorted(scores_by_students):
            high_five_average_by_student.append([student_id, sum(scores_by_students[student_id]) // len(scores_by_students[student_id])])
        
        return high_five_average_by_student
    
    def update_top_student_scores(self, student_id, scores_by_students, score):
        if student_id not in scores_by_students:
            scores_by_students[student_id] = [score]
        else:
            # insert in increasing order
            index_to_insert = 0
            while index_to_insert < len(scores_by_students[student_id]) and scores_by_students[student_id][index_to_insert] < score:
                index_to_insert += 1
            scores_by_students[student_id].insert(index_to_insert, score)
            # Just keep the last 5
            scores_by_students[student_id] = scores_by_students[student_id][-5:]

