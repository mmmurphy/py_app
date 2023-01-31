import os, platform, socket

def mrm_format_dict(dict) -> str:
   result = ""
   for key in dict:
      result += f'"{key}":  "{dict[key]}"\n'
   return result


print("Python runtime version: ", platform.python_version(), '\n\n')

print("Your network hostname:  ", socket.gethostname(), '\n\n')

print("O/S Environment:\n\n")
print(mrm_format_dict(os.environ), '\n\n')


#print("your o/s login is:        ", os.getlogin())
#print("Your o/s env username:    ", os.environ.get('USERNAME'))
#
#print("your o/s env hostname:    ", os.environ.get('userdomain'))
#print("your o/s env hostname:    ", os.getenv('hostname'))
#print("your o/s env computername:", os.getenv('computername'))
#
#print("your platform node:       ", platform.node())
#print()
#
#

