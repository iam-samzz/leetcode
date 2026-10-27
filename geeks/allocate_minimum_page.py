# allocate minimum page - binary search

class Solution:
    def findPages(self, arr, k):
        """
        Uses binary search on the possible range of maximum pages to find
        the minimum required capacity such that 'k' students can be accommodated.
    
        Args:
            arr (list[int]): A list where each element represents the number of pages in a book.
            k (int): The number of students available.
        Returns:
            int: The minimum maximum number of pages assigned to any student,
                  or potentially handles edge cases if constraints are violated.
        """
        # Get the total number of books/elements
        n = len(arr)
        
        # Edge case: If more students than books, something is likely wrong with inputs
        # or constraints given the nature of this problem (though standard competitive programming
        # setups usually ensure k >= 1 and k <= n). Returning -1 as per original logic.
        if k > n:
            return -1

        # The minimum possible answer (low bound) is the largest single book size,
        # because at least one student must take that book.
        low = max(arr)
        # The maximum possible answer (high bound) is the sum of all pages (one student takes everything).
        high = sum(arr)

        min_page = None

        # Binary search for the minimum feasible 'mid' value
        while low <= high:
            mid = (low + high) // 2
           
            # Check if it is possible to allocate all books such that no student gets more than 'mid' pages,
            # using at most 'k' students.
            if self.check_max_page(mid, k, arr):
                # If feasible (True), this 'mid' could be the answer. Store it and try for an even smaller max page size.
                min_page = mid
                high = mid - 1
            else:
                # If not feasible (False), the maximum allowed pages ('mid') is too small; we must increase it.
                low = mid + 1
        return min_page
    
    def check_max_page(self, mid , k , arr):
        """
        Greedy approach to check if all books can be allocated among at most 'k' students
        such that no student exceeds 'mid' total pages.

        Args:
            mid (int): The maximum allowed page limit per student (the capacity being tested).
            k (int): The maximum number of students allowed.
            arr (list[int]): The book sizes/pages.
        Returns:
            bool: True if allocation is possible with <= k students, False otherwise.
        """
        n = len(arr)
        students = 1  # Start with the first student
        pages = 0     # Pages accumulated by the current student
        for i in range(n):
            # Check if adding the current book fits within the limit 'mid'
            if pages + arr[i] <= mid:
                pages += arr[i]  # Add to the current student's load
            else:
                # Current student cannot take this book, so a new student must be assigned.
                students += 1
                pages = arr[i]   # The new student starts with the current book

        # If at any point an individual book (arr[i]) is greater than 'mid', the logic above fails
        # because we implicitly assume low >= max(arr). If this were not guaranteed,
        # an explicit check for arr[i] > mid would be needed here.

        # Check if the total number of students required is less than or equal to 'k'
        if students <= k:
            return True
        else:
            return False    
