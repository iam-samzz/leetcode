class Solution:
    def findUnion(self, a, b):

        p1 = 0
        p2 = 0

        l1 = len(a)
        l2 = len(b)

        ans = []

        while p1 < l1 and p2 < l2:

            if a[p1] < b[p2]:
                x = a[p1]
                ans.append(x)

                while p1 < l1 and a[p1] == x:
                    p1 += 1

            elif b[p2] < a[p1]:
                x = b[p2]
                ans.append(x)

                while p2 < l2 and b[p2] == x:
                    p2 += 1

            else:
                x = a[p1]
                ans.append(x)

                while p1 < l1 and a[p1] == x:
                    p1 += 1

                while p2 < l2 and b[p2] == x:
                    p2 += 1

        while p1 < l1:
            x = a[p1]
            ans.append(x)

            while p1 < l1 and a[p1] == x:
                p1 += 1

        while p2 < l2:
            x = b[p2]
            ans.append(x)

            while p2 < l2 and b[p2] == x:
                p2 += 1

        return ans