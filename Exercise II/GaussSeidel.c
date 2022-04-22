void gauss_seidel(double f[][100], double newf[][100]){
    int i, j;
    for (i=0; i<100; i++) {
        for (j=0; j<100; j++) {
            newf[i][j] = f[i][j];
        }
    }
    for (i=1; i<99; i++) {
        for (j=1; j<99; j++) {
            newf[i][j] = 0.25 * (newf[i][j+1] + newf[i][j-1] +
                         newf[i+1][j] + newf[i-1][j]);
        }
    }
}

