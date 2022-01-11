/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int pv = p->val, qv = q->val;
        
        while(root != NULL){
            int rv = root->val;
            
            //if both p and q are in different subtrees, then root is our LCA
            if((pv > rv and qv < rv) || (pv < rv and qv > rv)){
                return root;
            }
            
            //if anyone becomes equal to root then its LCA by default
            else if(root == p || root == q){
                return root==p?p:q;
            }

                if(pv > rv) root = root->right;
                else root = root->left;
        }
        return NULL;
    }
};