from _22_2_DB_String._2_FIND_STRING_LENTH._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        st_len = get_len(in_str)
        return st_len


