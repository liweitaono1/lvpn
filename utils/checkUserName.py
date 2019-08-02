def check_user_name(keyword, file_path):
    with open(file_path, 'r') as f:
        while True:
            content = f.readline()
            if content:
                if content in keyword:
                    return False
            else:
                return True
