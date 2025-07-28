import browser_cookie3

# Load cookies from your browser for youtube.com
cookies = browser_cookie3.brave(domain_name='youtube.com')

# Save cookies in Netscape format (compatible with yt-dlp)
with open("cookie.txt", "w") as f:
    f.write("# Netscape HTTP Cookie File\n")
    for cookie in cookies:
        f.write(
            f"{cookie.domain}\t"
            f"{'TRUE' if cookie.domain.startswith('.') else 'FALSE'}\t"
            f"{cookie.path}\t"
            f"{'TRUE' if cookie.secure else 'FALSE'}\t"
            f"{cookie.expires or 0}\t"
            f"{cookie.name}\t"
            f"{cookie.value}\n"
        )

print("✅ cookies.txt saved successfully.")
