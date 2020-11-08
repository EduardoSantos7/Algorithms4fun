func canFormArray(arr []int, pieces [][]int) bool {
    index := make(map[int][]int)
    
    for _, list := range pieces {
        index[list[0]] = list
    }
    
    result := make([]int, 0)
    
    for _, num := range arr {
        if list, ok := index[num]; ok {
            result = append(result, list...)
        }
    }
    
    return reflect.DeepEqual(result, arr)
}
