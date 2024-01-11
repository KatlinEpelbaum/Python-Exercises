import praw
import credentials
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    user_agent="python3:myapp:0.1 (by u/k2tlins)",
)
subredditname = "Eesti"

subreddit = reddit.subreddit(subredditname)

top_subbreddit = subreddit.top()
count = 0
max = 10000
print('success')
words = []
wordCount = {}
commonWords = {'ja','aga','ei','ok','kas','mina','millal','kuidas''ju','mu','lihtsalt','olen','hea','mida','mitte','ning','peale','kus','küll','siin','midagi','saab','palju','need','sa','Kas','välja','oleks','veel','ära','ole','nad','et','nii','seda','pole','mis','oli','ma','ka','siis','kui','kui','Eesti','nagu','See','ikka','selle','kes','Ma','oma','või','väga','ta','mingi','Kui','juba','seal','kõik'}

for submission in subreddit.top(limit=5):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    if(count == max):
            break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

labels = keyWords
sizes = keyCount

plt.title('Top comments for: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

plt.show()

keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

labels = keyWords
sizes = keyCount

plt.title('Top comments for: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  

plt.savefig("matplotlib.png")