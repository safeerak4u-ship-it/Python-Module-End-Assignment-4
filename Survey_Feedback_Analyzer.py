# Step 1: Preloaded Feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print("Preloaded Feedback Data:")
print(feedback_data)

# Step 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter details for feedback", i + 1)

    name = input("Enter Name: ")
    feedback = input("Enter Written Feedback: ")
    rating = int(input("Enter Rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nUpdated Feedback Data:")
print(feedback_data)

# Step 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    # Remove punctuation
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    # Remove extra spaces and leading/trailing spaces
    text = " ".join(text.split())

    # Convert to lowercase
    text = text.lower()

    # Update the dictionary
    feedback_data['Feedback'][i] = text

print("\nCleaned Feedback Data:")
print(feedback_data['Feedback'])

# Step 4: Word Count Insights

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.lower().split()

        if word.lower() in words:
            count += 1

    return count


print("\nWord Count Insights:")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

# Step 5: Final Summary & Insights

# a. Display the final cleaned feedback_data

print("\nFinal Cleaned Feedback Data:")
print(feedback_data)

# b. Calculate Average Rating

total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))

# c. Find the feedback with the longest comment

longest_feedback = ""
max_word_count = 0

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())

    if word_count > max_word_count:
        max_word_count = word_count
        longest_feedback = feedback

print("\nLongest Feedback:")
print(longest_feedback)
print("Word Count:", max_word_count)

# d. Find unique words across all feedbacks

unique_words = []

for feedback in feedback_data['Feedback']:
    words = feedback.split()

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print("\nUnique Words:")
print(unique_words)

# Optional: Sort feedbacks by rating (highest to lowest)

sorted_feedbacks = sorted(
    zip(feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']),
    key=lambda x: x[2],
    reverse=True
)

print("\nFeedbacks Sorted by Rating:")

for name, feedback, rating in sorted_feedbacks:
    print(name, "|", rating, "|", feedback)