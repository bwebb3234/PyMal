import os
import json
import sqlite3
import shutil
import tempfile
from pathlib import Path
import browser_cookie3

def get_chrome_cookies():
    return browser_cookie3.chrome()

def get_firefox_cookies():
    return browser_cookie3.firefox()

def get_edge_cookies():
    return browser_cookie3.edge()

def get_cookies_for_domain(cookie_jar, domain):
    return [cookie for cookie in cookie_jar if domain in cookie.domain]

def main():
    browsers = {
        "Chrome": get_chrome_cookies,
        "Firefox": get_firefox_cookies,
        "Microsoft Edge": get_edge_cookies
    }

    domain = input("Enter the domain to retrieve cookies for (e.g., example.com): ")

    for browser_name, get_cookies_func in browsers.items():
        try:
            cookie_jar = get_cookies_func()
            domain_cookies = get_cookies_for_domain(cookie_jar, domain)
            
            print(f"\n{browser_name} cookies for {domain}:")
            for cookie in domain_cookies:
                print(f"Name: {cookie.name}, Value: {cookie.value}")
        except Exception as e:
            print(f"Error retrieving {browser_name} cookies: {str(e)}")

if __name__ == "__main__":
    main()