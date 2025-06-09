class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        answer = []
        currentStateArray = [c for c in currentState]
        for i in range(0, len(currentState) - 1):
            if currentState[i] == "+" and currentState[i+1] == "+":
                currentStateArray[i] = "-"
                currentStateArray[i + 1] = "-"
                answer.append("".join(currentStateArray))
                currentStateArray[i] = "+"
                currentStateArray[i + 1] = "+"
        return answer