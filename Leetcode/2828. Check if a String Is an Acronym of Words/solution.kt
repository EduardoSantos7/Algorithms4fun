class Solution {
    fun isAcronym(words: List<String>, s: String): Boolean {
        return words.joinToString("") { it.take(1) } == s
    }
}