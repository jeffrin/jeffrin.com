import os
import frontmatter
from atproto import Client

# Load credentials from GitHub Secrets
BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

# Initialize Bluesky client
client = Client()
client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

# Define the Hugo microblog directory
HUGO_CONTENT_DIR = "content/posts/"  # Adjust if your folder is different

# Get the latest post
posts = sorted(os.listdir(HUGO_CONTENT_DIR), reverse=True)
if not posts:
    print("No posts found.")
    exit()

latest_post = posts[0]
with open(os.path.join(HUGO_CONTENT_DIR, latest_post), "r", encoding="utf-8") as file:
    post = frontmatter.load(file)

post_content = post.content.strip()
post_url = f"https://jeffrin.com/posts/{latest_post.replace('.md', '')}"  # Adjust URL structure if needed

# Post to Bluesky
response = client.post.create(text=f"{post_content}\n\n{post_url}")
print("✅ Posted to Bluesky:", response["uri"])
