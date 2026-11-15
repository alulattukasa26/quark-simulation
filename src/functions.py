def get_quarks_center(quarks_list):
    if not quarks_list:
        return 0, 0
    
    count = len(quarks_list)
    center_x = sum(q.x for q in quarks_list) / count
    center_y = sum(q.y for q in quarks_list) / count
    return center_x, center_y