#!/usr/bin/env python3
import requests
import json


def fetch_posts(): # GET request data from the serever
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json() # return server response

def create_post(data): # POST send data to the server
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    return response.json() # return new-modified data from the server

def update_post(post_id, data): # PUT update data on the server
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=data)
    return response.json() # return updated data from the server

def delete_post(post_id): # DELETE delete data from the server
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return response.status_code # return status code after post is deleted

def save_posts_to_file(posts): # Save fetched posts to a file for offline viewing
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)

def choose_menu_option():
    while True:
        try:
            post_id = int(input("Choose meniu option: "))
            if post_id <= 0 or post_id > 5:
                raise ValueError("Choose a meniu option 1 to 5")
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
            print(f"Invalid input: {e}. Please try again.")

while True: # Run user's menu
    print("\nBlog Manager Menu:")
    print("1. View Posts")
    print("2. Create a New Post")
    print("3. Update a Post")
    print("4. Delete a Post")
    print("5. Exit")
    #choice = input("Choose an option: ")
    choice = choose_menu_option()

    if choice == 1:# GET
        posts = fetch_posts()
        save_posts_to_file(posts[:5]) # Save FETCHED 5 posts to a file
        for post in posts[:5]: # Display first 5 posts
            print(f"ID: {post['id']}, Title: {post['title']}")
    elif choice == 2:# POST
        title = str(input("Enter title: "))
        body = str(input("Enter body: "))
        data = {"title": title, "body": body, "userId": 1}
        print("Post Created:", create_post(data))
    elif choice == 3: # PUT
        #post_id = int(input("Enter post ID to update: "))
        post_id =  get_post_id()
        new_title = str(input("Enter new title: "))
        data = {"title": new_title} 
        print("Post Updated:", update_post(post_id, data))
    elif choice == 4: # DELETE
        #post_id = int(input("Enter post ID to delete: "))
        post_id = get_post_id()
        print(f"\nPost ID {post_id} deleted \nDelete Status:", delete_post(post_id))
    elif choice == 5: # EXIT MENU
        print("Exiting Blog Manager. Goodbye!")
        break
    else:
        print(f"Invalid option. Please try again.")
        
            







#if __name__ == "__main__":
    #main()


