class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        moves = 0

        for student, seat in zip(students, seats):
            moves += abs(student - seat)

        return moves