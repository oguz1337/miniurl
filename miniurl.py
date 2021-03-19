import pyshorteners

print("""
      __  __ _       _ _   _ ____  _     
     |  \/  (_)_ __ (_) | | |  _ \| |    
     | |\/| | | '_ \| | | | | |_) | |    
     | |  | | | | | | | |_| |  _ <| |___ 
     |_|  |_|_|_| |_|_|\___/|_| \_\_____|
   Coder: SyberCodeV1 & www.sybercodev1.com
""")

def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__ =="__main__":
    url = input("Enter Site Url: ")
    print(f"\nNew Link: {shorten(url)}")
