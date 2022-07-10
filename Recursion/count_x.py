
def count_xs(str,count=0):
    # problem axbxcxd
    # subproblem xbxcxd
    if len(str) == 0:
        return count
    else:
        if str[0] == 'x':
            count += 1 
        return count_xs(str[1:],count)

print(count_xs("xaxbxcxdx"))