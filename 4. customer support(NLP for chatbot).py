# Import necessary libraries
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

nltk.download('stopwords')
nltk.download('punkt')

# Preprocessing social media data
stop_words = set(nltk.corpus.stopwords.words('english'))

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

social_media_data['processed_text'] = social_media_data['content'].apply(preprocess_text)

# Intent Recognition
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(social_media_data['processed_text'])
y = social_media_data['platform']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Response Generation
response_database = {
    'Twitter': 'Engage with us on Twitter for more updates!',
    'Facebook': 'Join our Facebook community for latest news!',
    'Instagram': 'Follow us on Instagram for stunning visuals!'
}

def get_response(intent):
    return response_database.get(intent, 'Sorry, I did not understand your query.')

# Get response for a customer query
customer_query = "How can I book a trip?"
processed_query = preprocess_text(customer_query)
query_vector = vectorizer.transform([processed_query])
intent = model.predict(query_vector)[0]
response = get_response(intent)
print(f"Customer Query: {customer_query}")
print(f"Response: {response}")


