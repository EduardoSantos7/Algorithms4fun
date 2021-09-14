

char * restoreString(char * s, int* indices, int indicesSize){
    char ans[indicesSize + 1];
    strcpy(ans, s);
    
    for(int i = 0; i < indicesSize; i++) {
        s[indices[i]] = ans[i];
    }
    
    return s;
}