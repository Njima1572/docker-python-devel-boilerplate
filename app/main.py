import os

def is_devel(env) -> bool:
    if env:
        devel_keywords = ['dev', 'debug']
        return any(keyword in env.lower() for keyword in devel_keywords)
    return True

if __name__ == "__main__":
    MODE = is_devel(os.getenv("MODE"))
    print(f'Hello {os.getenv("MODE")}')
    print("DEVEL" if MODE else "PROD" )
