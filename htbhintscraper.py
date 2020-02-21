import requests
import re
import sys

def getHelp():
    # Print the help text
    print("\nUsage: python " + sys.argv[0] + " [URL]")
    print("Example: python " + sys.argv[0] + " https://forum.hackthebox.eu/discussion/2427/traverxec")
    print("PARAMETERS")
    print("  -h/--help: Print this help.")
    print("\n")

def getMaxPages(r):
    # This will return the current amount of pages of the forum thread
    page = r.text
    maxPagePattern = re.compile('(?<=LastPage">)[^<:]+(?=:?<)')
    maxPage = re.findall(maxPagePattern, page)

    return int(maxPage[0].strip())

def getHints(maxPage, baseUrl):
    dynamicUrl = ""
    userHints = []
    rootHints = []
    userHintCounter = 0
    rootHintCounter = 0
    userPattern = re.compile('[U-u]ser\s?[*]?:[^<:]+(?=<)')
    rootPattern = re.compile('[R-r]oot\s?[*]?:[^<:]+(?=<)')
    
    for i in range(2, maxPage + 1):
        # Construct forum page URLs
        # Check if / has been given at the end of the baseUrl
        if baseUrl[-1:] == "/":
            dynamicUrl = baseUrl + "p" + str(i)
        else:
            dynamicUrl = baseUrl + "/p" + str(i)
        
        # Request forum page source
        r = requests.get(dynamicUrl)
        page = r.text
        
        # Find user hints on current page and add to hints array
        if re.findall(userPattern, page):
            userHints.append(re.findall(userPattern, page)[0])
        # Find root hints on current page and add to hints array
        if re.findall(rootPattern, page):
            rootHints.append(re.findall(rootPattern, page)[0])
        
    print("USER HINTS")
    print("----------")
    for hint in userHints:
        userHintCounter += 1
        hint = re.split(r"user[ *]?:", hint, flags=re.IGNORECASE)
        if hint:
            if len(hint) > 1:
                print(str(userHintCounter) + ". " + hint[1].strip())
            else:
                print(str(userHintCounter) + ". " + hint[0].strip())
    
    print("\nROOT HINTS")
    print("----------")
    for hint in rootHints:
        rootHintCounter += 1
        hint = re.split(r"root[ *]?:", hint, flags=re.IGNORECASE)
        if hint:
            if len(hint) > 1:
                print(str(rootHintCounter) + ". " + hint[1].strip())
            else:
                print(str(rootHintCounter) + ". " + hint[0].strip())

if __name__ == "__main__":
    baseUrl = sys.argv[1]
    
    if baseUrl == "-h" or baseUrl == "--help":
        getHelp()
    else:
        if "https://forum.hackthebox.eu/discussion/" not in baseUrl:
            print("[ERROR] Please provide a valid HTB forum URL.")
            getHelp()
        else:
            # Get page 1 source
            r = requests.get(baseUrl)
            
            # Get current maximum pages
            maxPage = getMaxPages(r)
            
            # Get all hints for the given box
            getHints(maxPage, baseUrl)
