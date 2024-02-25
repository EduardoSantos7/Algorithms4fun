func findingUsersActiveMinutes(logs [][]int, k int) []int {
    userActions := make(map[int]map[int]struct{})

    for _, log := range logs {
        userID, actionMin := log[0], log[1]

        if _, ok := userActions[userID]; ! ok {
            userActions[userID] = make(map[int]struct{})
        }
        userActions[userID][actionMin] = struct{}{}
    }

    usersByUAM := make([]int, k)
    for _, actions := range userActions {
        totalMins := len(actions)
        usersByUAM[totalMins - 1]++
    }

    return usersByUAM
}