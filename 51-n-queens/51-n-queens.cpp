class Solution {
public:
    bool isSafe(int row, int col, vector<string> &board, int n){
        int dupcol = col;
        int duprow = row;
        
        //bottom left diagonal safety
        while(row<n and col>=0){
            if(board[row][col] == 'Q') return false;
            row++;
            col--;
        }
        
        row = duprow;
        col = dupcol;
        
        //left row check
        while(col >= 0){
            if(board[row][col] == 'Q') return false;
            col--;
        }
        
        row = duprow;
        col = dupcol;
        
        //top left diagonal check
        while(row >= 0 and col >= 0){
            if(board[row][col] == 'Q') return false;
            row--;
            col--;
        }
    
        return true;
    }
    
    void solve(int col, int n, vector<string> &board, vector<vector<string>> &ans){
        if(col > n-1){
            ans.push_back(board);
            return;
        }
        
        for(int row=0; row<n; row++){
            if(isSafe(row, col, board, n)){
                board[row][col] = 'Q';
                solve(col+1, n, board, ans);
                board[row][col] = '.';
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        
        //initialise empty chess board
        vector<string> board(n);
        string s(n, '.');
        
        for(int i=0; i<n; i++){
            board[i] = s;
        }
        
        solve(0, n, board, ans);
        return ans;
    }
};