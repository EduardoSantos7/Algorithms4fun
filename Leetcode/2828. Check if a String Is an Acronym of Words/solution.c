bool isAcronym(char ** words, int wordsSize, char * s){
    char initials[wordsSize + 1];
    for (int i = 0; i < wordsSize; i++) {
        initials[i] = words[i][0];
    }
    initials[wordsSize] = '\0';
    return strcmp(initials, s) == 0;
}