int lengthOfLastWord(char * s){
    char * p = s;
    int counter = 0;
    
    while(*p != '\0') {p++;}  // Traverse the string to the last char.
    
    // go back to count the last word.
    while(p != s) {
        if(counter && *p == ' ') break;
        if(*--p != ' ') counter++;
    }
    
    return counter;
}
