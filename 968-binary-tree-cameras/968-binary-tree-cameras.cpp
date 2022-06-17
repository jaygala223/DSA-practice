/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    string f(TreeNode* node, int &ans){
        
        //na baap hai na bacche... to camera kyu chahiye
        if(node == NULL) return "nai_chahiye";
        
        string left = f(node->left, ans);
        string right = f(node->right, ans);
        
        if(left == "cover_kardo" or right == "cover_kardo"){
            ans++;
            return "diyaCamera";  
        } 
        
        //kisi bhi bacche ke pass hai to baap covered hai
        else if(left == "diyaCamera" or right == "diyaCamera") return "nai_chahiye";
        
        else return "cover_kardo";
    }
    
    int minCameraCover(TreeNode* root) {
        int ans = 0;
        
        if(f(root, ans) == "cover_kardo") ans++;
        
        return ans;
    }
};