int maxPower(char * s){
    char * prev = NULL;
    int count = 0;
    int max = 0;

    while(*s != '\0') {
        if(prev && *s == *prev) count++;
        else {
            count = 1;
            prev = s;
        }
        if(count > max) max = count;
        
        s++;
    }
    
    return max;
}
