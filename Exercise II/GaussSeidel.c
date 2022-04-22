void gauss_seidel(double f[][256], double newf[][256]){
    int i, j;
    for (i=0; i<256; i++) {
        for (j=0; j<256; j++) {
            newf[i][j] = f[i][j];
        }
    }
    for (i=1; i<255; i++) {
        for (j=1; j<255; j++) {
            newf[i][j] = 0.25 * (newf[i][j+1] + newf[i][j-1] +
                         newf[i+1][j] + newf[i-1][j]);
        }
    }
}

