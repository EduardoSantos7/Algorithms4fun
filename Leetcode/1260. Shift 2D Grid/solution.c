/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int rows = gridSize;
    int cols = *gridColSize;
    int total = rows * cols;
    k = k % total;

    *returnSize = rows;
    *returnColumnSizes = (int*)malloc(sizeof(int) * rows);
    for (int i = 0; i < rows; i++) {
        (*returnColumnSizes)[i] = cols;
    }

    int start = 0;
    int countVisited = 0;

    while (countVisited < total) {
        int current_index = start;
        int current_value = grid[current_index / cols][current_index % cols];

        while (1) {
            int next_index = (current_index + k) % total;
            int next_value = grid[next_index / cols][next_index % cols];

            grid[next_index / cols][next_index % cols] = current_value;
            current_index = next_index;
            current_value = next_value;
            countVisited++;

            if (current_index == start) {
                break;
            }
        }

        start++;
    }

    return grid;
}