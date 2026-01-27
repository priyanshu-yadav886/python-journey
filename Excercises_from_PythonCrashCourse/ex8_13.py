def build_profile(first, last, **user_info):
    """Build a dictionary containing everthing we know about user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


profile = build_profile('priyanshu', 'yadav', location = 'behror', age = '20')
print(profile)