int minPartitions(char * n){
    char max = *n;
    while(*n != '\0') {
        if(*n > max) max = *n;
        n++;
    }
    
    return max - '0';
}