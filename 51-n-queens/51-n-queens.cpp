class Solution {
public:
    void solve(int col, int n, vector<string> &board, vector<vector<string>> &ans, vector<int> &bottomDiag, vector<int> &upDiag, vector<int> &leftRow){
        if(col > n-1){
            ans.push_back(board);
            return;
        }
        
        for(int row=0; row<n; row++){
            if(upDiag[n-1 + col - row] == 0 and bottomDiag[row + col] == 0 and leftRow[row] == 0){
                board[row][col] = 'Q';
                
                //set positions to 1 for hashing
                upDiag[n-1 + col - row] = 1; 
                bottomDiag[row + col] = 1; 
                leftRow[row] = 1;
                
                solve(col+1, n, board, ans, bottomDiag, upDiag, leftRow);
                board[row][col] = '.';
                
                //backtrack bhi to karlo
                upDiag[n-1 + col - row] = 0; 
                bottomDiag[row + col] = 0; 
                leftRow[row] = 0;
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        
        //initialise empty chess board
        vector<string> board(n);
        string s(n, '.');
        
        //checking-with-hashing approach
        vector<int> bottomDiag(2*n - 1,0);
        vector<int> upDiag(2*n - 1,0);
        vector<int> leftRow(n,0);
        
        for(int i=0; i<n; i++) board[i] = s;
        
        solve(0, n, board, ans, bottomDiag, upDiag, leftRow);
        return ans;
    }
};