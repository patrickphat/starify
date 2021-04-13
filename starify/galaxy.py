import math

def star(string:str, star_percent:float = 0.6, max_len:int = 25, star_head=True):
    ori_str_len = len(string)
    
    # Trimming for too long string
    if ori_str_len <= max_len:
        new_str_len = ori_str_len
    else:
        new_str_len = max_len
    
    if star_head:
        string = string[ori_str_len-new_str_len:]
    else:
        # Trim tail
        string = string[:new_str_len]
    
    # Starify!
    num_star = math.ceil(new_str_len*star_percent)

    if star_head:
        string = num_star * "*" + string[ num_star:]
    else:
        string = string[:new_str_len - num_star]  + num_star * "*"

    return string
