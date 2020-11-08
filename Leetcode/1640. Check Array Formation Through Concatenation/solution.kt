class Solution {
    fun canFormArray(arr: IntArray, pieces: Array<IntArray>): Boolean {
        val index:HashMap<Int, IntArray> = HashMap<Int,IntArray>()
        
        for (elem in pieces) {
            index.put(elem[0], elem)
        }
        
        var result: List<Int> = listOf();
        
        for (num in arr) {
            val list:IntArray? = index.get(num)

            if(list?.isEmpty() == false) {
                result = result + list.toList()
            }
        }
        
        return result == arr.toList()
    }
}