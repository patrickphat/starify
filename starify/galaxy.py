import math

def star(string:str, percent_star:float = 0.6, max_len:int = 25, star_head=True):
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
    num_star = math.ceil(new_str_len*percent_star)

    if star_head:
        string = num_star * "*" + string[new_str_len - num_star:]
    else:
        string = string[:num_star]  + num_star * "*"

    return string
