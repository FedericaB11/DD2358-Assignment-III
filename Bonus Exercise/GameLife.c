#include <stdio.h>

void update(int grid[][800], int newGrid[][800], int N) {
    int i, j, m, n;
    int total;
    int ON = 255;
    int OFF = 0;
    for (i=1; i<800; i++) {
        for (j=1; j<800; j++) {
            total = (int) (grid[i][(j-1)%N] + grid[i][(j+1)%N] +
                           grid[(i-1)%N][j] + grid[(i+1)%N][j] +
                           grid[(i-1)%N][(j-1)%N] + grid[(i-1)%N][(j+1)%N] +
                           grid[(i+1)%N][(j-1)%N] + grid[(i+1)%N][(j+1)%N])/255;

            if ( grid[i][j] == ON && ( total < 2 || total > 3 ) ) {
                newGrid[i][j] = OFF;
            }

            else if ( total == 3 ) {
                newGrid[i][j] = ON;
            }
            
    for (m=0; m<800; m++) {
        for (n=0; n<800; n++) {
            grid[m][n] = newGrid[m][n];
        }
    }
}
