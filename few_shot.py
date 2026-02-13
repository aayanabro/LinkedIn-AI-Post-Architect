import pandas as pd
import json

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as f: # Fixed: utf-8
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            
            # Map length to capitalized versions to match UI dropdowns
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            
            # Flatten the list of tags to get unique ones
            all_tags = [tag for sublist in self.df['tags'] for tag in sublist]
            self.unique_tags = set(all_tags)

    def categorize_length(self, line_count):
        if line_count < 6:
            return "Short"
        elif 6 <= line_count <= 15:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient='records')

if __name__ == "__main__":
    fs = FewShotPosts()
    print(fs.get_tags())