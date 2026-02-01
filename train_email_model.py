import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Verify your account immediately",
    "Urgent login required now",
    "Reset your password now",
    "Bank account suspended click link",
    "Confirm your identity now",
    "Meeting scheduled tomorrow",
    "Project update attached",
    "Lunch at 2pm?",
    "Team report submitted",
    "Happy birthday!"
]

labels = [
    1,1,1,1,1,   # phishing
    0,0,0,0,0    # safe
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

pickle.dump(model, open("email_model.pkl","wb"))
pickle.dump(vectorizer, open("email_vectorizer.pkl","wb"))

print("✅ Email phishing model created")
