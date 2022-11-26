from collections import Counter

tweet_names = []

#code to take input
test_case = int(input("N of Test case: "))


for i in range(test_case):
    col = []
    tweets = int(input("N of Tweets: "))
    for j in range(tweets):
        col.append(input())

    tweet_names.append(col)
print(tweet_names)


for tests in tweet_names:
    uniq_names = [pref_names.split()[0] for
                  pref_names in tests]

    times = Counter(uniq_names)
    repeat = times.values()

    for element in set(repeat):
        dupl = ([(key, value) for
                 key, value in sorted(times.items()) if
                 value == element])

        if len(dupl) > 1:
            for (key, value) in dupl:
                print(key, '', value)
        max_value = max(times.values())
        temp_max_result = [(key, value) for
                           key, value in sorted(times.items()) if
                           value == max_value]

        if temp_max_result != dupl:
            for (key, value) in temp_max_result:
                print(key, '', value)
