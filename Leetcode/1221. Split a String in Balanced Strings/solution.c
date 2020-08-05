int balancedStringSplit(char * s) {
    int count = 0;
    int res = 0;

    while (*s != '\0') {
        if (*s == 'R') {
            count += 1;
        }
        else {
            count -= 1;
        }

        if (!count) {
            res += 1;
        }
        s += 1;
    }

    return res;
}