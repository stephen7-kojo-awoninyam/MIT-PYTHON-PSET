# Problem Set 4A
# Name: <Awinenyam Kojo Stephen>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
         return [sequence]
    
    else:
         perm = []

         last = sequence[-1]

         sequence = sequence[:-1]

         prev_perm_list = get_permutations(sequence)

         for p in prev_perm_list:
              
              for pos in range(0,len(p)+1):
                   
                   new = p[pos:] + last + p[:pos]

                   perm.append(new)

    return perm

print(get_permutations('abc'))