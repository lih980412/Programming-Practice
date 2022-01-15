# 找出第二个字符串在第一个字符串中第一次出现的下标

haystack = "hello"
needle = "ll"

# int strStr(string haystack, string needle) {
#     'C++解法'
#     int m = haystack.size()
#     int n = needle.size()
#
#     for(int i=0; i+n<=m; i++)     # 判断 i+n<=m 而不是 i<n，可以减少开销
#     {
#         bool flag = true;
#         for(int j=0; j<n; j++)
#         {
#             if(haystack[i+j] != needle[j])
#             {
#                 flag = false;
#                 break;
#             }
#         }
#         if(flag)
#             return i;
#     }
#     return -1;
# }