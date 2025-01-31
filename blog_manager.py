#!/usr/bin/env python3
import requests
import json
base_url = "https://jsonplaceholder.typicode.com/posts"

def http_get_request(url):
    try:
        return requests.get(url).json() # Attempt GET and parse JSON
    except requests.exceptions.RequestException as e:
        print(f"GET request failed: {e}")
        return None # Graceful exit on error
    
def http_post_request(url, payload):
    try:
        return requests.post(url, json=payload).json() # Atempt POST and parse JSON
    except requests.exceptions.RequestException as e:
        print(f"POST request failed: {e}")
        return None # Exit on error

def http_put_request(url, payload):
    try:
        return requests.put(url, json=payload).json() # Attempt PUT and parse JSON
    except requests.exceptions.RequestException as e:
        return None # Exit on error

def http_delete_request(url):
    try:
        return requests.delete(url).status_code # Attempt DELETE and return status code
    except requests.exceptions.RequestException as e:
        return None # Exit on error

def save_posts_to_file(posts): # Save fetched posts to a file for offline viewing
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)

def choose_menu_option():
    while True:
        try:
            post_id = int(input("Choose meniu option (1-5): "))
            if post_id <= 0 or post_id > 5:
                raise ValueError("Choose a meniu option (1-5)")
            return post_id
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def get_post_id():
    while True:
        try:
            post_id = int(input("Enter post ID: "))
            if not isinstance(post_id, int):
                raise ValueError("Post ID must be an integer")
            return post_id
        except ValueError as e:
            print(f"Input error : {e}. Please try again.")

while True: # Run user's menu
    print("\nBlog Manager Menu:")
    print("1. View Posts")
    print("2. Create a New Post")
    print("3. Update a Post")
    print("4. Delete a Post")
    print("5. Exit")
    choice = choose_menu_option()

    if choice == 1:# GET
        posts = http_get_request(base_url)
        if posts:
            for post in posts[:5]: # Display first 5 posts
                print(f"ID: {post['id']}, Title: {post['title']}")
            save_posts_to_file(posts[:5]) # Save 5 posts to a file
        else:
            print("Failed to fetch data")
            break
    elif choice == 2:# POST
        title = str(input("Enter title: "))
        body = str(input("Enter body: "))
        data = {"title": title, "body": body, "userId": 1}
        response = http_post_request(base_url, data)
        if response:
            print("Post Created: ", response)
        else:
            print(f"Failed to create post. {response.status_code}")
            break
    elif choice == 3: # PUT
        post_id =  get_post_id()
        new_title = str(input("Enter new title: "))
        data = {"title": new_title}
        dynamic_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  
        response = http_put_request(dynamic_url, data)
        if response:
            print("Post Updated:", response)
        else:
            print("Failed to update post.\nPost ID out of range\nTry again")
            break
    elif choice == 4: # DELETE
        post_id = get_post_id()
        dynamic_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = http_delete_request(dynamic_url)
        if response:
            print(f"\nPost ID {post_id} deleted \nDelete Status:", response)
        else:
            print("Failed to delete post.")
            break
    elif choice == 5: # EXIT MENU
        print("Exiting Blog Manager. Goodbye!")
        break
    else:
        print(f"Invalid option. Please try again.")
        
            







#if __name__ == "__main__":
    #main()


