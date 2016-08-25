# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):



    def recoverTree(self, root):

        """

        :type root: TreeNode

        :rtype: void Do not return anything, modify root in-place instead.

        """

        if root == None:

            return

        one = None

        stk = []

        res = []

        curr = root

        while True:

            while curr:

                stk.append(curr)

                curr = curr.left

            curr = stk.pop()

            res.append(curr)

            curr = curr.right

            if len(stk)==0 and curr == None:

                break

        print [x.val for x in res]

        for n in range(len(res)):

            print n

            if (res[n].val > res[n+1].val) and ((len(res)-n >= 3 and res[n].val < res[n+2].val and one==None) or (len(res)-n ==2 and one == None)):

                temp = res[n].val

                res[n].val = res[n+1].val

                res[n+1].val = temp

                print [x.val for x in res]

                return

            elif res[n].val > res[n+1].val:

                if one == None:

                    one = n

                else:

                    two = res[n+1].val

                    res[n+1].val = res[one].val

                    res[one].val = two

                    print [x.val for x in res]

                    return

                    

                    

        

            

        

            
