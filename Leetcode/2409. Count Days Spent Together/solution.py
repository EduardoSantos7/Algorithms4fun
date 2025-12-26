class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0] * 366
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_days(date):
            return sum(months[:int(date[:2]) - 1]) + int(date[3:])

        alice_start = date_to_days(arriveAlice)
        alice_days = date_to_days(leaveAlice) - alice_start
        bob_start = date_to_days(arriveBob)
        bob_days = date_to_days(leaveBob) - date_to_days(arriveBob)

        for i in range(alice_start, alice_start + alice_days + 1):
            days[i] += 1
        
        for i in range(bob_start, bob_start + bob_days + 1):
            days[i] += 1

        return len([x for x in days if x == 2])
