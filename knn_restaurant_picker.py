import tkinter as tk
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
import requests


def fetch_restaurants(zip_code):
    api_key = "YOUR_YELP_API_KEY"
    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api.yelp.com/v3/businesses/search"

    params = {
        "term": "restaurants",
        "location": zip_code,
        "radius": 5000,  # You can adjust the search radius (in meters) as needed
        "limit": 50  # Maximum number of results to return (maximum allowed by Yelp is 50)
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data["businesses"]


def train_knn_model(user_preferences, n_neighbors=5):
    X = [restaurant["coordinates"] for restaurant in user_preferences]
    y = [restaurant["categories"][0]["alias"] for restaurant in user_preferences]

    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X, y)

    return knn


def recommend_restaurants(knn, user_location, all_restaurants):
    X = [restaurant["coordinates"] for restaurant in all_restaurants]
    categories = knn.predict(X)

    recommendations = []
    for idx, restaurant in enumerate(all_restaurants):
        if categories[idx] in user_preferences:
            recommendations.append(restaurant)

    return recommendations


def update_preferences(category, like):
    if like:
        if category not in user_preferences:
            user_preferences.append(category)
    else:
        if category in user_preferences:
            user_preferences.remove(category)


def on_like_dislike(restaurant, like):
    update_preferences(restaurant['categories'][0]['alias'], like)


def display_recommendations(recommendations):
    for widget in recommendations_frame.winfo_children():
        widget.destroy()

    for idx, restaurant in enumerate(recommendations):
        restaurant_label = ttk.Label(recommendations_frame, text=f"{restaurant['name']} ({restaurant['categories'][0]['title']})")
        like_button = ttk.Button(recommendations_frame, text="Like", command=lambda r=restaurant: on_like_dislike(r, True))
        dislike_button = ttk.Button(recommendations_frame, text="Dislike", command=lambda r=restaurant: on_like_dislike(r, False))

        restaurant_label.grid(row=idx, column=0, padx=5, pady=5)
        like_button.grid(row=idx, column=1, padx=5, pady=5)
        dislike_button.grid(row=idx, column=2, padx=5, pady=5)


def on_submit():
    zip_code = zip_entry.get()
    all_restaurants = fetch_restaurants(zip_code)
    knn = train_knn_model(user_preferences)
    recommendations = recommend_restaurants(knn, user_location, all_restaurants)
    display_recommendations(recommendations)


# Initialize the Tkinter app
root = tk.Tk()
root.title("KNN Restaurants Picker")

# Create widgets
zip_label = ttk.Label(root, text="Enter your zip code:")
zip_entry = ttk.Entry(root)
submit_button = ttk.Button(root, text="Submit", command=on_submit)
recommendations_label = ttk.Label(root, text="Recommended Restaurants:")
recommendations_frame = ttk.Frame(root)

# Place widgets on the window
zip_label.grid(row=0, column=0, padx=5, pady=5)
zip_entry.grid(row=0, column=1, padx=5, pady=5)
submit_button.grid(row=1, column=1, padx=5, pady=5)
recommendations_label.grid(row=2, column=0, padx=5, pady=5)
recommendations_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Run the app
root.mainloop()
