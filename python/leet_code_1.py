from collections import deque
import re

class Solution:

    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

    def removeDuplicates_2(self, nums) -> int:
        left = 1
        for right in range(2,len(nums)):
            if nums[left] == nums[right] and nums[left-1] == nums[right]:
                continue
            left += 1
            nums[left] = nums[right]
            
        return left + 1
    
    def majorityElement(self, nums) -> int:
        caculate_dict = dict()
        for i in range(0, len(nums)):
            if nums[i] not in caculate_dict.keys():
                caculate_dict[nums[i]] = 1
            else:
                caculate_dict[nums[i]] += 1
        for key,value in caculate_dict.items():
            if value > len(nums)/2:
                return key
            
    def rotate(self, nums , k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for k in range(k):
            last = nums[-1]
            nums[1:] = nums[0:-1]
            nums[0] = last
  
    def romanToInt(self, s) -> int:
        roman_char_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        def get_value(s):
            for key,value in roman_char_map.items():
                if s == key:
                    return value
        def rule_I(first, second):
            if first == 'I':
                if second == 'V':
                    return 4
                if second == 'X':
                    return 9
            return 1
        def rule_X(first, second):
            if first == 'X':
                if second == 'L':
                    return 40
                if second == 'C':
                    return 90
            return 10 
        def rule_C(first, second):
            if first == 'C':
                if second == 'D':
                    return 400
                if second == 'M':
                    return 900
            return 100
        sum = 0
        index = 0
        while True:
            if index >= len(s):
                return sum
            if s[index] == 'I':
                if index != len(s) -1:
                    sum = sum + int(rule_I(s[index], s[index+1]))
                    if s[index+1] == 'V' or s[index+1] == 'X':
                        index = index + 2
                    else:
                        index = index + 1
                    continue
                    
            if s[index] == 'X':
                if index != len(s) -1:
                    sum = sum + int(rule_X(s[index], s[index+1]))
                    if s[index+1] == 'L' or s[index+1] == 'C':
                        index = index + 2
                    else:
                        index = index + 1
                    continue

            if s[index] == 'C':
                if index != len(s) -1:
                    sum = sum + int(rule_C(s[index], s[index+1]))
                    if s[index+1] == 'D' or s[index+1] == 'M':
                        index = index + 2
                    else:
                        index = index + 1
                    continue 
            sum = sum + get_value(s[index])
            index = index +1
            if index >= len(s):
                break
        return sum
    
    def intToRoman(self, num: int) -> str:
        roman_digit_map = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        roman_special_map = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        qian = num // 1000
        bai = (num - 1000*qian) // 100 
        shi = (num - 1000* qian - 100 * bai ) // 10
        ge = num % 10
        roman_char = ""
        for i in range(qian):
            roman_char = roman_char + "M"
        if bai == 4 or bai == 9 :
            roman_char = roman_char + roman_special_map[bai*100]
        else:
            if bai >= 5:
                roman_char = roman_char + roman_digit_map[500]
                for j in range(bai - 5):
                    roman_char = roman_char + roman_digit_map[100]
            else:
                for j in range(bai):
                    roman_char = roman_char + roman_digit_map[100]
        if shi == 4 or shi == 9 :
            roman_char = roman_char + roman_special_map[shi*10]
        else:
            if shi >= 5:
                roman_char = roman_char + roman_digit_map[50]
                for j in range(shi - 5):
                    roman_char = roman_char + roman_digit_map[10]
            else:
                for j in range(shi):
                    roman_char = roman_char + roman_digit_map[10]
        if ge == 4 or ge == 9 :
            roman_char = roman_char + roman_special_map[ge]
        else:
            if ge >= 5:
                roman_char = roman_char + roman_digit_map[5]
                for j in range(ge - 5):
                    roman_char = roman_char + roman_digit_map[1]
            else:
                for j in range(ge):
                    roman_char = roman_char + roman_digit_map[1]
        return roman_char
    
     
    def isValidSudoku(self, board) -> bool:
        def get_small_9_box(board,x,y):
            data = list()
            for x in range(3):
                for y in range(3):
                    data.append(board[x][y])
            return data
        
        def get_row(board,x,y):
            data = list()
            for y in range(9):
                data.append(board[x][y])
            return data

        def get_column(board,x,y):
            data = list()
            for x in range(9):
                data.append(board[x][y])
            return data

        def check_data_dup(data):
            num_list = list()
            for num in data:
                if num in num_list:
                    return False
                if num == '.':
                    continue
                if int(num) >=0 and int(num) <= 9:
                    num_list.append(num)
            return True
        
        for x in range(9):
            for y in range(9):
                data = get_row(board,x,y)
                if check_data_dup(data):
                    pass
                else:
                    return False
                
        points = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for point in points:
            x_p, y_p = point
            data = get_small_9_box(board,x_p,y_p)
            if check_data_dup(data):
                pass
            else:
                return False
        return True

    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        strings = s.split(' ')
        return len(strings[-1]) 

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(' ')
        while '' in s_list:
            s_list.remove('')
        ret = ""
        for i in range(len(s_list) - 1, -1, -1):
            ret = ret + s_list[i] + " "
        
        return ret.strip()

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp_magazine = magazine
        for i in range(len(ransomNote)):
            if ransomNote[i] in temp_magazine:
                temp_magazine = temp_magazine.replace(ransomNote[i],'',1)
            else:
                return False
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_char = dict()
        for i in range(len(s)):
            if s[i] not in map_char.keys():
                map_char[s[i]] = t[i]
            else:
                if t[i] == map_char[s[i]]:
                    pass
                else:
                    return False
        return True

    def searchMatrix(self, matrix, target: int) -> bool:
        def bio_search(nums, target):
            N = len(nums)
            low = 0
            high = N-1
            while(low <= high):
                mid = (low + high)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                return False
        nums = list()
        m = len(matrix)
        n = len(matrix[0])
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                nums.append(value)
        if len(nums) <= 3:
            return target in nums
        print(nums)
        return bio_search(nums, target)
    


    def simplifyPath(self, path: str) -> str:
        stack = list()
        path_list = path.split('/')
        for item in path_list:
            if item == '/' or item == '.' or item == "":
                continue
            if item == "..":
                if len(stack):
                    stack.pop()
                continue
            stack.append(item)
        ret = "/"
        for item in stack:
            ret = ret + item + '/'
        if ret == "/":
            return ret
        return ret[0:-1]
    
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def get_row_column_of_zero(matrix):
            m = len(matrix)
            n = len(matrix[0])
            zero_list = list()
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        zero_list.append((i,j))
            return zero_list
        row_column_list = get_row_column_of_zero(matrix)
        row_len = len(matrix)
        column_len = len(matrix[0])        
        for row, column in row_column_list:
            for j in range(column_len):  # set row 0
                if matrix[row][j] != 0:
                    matrix[row][j] = 0              
            for i in range(row_len):
                if matrix[i][column] != 0:
                    matrix[i][column] = 0

    def removeNthFromEnd(self, head, n: int):
        def link_length(head):
            index = 0
            while head:
                head = head.next
                index += 1
            return index
        head_back = head
        link_len = link_length(head)
        if link_len <= 1:
            return head
        if link_len == 2 and n == 1:
            return head
        delete_node_no = link_len -n + 1
        prv_delete_node_no = link_len - n
        index = 1
        while index <= prv_delete_node_no:
            if index != prv_delete_node_no:
                head = head.next
            else:
                head.next = head.next.next
                break
            index += 1
        return head_back

    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                if nums[idx1] == nums[idx2]:
                    if abs(idx1 - idx2) <= k:
                        return True
        else:
            return False
        
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0, None)
        head_bak = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1 is None:
            head.next = list2
        else:
            head.next = list1
        return head_bak.next

    def addTwoNumbers(self, l1, l2):
        def get_number(link):
            num_str = ""
            while link:
                num_str = num_str + str(link.val)
                link = link.next
            return int(num_str[::-1])
        num1 = get_number(l1)
        num2 = get_number(l2)
        sum = num1 + num2
        sum_str = str(sum)[::-1]
        l1_head = l1
        ret_l1 = l1
        while l1:
            l1_tail = l1
            l1 = l1.next
        l1_tail.next = l2
        i = 0
        while l1_head:
            l1_head.val = int(sum_str[i])
            i += 1
            if len(sum_str) == i:
                l1_head.next = None
                break
            else:
                l1_head = l1_head.next
        return ret_l1
    def minPathSum(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1,row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

    def plusOne(self, digits):
        digit_str = ""
        for i in range(len(digits)):
            digit_str = digit_str + str(digits[i])
        result = str(int(digit_str) + 1)
        new_digits = list()
        for i in range(len(result)):
            new_digits.append(int(result[i]))
        return new_digits

    def canCompleteCircuit(self, gas, cost) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            cur_sum = cur_sum + gas[i] - cost[i]
            total_sum = total_sum + gas[i] - cost[i]
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        if total_sum < 0:
            return -1
        return start         

    def hasPathSum(self, root, targetSum: int) -> bool:
        pass

    def maxDepth2(self, root) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
    def isSameTree(self, p ,  q) -> bool:
        if p is None or q is None:
            return p is q
        return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)

    def invertTree2(self, root):
        if root is None:
            return root
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def threeSum(self, nums):
        ret_list = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        candidate = sorted([nums[i],nums[j],nums[k]])
                        if candidate not in ret_list:
                            ret_list.append(candidate)                    
        return ret_list
    
    def evalRPN(self, tokens) -> int:
        if len(tokens) <= 1:
            return int(tokens[-1])
        digits = [str(i) for i in range(-200,201,1)]
        stack = list()
        for i in range(len(tokens)):
            if tokens[i] in digits:
                stack.append(tokens[i])
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                match tokens[i]:
                    case "+":
                        value = op1 + op2
                    case '-':
                        value = op2 - op1
                    case "*":
                        value = op1 * op2
                    case '/':
                        value = int(op2 / op1)
                stack.append(value)
        return stack.pop()

    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False
        if s[0] in [')', ']', '}']:
            return False
        stack = list()
        for i in range(len(s)):
            match s[i]:
                case '(' | '{' | '[':
                    stack.append(s[i])
                    continue
                case ')':
                    if len(stack) == 0 or stack[-1] != "(":
                        return False
                case ']':
                    if len(stack) == 0 or stack[-1] != "[":
                        return False
                case '}':
                    if len(stack) == 0 or stack[-1] != "{":
                        return False
            stack.pop()
        if len(stack)>0:
            return False                
        return True
    
    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(root, targetSum, sum):
            if root is None:
                return False
            sum = sum + root.val
            if root.left is None and root.right is None:
                return sum == targetSum
            left = dfs(root.left, targetSum, sum)
            right = dfs(root.right, targetSum, sum)
            return left or right
        return dfs(root, targetSum, 0)
    
    def sumNumbers(self, root) -> int:
        def dfs(root, str_ph, my_list):
            if root is None:
                return ""
            str_ph = str_ph + str(root.val)
            if root.left is None and root.right is None:
                return my_list.append(int(str_ph))
            dfs(root.left, str_ph, my_list)
            dfs(root.right, str_ph, my_list)
            return mylist
        mylist = list()
        dfs(root, "", mylist)
        ret = 0
        for num in mylist:
            ret = ret + num
        return ret

    def countNodes(self, root) -> int:
        if root.left is None and root.right is None:
            return 1
        if root.right is not None:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        else:
            return self.countNodes(root.left) + 1

    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict.keys():
                if s_list[i] not in pattern_dict.values():
                    pattern_dict[pattern[i]] = s_list[i]
                else:
                    return False
            else:
                if pattern_dict[pattern[i]] != s_list[i]:
                    return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_p = 0
        while t_p < len(t):
            if t[t_p] in s:
                s = s.replace(t[t_p], '', 1)
            else:
                return False
            t_p = t_p + 1
        return True
    
    def levelOrder(self, root):
        result = list()
        queue = list()
        if root is None:
            return result
        queue.append(root)
        while(len(queue)):
            size = len(queue)
            level = list()
            for _ in range(size): 
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                level.append(node.val)
            result.append(level)
        return result

    def longestCommonPrefix(self, strs) -> str:
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min(len(str) for str in strs)
        for i in range(min_len):
            char_list_i = list()
            for str in strs:
                char_list_i.append(str[i])
            dedup = set(char_list_i)
            if len(dedup) > 1:
                return strs[0][:i]
        else:
            return strs[0][:i+1]

    def strStr(self, haystack: str, needle: str) -> int:
        n_p = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[n_p]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1

    def canJump(self, nums) -> bool:
        if len(nums)<=1:
            return True
        cover = 0
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i+nums[i], cover)
                if cover >= len(nums) - 1:
                    return True
        return False

    def reverseBetween(self, head, left: int, right: int):
        from copy import deepcopy
        def reverseLink(cur, pre):
            if cur is None:
                return pre
            temp = cur.next
            cur.next = pre
            return reverseLink(temp, cur)
        
        def cut_link(head, left, right):
            index = 1
            while(index<right):
                if index == left:
                    ret_head = head
                head = head.next
                index += 1
            else:
                ret_tail = head
            old_tail = head
            new_head = deepcopy(ret_head)
            re_idx = 0
            bak_head = new_head
            while(re_idx<=right-left-1):
                bak_head = bak_head.next
                re_idx+=1
            else:
                bak_head.next = None
            return new_head, old_tail.next
        
        def get_prenode_with_num(head, num):
            if num == 1:
                return head
            idx = 1
            while(idx<num-1):
                head=head.next
                idx+=1
            return head
        
        def get_postnode_with_num(head, num):
            if num == 1:
                return head
            idx = 1
            while(idx<=num):
                head=head.next
                idx+=1
            return head   

        def goto_link_end(head):
            while(head.next):
                head = head.next
            return head

        if left == right:
            return head
        
        bak_head = head
        len = 0
        while(head):
            head=head.next
            len+=1
        head = bak_head
        if len == 2:
            first = head
            second = head.next
            second.next = head
            head.next = None
            return second
        
        new_head, old_tail = cut_link(head, left, right)
        reversed_link_head = reverseLink(new_head, None)
        search_head = bak_head
        pre_left_node = get_prenode_with_num(search_head, left)
        search_head = bak_head
        post_right_node = get_postnode_with_num(search_head, right)
        pre_left_node.next = new_head
        bak_new_head = reversed_link_head

        if left == 1:
            end = goto_link_end(reversed_link_head)
            end.next = post_right_node
            bak_head = bak_new_head
            return bak_head
        idx = 1
        while(idx<=right):
            if idx == left-1:
                head.next = reversed_link            
            head=head.next
            idx+=1
        while(reversed_link.next):
            reversed_link = reversed_link.next
        reversed_link.next = post_right_node
        return bak_head

    def summaryRanges(self, nums):
        if len(nums) == 0:
            return [] 
        if len(nums) == 1:
            return [str(nums[0])]
        mid_result = list()
        result = list()
        arrow="->"
        start = 0

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                mid_result.append([nums[start],nums[i-1]])
                start = i
            else:
                if i == len(nums) - 1:
                    mid_result.append([nums[start],nums[i]])
        if start == len(nums) - 1:
            mid_result.append([nums[start], nums[start]])

        for item in mid_result:
            if item[0] != item[1]:
                string = str(item[0]) + arrow + str(item[1])
                result.append(string)
            else:
                string = str(item[0])
                result.append(string)
        return result  

    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        string = str(x)
        start = 0
        end = len(string)-1
        while(start<=end):
            if string[start] == string[end]:
                start+=1
                end-=1
            else:
                return False
        return True

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def dfs(i,j, char):
            if i<0 or j<0 or i>m-1 or j>n-1 or board[i][j] == 'X' or board[i][j] == char:
                return
            if board[i][j] == 'O':
                board[i][j] = char
            dfs(i-1,j, char)
            dfs(i+1,j, char)
            dfs(i,j-1, char)
            dfs(i,j+1, char) 

        for i in range(0, m):
            for j in range(0, n):
                if(i==0 or j==0  or i==m-1 or j==n-1):
                    dfs(i,j,'e')

        for i , row in enumerate(board):
            for j, c in enumerate(row):
                if c=='O':
                    dfs(i,j, 'X')

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'e':
                    board[i][j] = 'O'   
    def addBinary(self, a: str, b: str) -> str:
        a10 = int(a,2)
        b10 = int(b,2)
        return bin(a10+b10)[2:]

    def isPalindrome2(self, s: str) -> bool:
        process_s = list()
        for char in s:
            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <='Z') or (char >= '0' and char <= '9'):
                process_s.append(char.lower())
        start = 0
        end = len(process_s) - 1
        while(start<=end):
            if process_s[start] != process_s[end]:
                return False
            start+=1
            end-=1
        else:
            return True
    
    def isSubsequence(self, s: str, t: str) -> bool:
        last_pos = -1
        for i in s:
            if i in t:
                pos = t.find(i, last_pos )
                t = t.replace(i,"0",1)
                if pos < last_pos:
                    return False
                else:
                    last_pos = pos
            else:
                return False
        return True
    
        
    def rob(self, nums) -> int:
        dp = list()
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))
        return dp[-1]

    def missingNumber(self, nums) -> int:  
        nums.sort()
        for i in range(nums[0], nums[-1]):
            if i in nums:
                continue
            else:
                return i
    
    def groupAnagrams(self, strs):
        import copy
        def verify_same_chars(str1, str2):
            if len(str1) != len(str2):
                return False
            for char in str1:
                if char in str2:
                    str2 = str2.replace(char,"",1)
                else:
                    return False
            return True
        def remove_item_from_list(item, strs):
            new_list = list()
            for each in strs:
                if each == item:
                    continue
                else:
                    new_list.append(each)
            return new_list
            
        strs2 = copy.deepcopy(strs)
        word_char_map = {}
        idx = 0
        for word in strs:
            word_list = list()
            
            for word1 in strs2:
                if verify_same_chars(word, word1):
                    word_list.append(word1)
                    word_char_map[idx] = word_list
                    #strs2 = remove_item_from_list(word1, strs2)
            idx += 1
 
        result = list()
        for _, value in word_char_map.items():
            if value not in result:
                result.append(value)
        return result
    def findKthLargest(self, nums, k: int):
        nums.sort()
        return nums[len(nums)-k]
    
    def kSmallestPairs(self, nums1, nums2, k: int):
        sum_map = {}
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in sum_map.keys():
                    exist_sum_list = sum_map[sum]
                    exist_sum_list.append([num1,num2])
                    continue      
                sum_list = list()
                sum_list.append([num1, num2])
                sum_map[num1+num2] = sum_list
        keys = list(sum_map.keys())
        keys.sort()
        result = list()
        idx = 0
        for key in keys:
            sum_list = sum_map[key]
            for item in sum_list:
                result.append(item)
                idx+=1
                if idx >= k:
                    return result
                
    def deleteDuplicates(self, head):
        prev = None
        cur = head
        while cur is not None:
            if prev:
                if prev.val == cur.val:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    prev = cur
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head    
    
    def generate(self, numRows: int):
        def create_list(num):
            row = [ 1 for i in range(num)]
            return row
        ans = dict()
        ans[0] = [1]
        ans[1] = [1,1]
        for i in range(2, numRows):
            row = create_list(i+1)
            for j in range(1, i):
                cal_row = ans[i-1]  
                sum = cal_row[j] + cal_row[j-1]
                row[j] = sum
            ans[i] = row
        result = list()
        for value in ans.values():
            result.append(value)
        return result[0:numRows]

    def getMinimumDifference(self, root) -> int:
        def dfs(root, ans):
            if root is None:
                return root
            ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)
        
        ans = list()
        dfs(root,ans)
        min = abs(ans[0] - ans[1])
        for i in range(0, len(ans)):
            for j in range(i+1, len(ans)):
                if min > abs(ans[i] - ans[j]):
                    min = abs(ans[i] - ans[j])
        return min

    def minDepth(self, root) -> int:
        if root is None:
            return 1
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)
        return min(left, right)




    def isHappy(self, n: int) -> bool:
        square = lambda x : x*x
        str_n = str(n)
        sum = 0
        result = dict()
        while True:
            sum = 0
            for i in range(len(str_n)):
                sum = sum + square(int(str_n[i]))
            print(" for {}, sum is {} ".format(n, sum))
            if sum == 1:
                return True
            else:
                if sum in result.keys():
                    return False
                result[sum] = 0
            str_n = str(sum)

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        def div2(n):
            if n % 2 != 0:
                return False
            if n  == 2:
                return True
            return div2(n/2)
        return div2(n)        

    def binaryTreePaths(self, root):
        def dfs(root, path, result):
            if root is None:
                return
            path = path + str(root.val)
            if root.left is None and root.right is None:
                result.append(path)
            else:
                path = path + "->"
                dfs(root.left, path, result)
                dfs(root.right, path, result)
        path = ""
        result = list()
        dfs(root, path, result)
        return result           
    
    def inorderTraversal(self, root):
        def dfs(root, res):
            if root is None:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        ans = list()
        dfs(root, ans)
        return ans

    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            str_num = str(num)
            sum = 0
            for number in str_num:
                sum = sum + int(number)
            return self.addDigits(sum)
        
    def firstBadVersion(self, n: int) -> int:
        nums=[True, True, True, True, True, False, False, False,False]
        def isBadVersion(index):
            return nums[index]
        start = 0
        high = n
        while start <= high:
            mid = (start + high) // 2
            print("start = {}, high = {}, mid = {}".format(start, high, mid))
            mid_correctness = isBadVersion(mid)
            if mid_correctness :
                if not isBadVersion(mid+1):
                    return mid + 1
                else:
                    start = mid + 1
            else:
                if isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid -1 

    def sumOfLeftLeaves(self, root) -> int:
        def isLeafNode(node):
            if node.left is None and node.right is None:
                return True
            return False
        def dfs(cur, ans):
            if cur is None:
                return
            if cur.left and isLeafNode(cur.left):
                ans.append(cur.left.val)
            dfs(cur.left, ans)
            dfs(cur.right, ans)
        my_list = list()
        dfs(root, my_list)
        sum = 0
        for i in my_list:
            sum = sum + i
        return sum  

    def longestPalindrome(self, s: str) -> int:
        char_map = dict()
        for i in s:
            if i not in char_map.keys():
                char_map[i] = 1
            else:
                char_map[i] = char_map[i] + 1
        length = 0
        odd_list = list()
        if len(char_map.keys()) == 1:
            values = list(char_map.values())
            return values[0]
        for key, value in char_map.items():
            if value % 2 == 0:
                length = length + value
            else:
                odd_list.append(value)
        if len(odd_list) > 0:
            for val in odd_list:
                if val > 1:
                    length = length + val -1
        else:
            return length
                
        return length+1

    def thirdMax(self, nums) -> int:

        nums = list(set(nums))
        nums.sort()
        print(nums)        
        if len(nums) == 3:
            return nums[0]
        if len(nums) > 3:
            return nums[-3]
        else:
            return nums[-1]
        
    def addStrings2(self, num1: str, num2: str) -> str:  
        def add(str1, str2):
            idx = len(str1) - 1
            result = ""
            add = 0
            while idx >= 0:
                sum = int(str1[idx]) + int(str2[idx]) + add
                if sum >= 10:
                    add = 1
                    sum = sum - 10
                else:
                    add = 0
                idx -= 1
                result = result + str(sum)
            if add:
                return '1'+ result[::-1]
            else:
                return result[::-1] 
        
        def add1(str1):
            idx = len(str1) - 1
            result = ""
            add = 0
            while idx >= 0:
                if add == 0:
                    sum = int(str1[idx]) + 1 + add
                else:
                    sum = int(str1[idx]) + add
                if sum >= 10:
                    add = 1
                    sum = sum - 10
                else:
                    add = 0
                result = result + str(sum)
                if add:
                    idx -= 1
                else:
                    return str1[0:idx] + result[::-1]
            else:
                return '1' + result[::-1]

        len1 = len(num1)
        len2 = len(num2)
        if len1 == len2:
            return add(num1, num2)
        else:
            if len1 > len2:
                 part1 = add(num1[-len2:], num2)
                 if len(part1) > len2:
                    left = num1[0:len1-len2]
                    result = ""
                    result = result + add1(left)
                    return  result+part1[1:]
                 else:
                     return num1[0:len1-len2] + part1
            else:
                num1,num2 = num2,num1
                len1,len2 = len2, len1
                part1 = add(num1[-len2:], num2)
                if len(part1) > len2:
                    left = num1[0:len1-len2]
                    result = add1(left)
                    return  result+part1[1:]
                else:
                    return num1[0:len1-len2] + part1
            
    def addStrings(self, num1: str, num2: str) -> str:  
        def add(str1, str2):
            idx = len(str1) - 1
            result = ""
            add = 0
            while idx >= 0:
                sum = int(str1[idx]) + int(str2[idx]) + add
                if sum >= 10:
                    add = 1
                    sum = sum - 10
                else:
                    add = 0
                idx -= 1
                result = result + str(sum)
            if add:
                return '1'+ result[::-1]
            else:
                return result[::-1] 
        len1 = len(num1)
        len2 = len(num2)
        if len1 == len2:
            return add(num1, num2)
        else:
            if len1 > len2:
                zeors = '0' *(len1-len2)
                result = add(num1, zeors+num2)
            else:
                zeors = '0' *(len2-len1)
                result = add(num2, zeors+num1)
            return result

    def reverseVowels(self, s: str) -> str:
        CHAR_LIST = ['a','e','i','o','u','A','E','I','O','U']
        char_list = list()
        for i in s:
            if i in CHAR_LIST:
                char_list.append(i)
        idx = len(char_list) - 1
        ans = ""
        for i in s:
            if i in CHAR_LIST:
                ans = ans + char_list[idx]
                idx -= 1
            else:
                ans=ans+i
        return ans

    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        num_map = dict()
        index = 0
        for i in nums:
            if i not in num_map.keys():
                idx_list = list()
                idx_list.append(index)
                num_map[i] = idx_list
            else:
                num_map[i].append(index)
            index += 1
        for key,value in num_map.items():
            if len(value) > 1:
                value.sort()
                for i in range(len(value)):
                    for j in range(i+1, len(value)):
                        if abs(value[i]-value[j]) <= k:
                            return True
        return False

    def findPoisonedDuration(self, timeSeries, duration) -> int:
        ans = 0
        last = 0
        for i in range(len(timeSeries)):
            if i == 0:
                last = timeSeries[i]
                ans = 1
            else:
                ans = ans + min(last + duration, timeSeries[i]-timeSeries[i-1]+1)
        return ans
            

    def countSegments(self, s: str) -> int:
        s_list = s.split(' ')
        ans = 0
        for word in s_list:
            if word != "":
                ans += 1
        return ans

    def numCells(self, grid):
        # Write your code here
        def generate_cor(i,j,m,n):
            full_list = [[i+1,j+1],[i-1,j-1],[i,j+1],[i,j-1],[i-1,j],[i+1,j],[i+1,j-1],[i-1,j+1]]
            result = list()
            for item in full_list:
                if item[0] < 0 or item[1] < 0 or item[0] >= m or item[1]>=n:
                    continue
                else:
                    result.append(item)
            return result
            
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(0,m):
            for j in range(0,n):
                cell = grid[i][j]
                neighbor_list = generate_cor(i,j,m,n)
                first_cor = neighbor_list[0]
                max_neighbor = grid[first_cor[0]][first_cor[1]]
                for cordal in neighbor_list:
                    if grid[cordal[0]][cordal[1]] > max_neighbor:
                        max_neighbor = grid[cordal[0]][cordal[1]]
                if cell > max_neighbor:
                    ans += 1
        return ans

    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 0
        row = 1
        while n - row >= 0:
            ans += 1
            n = n - row
            row += 1
            
        return ans

    def nextGreaterElement(self, nums1, nums2):
        ans = list()
        for num1 in nums1:
            try:
                idx = nums2.index(num1)
                if idx+1 <len(nums2):
                    for i in nums2[idx:]:
                        if i > num1:
                            ans.append(i)
                            break
                    else:
                        ans.append(-1)
                else:
                    ans.append(-1)
            except ValueError:
                ans.append(-1)
        return ans
    
    def numIslands(self, grid) -> int:
        def dfs(grid, i,j,m,n):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] != '1':
                return 
            grid[i][j] = 2
            dfs(grid, i+1, j,m,n)
            dfs(grid, i-1, j,m,n)
            dfs(grid, i, j+1, m, n)
            dfs(grid, i, j-1, m, n)
        m = len(grid)
        n = len(grid[0])

        result = 0
        for i, row in  enumerate(grid):
            for j, c in enumerate(row):
                if c=='1':
                    dfs(grid, i,j,m,n)
                    result += 1
        return result

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(cur, ans):
            if cur is None:
                return
            ans.append(cur.val)
            traverse(cur.left, ans)
            traverse(cur.right, ans)
        ans = list()
        traverse(root, ans)
        if len(ans) == 0:
            return []
        head = TreeNode(ans[0])
        pre = head
        idx = 1
        while idx < len(ans):     
            node = TreeNode(ans[idx])
            idx += 1
            pre.right = node
            pre = node
        return head

    def productExceptSelf(self, nums):
        ans = list()
        caculated_map = dict()
        def multiple(a_list):
            result = 1
            for i in a_list:
                result = result * i
            return result
        def copy_nums(nums, idx):
            result = list()
            for i in range(len(nums)):
                if i != idx:
                    result.append(nums[i])
            return result
        N = len(nums)
        idx = 0
        while idx < N:
            if nums[idx] in caculated_map.keys():
                ans.append(caculated_map[nums[idx]])
                idx += 1
                continue
            new_list = copy_nums(nums, idx)
            last = multiple(new_list)
            ans.append(last)
            caculated_map[nums[idx]] = last           
            idx += 1
           
        return ans

    def minSubArrayLen(self, target, nums) -> int:
        sum = 0
        N = len(nums)
        left = 0
        ans = N
        set = False
        for right in range(N):
            sum = sum + nums[right]
            while sum >= target:
                set = True
                ans = min(ans, right - left + 1)
                sum = sum - nums[left]
                left+=1
        if set:
            return ans
        else:
            return 0

    def dailyTemperatures(self, temperatures):
        ans = dict()
        result = list()
        st = list()
        N = len(temperatures)
        for idx in range(N):
            if idx == 0 :
                st.append(idx)
                continue
            while(len(st)>0 and temperatures[idx] > temperatures[st[-1]]):
                ans[st[-1]] = idx - st[-1]
                st.pop()
            else:
                st.append(idx)
        for idx in st:
            ans[idx] = 0
        keys = list(ans.keys())
        keys.sort()
        for key in keys:
            result.append(ans[key])
        return result

    def maxProfit(self, prices) -> int:
        #dp[i] means: NO. i day, max money
        N = len(prices)
        dp = dict()
        for i in range(N):
            dp[i] = 0
        
        dp[0] = 0
        min_price = prices[0]
        for i in range(1, N):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            if min_price > prices[i]:
                min_price = prices[i]
        return dp[N-1]      

    def maxArea(self, height) -> int:
        N = len(height)
        left = 0
        right = N - 1
        size = 0
        while left < right:
            width = right - left 
            h = min(height[left], height[right])
            size = max(size, width*h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return size    
      
    def maximizeSum(self, nums, k: int) -> int:
        idx = 0
        sum = 0
        while idx < k:
            nums.sort()
            biggest = nums.pop()
            new = biggest + 1
            sum = sum + biggest
            nums.append(new)
            idx += 1
        return sum

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = list()
        left = 0
        right = 0
        N = len(s)
        size = 0
        while (right<N):
            if s[right] not in window:
                window.append(s[right])
                size = max(size, len(window))
            else:
                idx = window.index(s[right])
                left = left + idx + 1
                window = window[idx+1:]
                window.append(s[right])
            right += 1
        return size

    def twoSum(self, nums, target: int):
        import copy
        new_nums = copy.deepcopy(nums) 
        nums.sort()
        left = 0
        N = len(nums)
        right = N - 1
        while (nums[left] + nums[right] != target):
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        if nums[left] == nums[right]:
            return [new_nums.index(nums[left]), new_nums.index(nums[right],new_nums.index(nums[left])+1)]
        else:
            return [new_nums.index(nums[left]), new_nums.index(nums[right])]

    def getRow(self, rowIndex: int):
        trangle = dict()
        trangle[0] = [1]
        trangle[1] = [1,1]
        for idx in range(2, rowIndex+1):
            row = list()
            last_row = trangle[idx-1]
            row.append(1)
            for i in range(1, len(last_row)):
                row.append(last_row[i]+last_row[i-1])
            row.append(1)
            trangle[idx] = row
        return trangle[rowIndex]    

    def hIndex(self, citations) -> int:
        N = len(citations)
        max_cita = max(citations)
        calc = dict()
        for i in range(max_cita+1):
            idx = 0
            for j in citations:
                if j>=i:
                    idx += 1
            calc[i] =idx
        h_candidate = 0
        for key, value in calc.items():
            h_candidate = max(h_candidate, min(N, key, value))

        return h_candidate

    def sortList(self, head):
        val_list = list()
        node = head
        while node is not None:
            val_list.append(node.val)
            node = node.next
        val_list.sort()
        node = head
        for val in val_list:
            node.val = val
            node = node.next
        return head

    #No.283
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i],nums[j] = nums[j], nums[i]

    #No.605
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        import copy
        dp = copy.deepcopy(flowerbed)
        N = len(dp)
        if n==0:
            return True
        if N == 1:
            dp[0] = not dp[0]
            print(dp)
            return (dp.count(1) - flowerbed.count(1) >=n )
        if dp[0] == 0 and dp[1] == 0:
            dp[0] = 1        
        for i in range(1, N-1):    
            if not (dp[i-1] or dp[i+1]):
                dp[i] = 1
            else:
                dp[i] = 0
        if dp[N-2] == 0:
            dp[N-1] = 1        
        print(dp)
        return (dp.count(1) - flowerbed.count(1) >=n )

    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        cnt=1
        max_size = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cnt += 1
            else:
                max_size = max(max_size, cnt)
                cnt = 1
        else:
            max_size = max(max_size, cnt)
        return max_size

    def copyRandomList(self, head):
        import copy
        cur = head
        node_list = list()
        random_list = list()
        while cur:
            node = copy.deepcopy(cur)
            node_list.append(node)
            random_node = copy.deepcopy(cur.random)
            random_list.append(random_node)
            cur = cur.next
        N = len(node_list)
        cur = head
        print(node_list)
        print(random_list)
        for idx in range(N-1):
            node_list[idx].next = node_list[idx+1]
        node_list[N-1].next = node_list[N-1]
        for idx in range(N-1):
            node_list[idx].random = random_list[idx]
        node_list[N-1].random = random_list[N-1]
        return node_list[0]
    #No.459
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s + s
        search_s = s2[1:-1]
        if s in search_s:
            return True
        else:
            return False

    #No.643
    def findMaxAverage(self, nums, k: int) -> float:
        N = len(nums)
        window = list()
        total = -1000000000000000000000
        s = 0
        idx = 0
        while idx < N:
            if len(window) < k:
                window.append(nums[idx])
                s = s + nums[idx]
                if len(window) == k:
                    total = max(total, s)
                    head = window.pop(0)
                    s = s - head
            idx += 1
        return total/k
    
    #No.110
    def isBalanced(self, root) -> bool:
        def recur(root):
            if not root: 
                return 0
            left = recur(root.left)
            if left == -1: 
                return -1
            right = recur(root.right)
            if right == -1: 
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
    
    #No.645
    def findErrorNums(self, nums):
        N = len(nums)
        nums.sort()
        dup = -1
        miss = -1
        for i in range(N):
            if i+1 not in nums:
                miss = i + 1
            if nums[i] == nums[i-1]:
                dup = nums[i]    
        return [dup, miss]
    
    #No.965
    def isUnivalTree(self, root) -> bool:
        def dfs(node, val):
            if node is None:
                return 
            if node.val != val:
                return False
            left = dfs(node.left, val)
            right = dfs(node.right, val)
            if left != False and right != False:
                return True
            else:
                return False
        return dfs(root, root.val)

    #No.189
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        ans = [0 for i in range(N)]
        for idx in range(N):
            ans_idx = (idx + k) % N 
            ans[ans_idx] = nums[idx]
        for idx in range(N):
            nums[idx] = ans[idx]

    #No.697
    def findShortestSubArray(self, nums) -> int:
        digit_map = dict()
        idx  = 0
        for i in nums:
            if i not in digit_map.keys():
                digit_map[i] = [idx]
            else:
                digit_map[i].append(idx)
            idx += 1
        du = 0
        for _, value in digit_map.items():
            du = max(du, len(value))
        du_list = [ value for value in digit_map.values() if len(value) == du]
        min_ = 100000
        for value in du_list:
            min_ = min(min_, value[-1] - value[0])
        return min_+1
    
    #No.387
    def firstUniqChar(self, s: str) -> int:
        N = len(s)
        digit_map = dict()
        idx = 0
        for char in s:
            if char not in digit_map.keys():
                spec = list() 
                spec.append(idx)
                digit_map[char] = spec
            else:
                digit_map[char].append(idx)
            idx += 1
        min_idx = N+1
        for key, value in digit_map.items():
            if len(value) == 1:
                min_idx = min(min_idx, value[0])
        if min_idx == N+1:
            return -1
        return min_idx
        
    #No.485
    def findMaxConsecutiveOnes(self, nums) -> int:
        N = len(nums)
        window = 0
        idx = 0
        max_1 = 0
        while idx < N:
            if nums[idx] == 1:
                window+=1
            else:
                max_1 = max(max_1, window)
                window = 0
            idx += 1
        return max(max_1,window)

    #No.520
    def detectCapitalUse(self, word: str) -> bool:
        UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        LOWER = "abcdefghijklmnopqrstuvwxyz"
        N = len(word)
        char_dict = {'U':0, 'L':0}
        for i in word:
            if i in UPPER:
                char_dict['U'] += 1
            else:
                char_dict['L'] += 1
        if word[0] in LOWER:
            if char_dict['U'] > 0:
                return False
            else:
                return True
        else:
            if char_dict['U'] == N:
                return True
            if char_dict['L'] > 0 and char_dict['L'] != N - 1:
                return False
            else:
                return True
    #No.206
    def reverseList(self, head):
        p = None
        q = head
        while q.next:
            p = q
            next = p.next
            q.next = p
            q = next
        return q

    #No.500
    def findWords(self, words):
        def word_in_line(word, line):
            idx = 0
            N = len(word)
            for idx in range(N):
                if word[idx] not in line:
                    return False
            else:
                return True


        line1 = "qwertyuiopQWERTYUIOP"
        line2 = "asdfghjklASDFGHJKL"
        line3 = "zxcvbnmZXCVBNM"
        result = list()
        for word in words:
            for line in [line1, line2, line3]:
                if word_in_line(word, line):
                    result.append(word)
        return result        

from leet_code_util import *

if __name__=="__main__":


    # root = TreeNode.buildTree(preorder, inorder)

    solution = Solution()
    #solution.merge(list1, m, list2, n)
    #inorder = [3,2,4,1,5,6]
    #postorder = [3,4,2,6,5,1]
    #postorder = [5,1,1,2,6,3,8,-1,4,0]
    #inorder = [5,1,1,2,0,3,6,4,-1,8]
    #targetSum = 22
    #root=TreeNode.buildTree2(inorder, postorder)
    #nums = [2,3,1,1,4]
    #link_list = [2,3,3]
    link_list = [1,2,3,4]
    link = buid_list_node(link_list)
    #head = buid_list_node2([[7,None],[13,0],[11,4],[10,2],[1,0]])
    words = ["Hello","Alaska","Dad","Peace"]
    #numRows = 5
    print(solution.findWords(words))

    #q = solution.reverseList(link)
    #while(q):
    #    print(q.val)
    #    q=q.next


    

    
    