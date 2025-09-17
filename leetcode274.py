'''Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
'''

def h_index(citations):
      ## sorting in descending order
        ## use a count 
        ## taking a loop to check the value of array is equal and greater than their indices if yes increment in count.
        ## num + 1 because index start from 1 instead of 0 
    citations.sort(reverse = True)
        # print(citations)
        # if len(citations) == 1:
            # return citations

    count = 0
    for num in range(len(citations)):
        if citations[num] >= num +1:
            count += 1
               
    return count

citations = [3,0,6,1,5]
print(h_index(citations))



       