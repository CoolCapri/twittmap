class ReadData:

    def read(self, filepath, keywords):
        data = {}
        for keyword in keywords:
            data[keyword] = []

        with open(filepath) as f:
            tweet_lines = f.readlines()
            for i in range(0, 5):
                line = tweet_lines[i]
                print(line)
                for keyword in keywords:
                    if keyword in tweet_lines[i]:
                        data[keyword].append(tweet_lines[i])
        return data
