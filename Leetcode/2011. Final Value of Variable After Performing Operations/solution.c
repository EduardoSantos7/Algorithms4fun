int finalValueAfterOperations(char ** operations, int operationsSize){
    int acum = 0;
    for(int i = 0; i < operationsSize; i++) {
        acum += (operations[i][0] == '+' || operations[i][1] == '+') ? 1 : -1;
    }
    
    return acum;
}