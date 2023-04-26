# KNN Restaurants Picker

KNN Restaurants Picker is a restaurant recommendation app designed to help indecisive people choose a restaurant conveniently. The app uses a K-Nearest Neighbors (KNN) algorithm to make recommendations based on user preferences and location. The app adapts to user interests over time, making better suggestions as more feedback is provided.

## Background

**Goal:** 

- Help indecisive people choose a restaurant conveniently
- Provide a list of places that are easier to decide on compared to 2D map representations
- Adapt the algorithm to the user's interests over time for better suggestions

## Algorithm Overview

1. Use a map API to get a list of restaurants based on the provided zip code
2. Apply the KNN model to classify each restaurant and assign weights (default to 1 for new users)
3. Store the classified restaurants in a priority queue
4. Update the KNN model based on user feedback (e.g., "Like", "Dislike") to improve future recommendations

## Requirements

- Map API
- KNN Algorithm
- Priority Queue
- User Interface

## Design

- App interface: main screen, buttons, recommendations
- App flow: initialization, user interaction, updating KNN model, recommendation

## Implementation

1. Integrate map API to fetch a list of nearby restaurants based on zip code
2. Implement KNN algorithm with weights
3. Implement priority queue for restaurant recommendations
4. Implement user interface with buttons and actions (e.g., "Like", "Dislike")
5. Store user preferences and update KNN model accordingly

## Testing

- Test app functionality on different devices
- Test accuracy and efficiency of KNN model
- Test app performance under various conditions (e.g., slow internet, location change)

## Deployment

- Deploy the app on the App Store
- Ensure compatibility with iOS devices

## Future Enhancements

- Add support for other platforms (Android, web)
- Expand app capabilities to other types of decision-making
- Improve user interface and user experience
- Add more features (filters, categories, user reviews)
