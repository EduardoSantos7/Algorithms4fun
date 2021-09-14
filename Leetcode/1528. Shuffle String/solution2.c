

char * restoreString(char * s, int* indices, int indicesSize){
    int temp_pos = 0;
    char temp_char = (char) 0;
    bool change = true;

    do {
        change = false;
        for(int i = 0; i < indicesSize; i++) {
            if(indices[i] == i) continue;

            change = true;
            temp_pos = indices[i];
            temp_char = s[i];

            indices[i] = indices[indices[i]];
            s[i] = s[temp_pos];

            indices[temp_pos] = temp_pos;
            s[temp_pos] = temp_char;
        }
    }
    while(change);
    
    return s;
}