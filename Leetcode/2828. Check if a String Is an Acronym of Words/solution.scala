object Solution {
    def isAcronym(words: List[String], s: String): Boolean = {
        words.map(_.head).mkString == s
    }
}