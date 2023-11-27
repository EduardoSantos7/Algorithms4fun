function isAcronym(words: string[], s: string): boolean {
    return words.map(word => word.charAt(0)).join('') === s;
};