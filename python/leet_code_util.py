class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.random = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    @classmethod
    def buildTree(self, preorder, inorder):
         if len(preorder)==0 or len(inorder)==0:
             return None
         root_val = preorder[0]
         in_idx = inorder.index(root_val)
         root = TreeNode(root_val)
         inorder_left = inorder[0:in_idx]
         inorder_right = inorder[in_idx+1:]
         preorder_left = preorder[1 : len(inorder_left) + 1]
         preorder_right = preorder[len(inorder_left) + 1:]
         root.left = self.buildTree(preorder_left, inorder_left)
         root.right = self.buildTree(preorder_right, inorder_right)  
         return root
     
    @classmethod
    def buildTree2(self, inorder, postorder):
        if len(inorder)==0 or len(postorder)==0:
             return None 
        root_val = postorder[-1]
        mid_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        inorder_left = inorder[:mid_idx]
        inorder_right = inorder[mid_idx+1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(inorder)-1]       
        root.left = self.buildTree2(inorder_left, postorder_left)
        root.right = self.buildTree2(inorder_right, postorder_right)
        return root
    
    @classmethod
    def buildTree3(self, nums):
        def build(idx, nums):
            if idx >= len(nums):
                return None
            node = TreeNode(nums[idx])
            node.left = build(2*idx + 1, nums)
            node.right = build(2*idx +2, nums)
            return node
        return build(0, nums)
        
def buid_list_node(val_nums):
    head = ListNode(0, None)
    temp = head
    for i in range(len(val_nums)):
        node = ListNode(val_nums[i])
        node.random = None
        head.next = node
        head = head.next
    return temp.next

def buid_list_node2(val_nums):
    head = ListNode(0, None)
    temp = head
    for i in range(len(val_nums)):
        node = ListNode(val_nums[i][0])
        node.random = val_nums[i][1]
        head.next = node
        head = head.next
    return temp.next




def fab(n):
    dp = {0:1, 1:1}
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n-1]

def palouti(cost,n):
    dp = {0:0, 1:0}
    for i in range(2,n+1):
        dp[i] = min((dp[i-1]+cost[i-1]),(dp[i-2]+cost[i-2]))
    return dp[n]

def butonglujing():
    pass

#No.146
class LRUCache:
    tick = 0
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        LRUCache.tick += 1
        #debug begin
        if key == 7:
            pass

        #debug done        
        if key in self.cache.keys():
            self.cache[key][1] = LRUCache.tick
            #print(self.cache)
            return self.cache[key][0]
        else:
            #print(self.cache)
            return -1    

    def put(self, key: int, value: int) -> None:
        LRUCache.tick += 1
        key_list = list(self.cache.keys())
        if key in self.cache.keys():
            pass
        else:
            if len(key_list) + 1 > self.capacity:
                value_list = list(self.cache.values())
                smallest_used = value_list[0][1]
                for value_ in value_list:
                    if value_[1] <= smallest_used:
                        smallest_value = value_ 
                        smallest_used = smallest_value[1]    
                #print("smallest_value tick {} will be evicted".format(smallest_value[1]))       
                
                for key_,value_ in self.cache.items():
                    #print("value_ is {}".format(value_))
                    #print("smallest_value is {}".format(smallest_value))
                    if value_ == smallest_value:
                        the_key = key_
                pop_value = self.cache[the_key]

                #print("now, tick is {}".format(LRUCache.tick))
                #print("{}->{}, tick {} is evicted".format(the_key, pop_value[0], pop_value[1]))
                if the_key == 7:
                    pass
                self.cache.pop(the_key)

        if key in self.cache.keys():
            value_time = self.cache[key]
            value_time = [value, LRUCache.tick]
            self.cache[key] = value_time
        else:
            value_time = [value, LRUCache.tick]
            self.cache[key] = value_time
        #print(self.cache)

if __name__ == "__main__":
    lru_cache = None
    behavior = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    data = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    idx = 0
    while idx < len(behavior):
        match behavior[idx]:
            case "put":
                print(lru_cache.put(*data[idx]))
            case "get":
                print(lru_cache.get(*data[idx]))
            case "LRUCache":
                lru_cache = LRUCache(*data[idx])
        idx += 1
    
        

