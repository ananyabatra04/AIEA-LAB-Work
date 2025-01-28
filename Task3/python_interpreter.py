from pyswip import Prolog

prolog = Prolog()

# Loading the knowledge base
prolog.consult("kb.pl")

# Querying for book recommendations based on matching genres
recommendations = set()
print("Book Recommendations:")
for result in prolog.query("recommend_book(Book1, Book2)"):
    recommendation1 = result['Book1']
    recommendation2 = result['Book2']
    if recommendation1 and recommendation2 not in recommendations:
        recommendations.add(recommendation1)
        print(f"If you liked {result['Book1']}, try {result['Book2']} or vice versa")

# Adding new facts
prolog.assertz("book('The Catcher in the Rye')")
prolog.assertz("genre('The Catcher in the Rye', 'Classic')")

# Querying for updated recommendations after adding the new facts
print("\nUpdated Book Recommendations:")
for result in prolog.query("recommend_book(Book1, Book2)"):
    recommendation1 = result['Book1']
    recommendation2 = result['Book2']
    if recommendation1 and recommendation2 not in recommendations:
        recommendations.add(recommendation1)
        print(f"If you liked {result['Book1']}, try {result['Book2']} or vice versa")
