char * restoreString(char * s, int* indices, int indicesSize){
    char *ans = malloc(indicesSize + 1);
    strcpy(ans, s);
    
    for(int i = 0; i < indicesSize; i++) ans[indices[i]] = s[i];
    
    return ans;
}